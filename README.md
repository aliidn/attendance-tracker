# Simple Attendance Tracker

A Python-based automation tool designed to manage attendance for 20,000 students across multiple subjects. This project demonstrates efficient data handling with Pandas and automated threshold monitoring.

## 🚀 Features
* **Scalable Data Processing:** Handles 20,000+ records using optimized Pandas operations (`.loc`, `.isin`).
* **Automated Data Transformation:** Dynamically generates student email addresses using Lambda functions.
* **Threshold Logic:** * **2 Leaves:** Triggers a "Warning" status.
  * **3+ Leaves:** Triggers an "Attendance Alert" for students and staff.
* **Persistent Storage:** Automatically updates and saves records to CSV.

## 📊 Dataset Structure
The system utilizes a central `Attendance1.csv` with the following schema:
| Student ID | CI | python | DM | mailid |
| :--- | :--- | :--- | :--- | :--- |
| 1 | 0 | 0 | 0 | student_1@gmail.com |

## 🛠️ Installation & Usage
1. **Clone the repository:**
   ```bash
   git clone https://github.com/YourUsername/AttendanceTracker.git
