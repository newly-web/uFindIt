<!doctype html>
<html lang="en">

<head>
    <meta charset="UTF-8" />
    <link rel="icon" type="image/svg+xml" href="/vite.svg" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>Report Lost Item</title>
</head>

<body>
    <form id="lostItemForm" method="POST" action="../backend/lost_item_handler.php" enctype="multipart/form-data">


        <input type="text" name="title" placeholder="Item Title" required />
        <textarea name="description" placeholder="Item Description"></textarea>
        <input type="file" name="photo" accept="image/*" required />
        <button type="submit" name="reportLost">Report Lost Item</button>
        <select name="category_id" required>
            <option value="">Select a category</option>
            <?php
            // Include database connection
            include '../backend/db_config.php';

            // Fetch categories from the database
            $result = $conn->query("SELECT id, name FROM categories");
            if ($result) {
                while ($row = $result->fetch_assoc()) {
                    echo "<option value='" . $row['id'] . "'>" . $row['name'] . "</option>";
                }
            } else {
                echo "<option value=''>No categories available</option>";
            }
            ?>
        </select>

    </form>

</body>

</html>