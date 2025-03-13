<?php
include 'db_config.php';

if ($_SERVER["REQUEST_METHOD"] == "POST") {
    $title = $_POST["title"];
    $description = $_POST["description"];
    $location = $_POST["location"];
    $user_id = $_SESSION["user_id"]; // Assume the user is logged in.

    $sql = "INSERT INTO items (title, description, location, user_id) VALUES ('$title', '$description', '$location', '$user_id')";

    if ($conn->query($sql) === TRUE) {
        echo "New lost item added!";
    } else {
        echo "Error: " . $sql . "<br>" . $conn->error;
    }
}
