<?php
$servername = "localhost";
$username = "root"; // the MySQL username
$password = ""; // the MySQL password
$dbname = "ufindit";

$conn = new mysqli($servername, $username, $password, $dbname);

if ($conn->connect_error) {
    die("Connection failed: " . $conn->connect_error);
}
echo "Connected successfully";

?>
