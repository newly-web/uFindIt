<?php
// Database connection
include '../backend/db_config.php';

if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    $name = $_POST['name'];  // Assuming 'name' includes both first and last name
    $school_id = $_POST['school_id'];
    $email = $_POST['email'];
    $password = $_POST['password'];

    // Secure password hashing
    $password_hashed = password_hash($password, PASSWORD_BCRYPT);

    // Validation for school_id
    if (!preg_match('/^\d{9}$/', $school_id)) {
        echo "School ID must be a 9-digit number!";
        exit();
    }

    // Validation for email domain
    if (!preg_match('/@uottawa.ca$/', $email)) {
        echo "Email must be a valid uOttawa domain!";
        exit();
    }

    // Check if school_id already exists in users table
    $checkSchool = $conn->prepare("SELECT id FROM users WHERE school_id = ?");
    if ($checkSchool === false) {
        die('Prepare failed: ' . $conn->error);
    }
    $checkSchool->bind_param('i', $school_id);
    $checkSchool->execute();
    $schoolResult = $checkSchool->get_result();

    if ($schoolResult->num_rows > 0) {
        echo "User with this school_id is already registered!";
    } else {
        // Insert new user into database
        $stmt = $conn->prepare("INSERT INTO users (name, school_id, email, password) VALUES (?, ?, ?, ?)");
        if ($stmt === false) {
            die('Prepare failed: ' . $conn->error);
        }
        $stmt->bind_param('siss', $name, $school_id, $email, $password_hashed);

        if ($stmt->execute()) {
            echo "User registered successfully!";
        } else {
            echo "Error: " . $stmt->error;
        }
    }

} else {
    echo "Invalid request method!";
}
