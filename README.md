# Finance Project

This project is a comprehensive solution for personal finance management, featuring a backend server, a mobile application, and machine learning models for expense prediction.

## Project Structure

The project is organized into the following directories:

- `backend/`: Contains the backend server code, built with Python and FastAPI.
- `mobile/`: Contains the mobile application code, built with React Native.
- `data/`: Stores data files, including sample transactions and trained machine learning models.
- `scripts/`: Includes various utility scripts for running the project, seeding the database, etc.
- `finance_env/`: A Python virtual environment for the backend.

## Features

### Backend

- **API Server**: A robust API server built with FastAPI that serves data to the mobile app.
- **User Authentication**: Secure user authentication using JWT.
- **Database Integration**: Connects to a MongoDB database to store user and transaction data.
- **Expense Prediction**: Utilizes machine learning models to predict future expenses.

### Mobile App

- **Cross-Platform**: Built with React Native for both Android and iOS.
- **User-Friendly Interface**: A clean and intuitive interface for managing finances.
- **Transaction Management**: Allows users to view, add, and categorize their expenses.
- **Expense Visualization**: Presents financial data in the form of charts and graphs.
- **Real-time Updates**: Fetches and displays real-time data from the backend.

## Getting Started

### Prerequisites

- **Node.js**: Required for the mobile app.
- **Python**: Required for the backend server.
- **Conda**: Used for managing the Python environment.
- **Android Studio/Xcode**: Required for running the mobile app on an emulator or device.

### Installation

1. **Clone the repository:**
   ```bash
   git clone <repository-url>
   ```
2. **Backend Setup:**
   - Navigate to the `scripts` directory.
   - Run the setup script:
     ```bash
     setup.bat
     ```
3. **Mobile App Setup:**
   - Navigate to the `mobile` directory.
   - Install the required Node.js modules:
     ```bash
     npm install
     ```

### Running the Project

1. **Run the Backend Server:**
   - Open a terminal and navigate to the `scripts` directory.
   - Execute the following command:
     ```bash
     run_backend.bat
     ```
   - This will start the backend server on `http://localhost:8000`.

2. **Run the Mobile App:**
   - Open a separate terminal and navigate to the `scripts` directory.
   - Execute the following command:
     ```bash
     run_mobile.bat
     ```
   - This will start the Metro bundler and launch the app on an Android emulator or connected device.

## Scripts

The `scripts` directory contains several useful scripts:

- `run_backend.bat`: Starts the backend server.
- `run_mobile.bat`: Starts the mobile application.
- `setup.bat`: Sets up the Python environment for the backend.
- `seed_database.py`: Seeds the database with sample data.
- `check_user.py`: A script to check user details.
- `list_users.py`: Lists all users in the database.
- `test_prediction.py`: Tests the expense prediction model.
 
Made by NJ

~MIT License