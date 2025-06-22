-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Dec 08, 2024 at 10:13 AM
-- Server version: 10.4.32-MariaDB
-- PHP Version: 8.2.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `edu_ai_museum_management_system`
--

-- --------------------------------------------------------

--
-- Table structure for table `ai_specimens`
--

CREATE TABLE `ai_specimens` (
  `Specimen_ID` int(11) NOT NULL,
  `Section_ID` int(11) DEFAULT NULL,
  `Specimen_Title` varchar(100) NOT NULL,
  `Specimen_Description` text DEFAULT NULL,
  `Developed_By` int(11) DEFAULT NULL,
  `Date_of_Creation` date DEFAULT NULL,
  `Specimen_Category` enum('Prototype','Research Project','Art Installation','Educational Tool') NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `ai_specimens`
--

INSERT INTO `ai_specimens` (`Specimen_ID`, `Section_ID`, `Specimen_Title`, `Specimen_Description`, `Developed_By`, `Date_of_Creation`, `Specimen_Category`) VALUES
(1, 1, 'AI Diagnosis Assistant', 'An AI system to assist doctors in diagnosing diseases with high accuracy.', 1, '2023-09-20', 'Research Project'),
(2, 1, 'Smart Health Wearable', 'A device powered by AI to monitor and predict patient health metrics.', 2, '2023-11-01', 'Prototype'),
(3, 1, 'Virtual Surgery Assistant', 'An AI assistant that helps surgeons plan and execute complex procedures.', 1, '2024-01-15', 'Educational Tool'),
(4, 2, 'Creative AI Painter', 'An AI system that creates unique artworks based on user input.', 3, '2023-10-05', 'Art Installation'),
(5, 2, 'Music Composer AI', 'A generative AI that composes music in various genres.', 6, '2023-11-10', 'Research Project'),
(6, 2, 'AI Storyteller', 'A creative writing assistant that crafts short stories based on prompts.', 5, '2023-12-01', 'Educational Tool'),
(7, 3, 'RoboArm v3', 'A robotic arm capable of precise and intricate movements using AI.', 4, '2023-08-12', 'Prototype'),
(8, 3, 'Autonomous Drone AI', 'An AI-powered drone for real-time object detection and navigation.', 7, '2023-09-25', 'Research Project'),
(9, 3, 'Humanoid Assistant Bot', 'A robot with speech recognition and task automation for assistance.', 10, '2023-11-30', 'Educational Tool'),
(10, 4, 'Smart Vision AI', 'An AI-powered vision system that can identify objects with high accuracy.', 8, '2023-10-15', 'Research Project'),
(11, 4, 'Language Translation AI', 'An NLP-based system for real-time multilingual translation.', 9, '2023-12-10', 'Educational Tool'),
(12, 4, 'Emotion Recognition AI', 'AI that analyzes text and speech to identify emotional tone.', 4, '2024-01-05', 'Prototype'),
(13, 5, 'Pattern Recognition AI', 'A neural network that identifies patterns in images and datasets.', 3, '2023-09-15', 'Educational Tool'),
(14, 5, 'Predictive Analytics Tool', 'A neural network system for predicting trends in large datasets.', 2, '2023-11-05', 'Research Project'),
(15, 5, 'Deep Learning Simulator', 'An interactive tool to demonstrate how deep learning algorithms work.', 4, '2024-01-20', 'Prototype');

-- --------------------------------------------------------

--
-- Table structure for table `developers_list`
--

CREATE TABLE `developers_list` (
  `Developer_ID` int(11) NOT NULL,
  `Developer_Name` varchar(100) NOT NULL,
  `Developer_Type` enum('Faculty','Student') NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `developers_list`
--

INSERT INTO `developers_list` (`Developer_ID`, `Developer_Name`, `Developer_Type`) VALUES
(1, 'Prof. Mahbub Alam', 'Faculty'),
(2, 'Prof. Sumaiya Akhter', 'Faculty'),
(3, 'Prof. Fakhrul Islam', 'Faculty'),
(4, 'Prof. Azizur Rahman', 'Faculty'),
(5, 'Intesar Hossain', 'Student'),
(6, 'Asif Iqbal', 'Student'),
(7, 'Afia Rahman', 'Student'),
(8, 'Zarin Tasfia', 'Student'),
(9, 'Nafis Rahman', 'Student'),
(10, 'Tariq Anwar', 'Student');

-- --------------------------------------------------------

--
-- Table structure for table `museum_sections`
--

CREATE TABLE `museum_sections` (
  `Section_ID` int(11) NOT NULL,
  `Section_Title` varchar(100) NOT NULL,
  `Section_Description` text DEFAULT NULL,
  `Managed_By_Professor` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `museum_sections`
--

INSERT INTO `museum_sections` (`Section_ID`, `Section_Title`, `Section_Description`, `Managed_By_Professor`) VALUES
(1, 'Smart Healthcare Zone', 'Exploring AI applications in diagnostics, patient care, and wearable health technologies.', 101),
(2, 'AI in Creativity', 'Showcasing generative art, AI-driven music composition, and creative writing tools.', 102),
(3, 'Cognitive Robotics Lab', 'A collection of intelligent robots that mimic human-like decision-making and movements.', 103),
(4, 'Vision and Language Studio', 'Highlights AI applications in image recognition, natural language processing, and creative AI systems like generative art.', 104),
(5, 'Neural Networks Playground', 'Interactive exhibits demonstrating neural network models and their applications.', 105);

-- --------------------------------------------------------

--
-- Table structure for table `museum_visitors`
--

CREATE TABLE `museum_visitors` (
  `Visitor_ID` int(11) NOT NULL,
  `Visitor_FullName` varchar(100) NOT NULL,
  `Contact_Number` varchar(15) DEFAULT NULL,
  `Contact_Email` varchar(100) DEFAULT NULL,
  `Visitor_Address` text DEFAULT NULL,
  `Visited_Date` date DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `museum_visitors`
--

INSERT INTO `museum_visitors` (`Visitor_ID`, `Visitor_FullName`, `Contact_Number`, `Contact_Email`, `Visitor_Address`, `Visited_Date`) VALUES
(1, 'Farhana Rahman', '01712345678', 'farhana.rahman@gmail.com', 'Dhanmondi, Dhaka', '2024-11-06'),
(2, 'Suman Chatterjee', '01898765432', 'suman.chatterjee@gmail.com', 'Agrabad, Chattogram', '2024-10-23'),
(3, 'Tahmid Hossain', '01611223344', 'tahmid.hossain@gmail.com', 'Banani, Dhaka', '2024-11-13'),
(4, 'Ritu Saha', '01754321678', 'ritu.saha@gmail.com', 'Mirpur, Dhaka', '2024-10-24'),
(5, 'Arifuzzaman Siddique', '01567891234', 'arif.siddique@gmail.com', 'Khulshi, Chattogram', '2024-11-21'),
(6, 'Priya Sen', '01922113355', 'priya.sen@gmail.com', 'Uttara, Dhaka', '2024-12-01'),
(7, 'Nafis Ahmed', '01844556677', 'nafis.ahmed@gmail.com', 'Rajshahi City, Rajshahi', '2024-10-31'),
(8, 'Anika Chowdhury', '01766778899', 'anika.chowdhury@gmail.com', 'Sylhet City, Sylhet', '2024-11-15'),
(9, 'Soumitra Ghosh', '01912345678', 'soumitra.ghosh@gmail.com', 'Gulshan, Dhaka', '2024-11-07'),
(10, 'Sharmin Akhter', '01633445566', 'sharmin.akhter@gmail.com', 'Bogura Sadar, Bogura', '2024-10-22'),
(11, 'Bijoy Das', '01555667788', 'bijoy.das@gmail.com', 'Kumira, Chattogram', '2024-11-10'),
(12, 'Tamanna Haque', '01899887766', 'tamanna.haque@gmail.com', 'Barishal Sadar, Barishal', '2024-09-21');

-- --------------------------------------------------------

--
-- Table structure for table `professors_info`
--

CREATE TABLE `professors_info` (
  `Professor_ID` int(11) NOT NULL,
  `Full_Name` varchar(100) NOT NULL,
  `Dept_Name` varchar(50) DEFAULT 'CSE',
  `Start_Date` date DEFAULT NULL,
  `End_Date` date DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `professors_info`
--

INSERT INTO `professors_info` (`Professor_ID`, `Full_Name`, `Dept_Name`, `Start_Date`, `End_Date`) VALUES
(101, 'Dr. Farid Ahmed', 'CSE', '2023-08-01', '2023-10-01'),
(102, 'Dr. Mahbub Alam', 'CSE', '2023-10-01', '2023-12-01'),
(103, 'Prof. Khalid Hasan', 'CSE', '2023-12-01', '2024-02-01'),
(104, 'Prof. Saifur Rahman', 'CSE', '2024-02-01', '2024-04-01'),
(105, 'Prof. Ayesha Sultana', 'CSE', '2024-05-01', '2024-07-01'),
(106, 'Prof. Nusrat Jahan', 'CSE', '2024-07-01', '2024-09-01'),
(107, 'Prof. Fakhrul Islam', 'CSE', '2024-09-01', '2024-11-01'),
(108, 'Prof. Azizur Rahman', 'CSE', '2024-11-01', '2025-01-01'),
(109, 'Prof. Naznin Ferdous', 'CSE', '2025-01-01', '2025-03-01'),
(110, 'Prof. Sumaiya Akhter', 'CSE', '2025-03-01', '2025-05-01'),
(111, 'Prof. Sadia Karim', 'CSE', '2025-05-01', '2025-07-01'),
(112, 'Prof. Farzana Yasmin', 'CSE', '2025-07-01', '2025-09-02');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `ai_specimens`
--
ALTER TABLE `ai_specimens`
  ADD PRIMARY KEY (`Specimen_ID`),
  ADD KEY `Section_ID` (`Section_ID`),
  ADD KEY `Developed_By` (`Developed_By`);

--
-- Indexes for table `developers_list`
--
ALTER TABLE `developers_list`
  ADD PRIMARY KEY (`Developer_ID`);

--
-- Indexes for table `museum_sections`
--
ALTER TABLE `museum_sections`
  ADD PRIMARY KEY (`Section_ID`),
  ADD KEY `Managed_By_Professor` (`Managed_By_Professor`);

--
-- Indexes for table `museum_visitors`
--
ALTER TABLE `museum_visitors`
  ADD PRIMARY KEY (`Visitor_ID`);

--
-- Indexes for table `professors_info`
--
ALTER TABLE `professors_info`
  ADD PRIMARY KEY (`Professor_ID`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `ai_specimens`
--
ALTER TABLE `ai_specimens`
  MODIFY `Specimen_ID` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=16;

--
-- AUTO_INCREMENT for table `developers_list`
--
ALTER TABLE `developers_list`
  MODIFY `Developer_ID` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=11;

--
-- AUTO_INCREMENT for table `museum_sections`
--
ALTER TABLE `museum_sections`
  MODIFY `Section_ID` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- AUTO_INCREMENT for table `museum_visitors`
--
ALTER TABLE `museum_visitors`
  MODIFY `Visitor_ID` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=13;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `ai_specimens`
--
ALTER TABLE `ai_specimens`
  ADD CONSTRAINT `ai_specimens_ibfk_1` FOREIGN KEY (`Section_ID`) REFERENCES `museum_sections` (`Section_ID`),
  ADD CONSTRAINT `ai_specimens_ibfk_2` FOREIGN KEY (`Developed_By`) REFERENCES `developers_list` (`Developer_ID`);

--
-- Constraints for table `museum_sections`
--
ALTER TABLE `museum_sections`
  ADD CONSTRAINT `museum_sections_ibfk_1` FOREIGN KEY (`Managed_By_Professor`) REFERENCES `professors_info` (`Professor_ID`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
