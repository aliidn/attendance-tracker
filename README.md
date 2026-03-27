# Simple Attendance Tracker

A Python-based automation tool designed to manage attendance for 20,000 students across multiple subjects. This project demonstrates efficient data handling with Pandas and automated threshold monitoring.

## 🚀 Key Features
* **Vectorized Data Updates:** Uses Pandas `.loc` and `.isin()` to update thousands of records simultaneously, ensuring high performance regardless of dataset size.
* **Robust Input Validation:**
    * **Type Safety:** Uses `try/except` blocks to handle non-numeric inputs for subjects.
    * **ID Verification:** Uses list comprehensions with `.isdigit()` and `.values` checks to filter out typos or non-existent Student IDs before processing.
* **Modular Notification System:** Features a dedicated `send_email` function that separates attendance logic from the notification process.
* **Dynamic Email Generation:** Automatically generates a `mailid` column based on Student IDs using Lambda functions.
* **Threshold Monitoring:**
    * **2 Leaves:** Triggers a "warning" status.
    * **3+ Leaves:** Triggers an "alert" status for both the student and administrative staff.
 
## 📊 Dataset Structure
The system utilizes a central `Attendance1.csv` with the following schema:
| Student ID | CI | python | DM | mailid |
| :--- | :--- | :--- | :--- | :--- |
| 1 | 0 | 0 | 0 | student_1@gmail.com |

## 🛠️ Installation & Usage
1. **Clone the repository:**
   ```bash
   git clone https://github.com/YourUsername/AttendanceTracker.git
