<?php
include 'db_config.php';

if ($_SERVER["REQUEST_METHOD"] == "POST" && isset($_FILES["photo"])) {
    $target_dir = "uploads/";
    $target_file = $target_dir . basename($_FILES["photo"]["name"]);
    move_uploaded_file($_FILES["photo"]["tmp_name"], $target_file);

    $sql = "UPDATE items SET photo_path = '$target_file' WHERE id = LAST_INSERT_ID()";
    if ($conn->query($sql) === TRUE) {
        echo "Photo uploaded!";
    } else {
        echo "Error: " . $conn->error;
    }
}
