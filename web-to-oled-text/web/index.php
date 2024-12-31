<?php
$json_file = 'text.json';

// Handle form submission to save the text
if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    $text = $_POST['text'] ?? '';
    $data = ['text' => $text];
    file_put_contents($json_file, json_encode($data, JSON_PRETTY_PRINT));
    echo "Text saved successfully!";
}

// Fetch the text data
if ($_SERVER['REQUEST_METHOD'] === 'GET' && isset($_GET['fetch'])) {
    header('Content-Type: application/json');
    if (file_exists($json_file)) {
        echo file_get_contents($json_file);
    } else {
        echo json_encode(['text' => 'No data found']);
    }
    exit;
}
?>

<!DOCTYPE html>
<html>
<head>
    <title>Save Text</title>
</head>
<body>
    <h1>Enter Text</h1>
    <form action="" method="post">
        <textarea name="text" rows="4" cols="50" maxlength="81"></textarea><br><br>
        <input type="submit" value="Save">
    </form>
</body>
</html>

