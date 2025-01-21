<!doctype html>
<html lang="en">

<head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>Login</title>
</head>
<?php
error_reporting(E_ALL);
ini_set('display_errors', 1);
?>
<body>
    <form id="loginForm" method="POST" action="../backend/login.php">
        <input type="email" name="email" placeholder="Email" required />
        <input type="password" name="password" placeholder="Password" required />
        <button type="submit" name="login">Log In</button>
    </form>

    <script type="module" src="/src/main.js"></script>
</body>

</html>