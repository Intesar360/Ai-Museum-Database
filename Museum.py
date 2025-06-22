import tkinter as tk
from tkinter import messagebox, simpledialog
from tkinter import ttk
from PIL import Image, ImageTk
import mysql.connector


class MuseumLoginApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Museum Management System - Login")
        self.root.geometry("500x500")
        self.root.resizable(False, False)
        self.root.configure(bg="#87CEEB")

        # Database configuration
        self.db_config = {
            'host': 'localhost',
            'user': 'root',
            'password': '',
            'database': 'edu_ai_museum_management_system'
        }

        # Create a custom style for buttons
        self.style = ttk.Style()
        self.style.configure(
            "TButton",
            font=("Arial", 12, "bold"),
            padding=10,
            borderwidth=3,
            relief="solid",
            background="#000000",  # Steel blue background
            foreground="#000000"
        )
        self.style.map(
            "TButton",
            foreground=[("active", "#000000")],
            background=[("active", "#45a049")],
        )
        

        # GUI Elements
        self.create_login_frame()

    def create_login_frame(self):
        self.login_frame = ttk.Frame(self.root, padding="20")
        self.login_frame.place(relx=0.5, rely=0.5, anchor="center")

        # Load and display the image
        try:
            image_path = "F:\\VS Code\\logo.png"  # Replace with your image file path
            image = Image.open(image_path)  # Open the image file
            image = image.resize((200, 200), Image.Resampling.LANCZOS)  # Resize the image
            self.logo = ImageTk.PhotoImage(image)  # Convert to a Tkinter-compatible image
            image_label = tk.Label(self.login_frame, image=self.logo, background="#f0f0f0")
            image_label.grid(row=0, column=0, columnspan=2, pady=10)  # Place the image
        except FileNotFoundError:
            print(f"Error: The image file '{image_path}' was not found.")
            messagebox.showerror("Image Error", f"The image file '{image_path}' was not found.")
        except Exception as e:
            print(f"Error loading image: {e}")
            messagebox.showerror("Image Error", f"An unexpected error occurred: {e}")

        # Remaining Login Form Elements
        ttk.Label(
            self.login_frame, 
            text="Museum Login", 
            font=("Arial", 16, "bold")
        ).grid(row=1, column=0, columnspan=2, pady=10)

        ttk.Label(self.login_frame, text="Username:", font=("Arial", 12, "bold")).grid(row=2, column=0, pady=5, sticky="e")
        self.username_entry = ttk.Entry(self.login_frame, width=30)
        self.username_entry.grid(row=2, column=1, pady=5)

        ttk.Label(self.login_frame, text="Password:", font=("Arial", 12, "bold")).grid(row=3, column=0, pady=5, sticky="e")
        self.password_entry = ttk.Entry(self.login_frame, show="*", width=30)
        self.password_entry.grid(row=3, column=1, pady=5)

        ttk.Button(
            self.login_frame, 
            text="Login", 
            style="TButton", 
            command=self.authenticate_user
        ).grid(row=4, column=0, columnspan=2, pady=20)

    def authenticate_user(self):
        username = self.username_entry.get()
        password = self.password_entry.get()

        try:
            connection = mysql.connector.connect(**self.db_config)
            cursor = connection.cursor(dictionary=True)

            query = "SELECT * FROM users WHERE username = %s AND password = %s"
            cursor.execute(query, (username, password))
            user = cursor.fetchone()

            if user:
                role = user['role']
                messagebox.showinfo("Login Successful", f"Welcome {role.capitalize()}!")
                self.open_dashboard(role)
            else:
                messagebox.showerror("Login Failed", "Invalid credentials. Please try again.")

        except mysql.connector.Error as err:
            messagebox.showerror("Database Error", f"Error: {err}")

        finally:
            if 'connection' in locals() and connection.is_connected():
                cursor.close()
                connection.close()

    def open_dashboard(self, role):
        if role == "admin":
            self.open_admin_dashboard()
        elif role == "guest":
            self.open_guest_dashboard()

    def open_admin_dashboard(self):
        admin_window = tk.Toplevel(self.root)
        admin_window.title("Admin Dashboard")
        admin_window.geometry("400x500")
        admin_window.resizable(False, False)
        admin_window.configure(bg="#f0f4f7")

        try:
            image_path = (r"F:\vs code\admin.png")
            image = Image.open(image_path)  # Replace with your image path
            image = image.resize((250, 250), Image.LANCZOS)
            photo = ImageTk.PhotoImage(image)
            img_label = tk.Label(admin_window, image=photo, bg="#f0f4f7")
            img_label.image = photo  # Keep reference to avoid garbage collection
            img_label.pack(pady=10)
        except Exception as e:
            messagebox.showerror("Error", f"Unable to load image: {e}")


        ttk.Label(admin_window, text="Admin Dashboard", font=("Arial", 16, "bold")).pack(pady=10)

        # Create stylish buttons for the admin dashboard
        ttk.Button(admin_window, text="View Data", style="TButton", command=self.view_data).pack(pady=5)
        ttk.Button(admin_window, text="Edit Data", style="TButton", command=self.select_table).pack(pady=5)
        

    def open_guest_dashboard(self):
        guest_window = tk.Toplevel(self.root)
        guest_window.title("Welcome!")
        guest_window.geometry("400x400")
        guest_window.resizable(False, False)
        guest_window.configure(bg="#f0f4f7")

        try:
            image_path = (r"F:\vs code\welcome.png")
            image = Image.open(image_path)  # Replace with your image path
            image = image.resize((200, 200), Image.LANCZOS)
            photo = ImageTk.PhotoImage(image)
            img_label = tk.Label(guest_window, image=photo, bg="#f0f4f7")
            img_label.image = photo  # Keep reference to avoid garbage collection
            img_label.pack(pady=10)
        except Exception as e:
            messagebox.showerror("Error", f"Unable to load image: {e}")

        ttk.Label(guest_window, text="Let's Visit Our Museum!", font=("Arial", 16, "bold")).pack(pady=10)

        # Create stylish buttons for the guest dashboard
        ttk.Button(guest_window, text="Enter", style="TButton", command=self.view_data).pack(pady=5)

    # Other methods (view_data, add_data, edit_data, delete_data) remain unchanged.
    def view_data(self):
        table_name_mapping = {
        "ai_specimens": "AI Specimens",
        "developers_list": "Developers List",
        "museum_sections": "Museum Sections",
        "museum_visitors": "Museum Visitors",
        "professors_info": "Professors Information",
        "users": "User Accounts"
    }
        try:
            connection = mysql.connector.connect(**self.db_config)
            cursor = connection.cursor()

            query = "SHOW TABLES In edu_ai_museum_management_system  WHERE Tables_in_edu_ai_museum_management_system != 'users';  "
            cursor.execute(query)

            tables = cursor.fetchall()
            table_list = [table[0] for table in tables]

            view_window = tk.Toplevel(self.root)
            view_window.title("View Data")
            view_window.geometry("400x400")
            view_window.resizable(False, False)
            view_window.configure(bg="#f0f4f7")

            ttk.Label(view_window, text="View Information", font=("Arial", 14)).pack(pady=10)

            for table in table_list:
                display_name = table_name_mapping.get(table, table)
                ttk.Button(view_window, text=display_name, command=lambda t=table: self.show_table_data(t)).pack(pady=5)

        except mysql.connector.Error as err:
            messagebox.showerror("Database Error", f"Error: {err}")

        finally:
            if 'connection' in locals() and connection.is_connected():
                cursor.close()
                connection.close()
    def edit_table_interactively(self, table_name):
        try:
            connection = mysql.connector.connect(**self.db_config)
            cursor = connection.cursor(dictionary=True)

            # Fetch data and column names from the table
            cursor.execute(f"SELECT * FROM {table_name}")
            rows = cursor.fetchall()
            columns = [desc[0] for desc in cursor.description]

            # Create a new window for the interactive table
            table_window = tk.Toplevel(self.root)
            table_window.title(f"Edit Table: {table_name}")
            table_window.geometry("800x500")
            table_window.configure(bg="#f0f4f7")

            ttk.Label(table_window, text=f"Editing Table: {table_name}", font=("Arial", 14, "bold")).pack(pady=10)

            # Create Treeview widget
            tree_frame = ttk.Frame(table_window)
            tree_frame.pack(fill="both", expand=True, padx=10, pady=10)

            tree = ttk.Treeview(tree_frame, columns=columns, show="headings")
            tree.pack(side="left", fill="both", expand=True)

            # Configure odd and even row styles
            tree.tag_configure("odd", background="#f2f2f2")  # Light gray background for odd rows
            tree.tag_configure("even", background="#ffffff")  # White background for even rows

            # Insert existing rows
            for i, row in enumerate(rows):
                row_tag = "odd" if i % 2 == 0 else "even"
                tree.insert("", "end", values=list(row.values()), tags=row_tag)

            scrollbar = ttk.Scrollbar(tree_frame, orient="vertical", command=tree.yview)
            scrollbar.pack(side="right", fill="y")
            tree.configure(yscrollcommand=scrollbar.set)

            # Functions to handle edits
            def edit_cell(event):
                selected_item = tree.focus()
                column = tree.identify_column(event.x)
                col_index = int(column.strip("#")) - 1  # Adjusting column index
                col_name = columns[col_index]
                original_value = tree.item(selected_item)["values"][col_index]

                new_value = simpledialog.askstring("Edit Cell", f"Edit {col_name}:",
                                                initialvalue=original_value)
                if new_value is not None:
                    tree.set(selected_item, column=col_name, value=new_value)

            def add_row():
                new_row = [""] * len(columns)  # Create empty row
                current_row_count = len(tree.get_children())  # Get the current number of rows
                if current_row_count % 2 == 0:
                    row_tag = "odd"  # Even number of rows (0, 2, 4...) -> odd tag
                else:
                    row_tag = "even"  # Odd number of rows (1, 3, 5...) -> even tag
                
                tree.insert("", "end", values=new_row, tags=row_tag)  # Insert with appropriate tag

            def delete_selected_row():
                selected_item = tree.focus()
                if selected_item:
                    tree.delete(selected_item)

            def save_changes():
                try:
                    # Ensure the connection is open
                    connection = mysql.connector.connect(**self.db_config)
                    cursor = connection.cursor()

                    # First, delete all rows in the table
                    cursor.execute(f"DELETE FROM {table_name}")
                    connection.commit()

                    # Insert all rows from the Treeview back into the table
                    for item in tree.get_children():
                        row_values = tree.item(item)["values"]
                        placeholders = ", ".join(["%s"] * len(columns))
                        query = f"INSERT INTO {table_name} ({', '.join(columns)}) VALUES ({placeholders})"
                        cursor.execute(query, row_values)

                    connection.commit()  # Commit the changes
                    messagebox.showinfo("Success", "Changes saved successfully!")

                except mysql.connector.Error as err:
                    messagebox.showerror("Error", f"Could not save changes: {err}")

                finally:
                    # Ensure that the cursor and connection are closed after the operation
                    if 'cursor' in locals():
                        cursor.close()
                    if 'connection' in locals() and connection.is_connected():
                        connection.close()

            # Bind the double-click event to edit cells
            tree.bind("<Double-1>", edit_cell)

            # Buttons for adding, deleting, and saving changes
            button_frame = ttk.Frame(table_window)
            button_frame.pack(pady=10)

            ttk.Button(button_frame, text="Add Row", command=add_row).pack(side="left", padx=10)
            ttk.Button(button_frame, text="Delete Selected Row", command=delete_selected_row).pack(side="left", padx=10)
            ttk.Button(button_frame, text="Save Changes", command=save_changes).pack(side="left", padx=10)

        except mysql.connector.Error as err:
            messagebox.showerror("Database Error", f"Error: {err}")
        finally:
            if 'connection' in locals() and connection.is_connected():
                cursor.close()
                connection.close()





    def select_table(self):
        """Open a dropdown menu to select a table and then edit it interactively."""
        try:
            connection = mysql.connector.connect(**self.db_config)
            cursor = connection.cursor()

            # Fetch table names
            cursor.execute("SHOW TABLES In edu_ai_museum_management_system  WHERE Tables_in_edu_ai_museum_management_system != 'users';  ")
            tables = [table[0] for table in cursor.fetchall()]

            if not tables:
                messagebox.showinfo("No Tables", "No tables available in the database.")
                return

            # Create a selection window
            select_window = tk.Toplevel(self.root)
            select_window.title("Select Table")
            select_window.geometry("300x150")
            select_window.resizable(False, False)

            ttk.Label(select_window, text="Select a Table:", font=("Arial", 12, "bold")).pack(pady=10)

            table_var = tk.StringVar()
            table_dropdown = ttk.Combobox(select_window, textvariable=table_var, values=tables, state="readonly")
            table_dropdown.pack(pady=5)
            table_dropdown.current(0)  # Select the first table by default

            def confirm_selection():
                selected_table = table_var.get()
                if selected_table:
                    select_window.destroy()
                    self.edit_table_interactively(selected_table)

            ttk.Button(select_window, text="Confirm", command=confirm_selection).pack(pady=10)

        except mysql.connector.Error as err:
            messagebox.showerror("Database Error", f"Error: {err}")

        finally:
            if 'connection' in locals() and connection.is_connected():
                cursor.close()
                connection.close()

    
    def show_table_data(self, table_name):
        try:
            connection = mysql.connector.connect(**self.db_config)
            cursor = connection.cursor()

            query = f"SELECT * FROM {table_name}"
            cursor.execute(query)
            rows = cursor.fetchall()
            columns = [desc[0] for desc in cursor.description]

            data_window = tk.Toplevel(self.root)
            data_window.title(f"Data from {table_name}")
            data_window.geometry("800x400")
            data_window.configure(bg="#f0f4f7")

            ttk.Label(data_window, text=f"Table: {table_name}", font=("Arial", 14, "bold")).pack(pady=10)

            tree_frame = ttk.Frame(data_window)
            tree_frame.pack(fill="both", expand=True, padx=10, pady=10)

            tree = ttk.Treeview(tree_frame, columns=columns, show="headings")
            tree.pack(side="left", fill="both", expand=True)

            for col in columns:
                tree.heading(col, text=col)
                tree.column(col, anchor="center", width=100)

            # Insert rows with alternating colors
            for index, row in enumerate(rows):
                row_values = tuple(row)
                color = "#f9f9f9" if index % 2 == 0 else "#e0e0e0"  # Alternating row colors
                tree.insert("", "end", values=row_values, tags=("even" if index % 2 == 0 else "odd"))

            # Style for alternating row colors
            tree.tag_configure("even", background="#f9f9f9")
            tree.tag_configure("odd", background="#e0e0e0")

            scrollbar = ttk.Scrollbar(tree_frame, orient="vertical", command=tree.yview)
            scrollbar.pack(side="right", fill="y")
            tree.configure(yscrollcommand=scrollbar.set)

        except mysql.connector.Error as err:
            messagebox.showerror("Database Error", f"Error: {err}")

        finally:
            if 'connection' in locals() and connection.is_connected():
                cursor.close()
                connection.close()



if __name__ == "__main__":
    root = tk.Tk()
    app = MuseumLoginApp(root)
    root.mainloop()
