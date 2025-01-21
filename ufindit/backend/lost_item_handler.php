<?php
// Database connection
include 'db_config.php';

if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    $category_id = $_POST['category_id'];
    $title = $_POST['title'];
    $description = $_POST['description'];

    // Handle file upload
    $photo = $_FILES['photo'];
    $target_dir = "../uploads/";
    $target_file = $target_dir . basename($photo["name"]);
    move_uploaded_file($photo["tmp_name"], $target_file);

    // Insert lost item into database
    $stmt = $conn->prepare("INSERT INTO items (category_id, title, description, photo_path) VALUES (?, ?, ?, ?)");
    $stmt->bind_param('isss', $category_id, $title, $description, $target_file);
    $stmt->execute();

    echo "Lost item reported successfully!";
}
