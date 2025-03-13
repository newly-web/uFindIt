<?php
// Correcting the URL parsing
$url = 'mysql://sd71uc4xbtds69l9:jeigr7149b4s4ldm@arfo8ynm6olw6vpn.cbetxkdyhwsb.us-east-1.rds.amazonaws.com:3306/h7ehdbu4aune32sp';
$dbparts = parse_url($url);

// Extract parts
$hostname = $dbparts['host'];
$username = $dbparts['user'];
$password = $dbparts['pass'];
$database = ltrim($dbparts['path'], '/');

// Create connection
$conn = new mysqli($hostname, $username, $password, $database);

// Check connection
if ($conn->connect_error) {
    die("Connection failed: " . $conn->connect_error);
}
echo "Connection was successfully established!";
