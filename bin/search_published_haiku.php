<?php
// Ensure output is interpreted as UTF-8 by the browser
header('Content-Type: text/html; charset=utf-8');

// Database connection settings — match your Python script's credentials
$db_host = "localhost";
$db_user = "root";
$db_pass = "menagerie";
$db_name = "haiku_archive";

// Grab the search term from the POST request
$search_term = isset($_POST['keywords']) ? trim($_POST['keywords']) : '';

if ($search_term === '') {
    echo "Please enter a search term.";
    exit;
}

// Connect to the database
$mysqli = new mysqli($db_host, $db_user, $db_pass, $db_name);

if ($mysqli->connect_errno) {
    echo "Database connection failed: " . htmlspecialchars($mysqli->connect_error);
    exit;
}

// Make sure PHP reads data from MySQL as UTF-8
$mysqli->set_charset("utf-8");

// Use a prepared statement to safely search haiku_text for any partial match
$sql = "SELECT haiku_text, publication_name, year, month, volume, issue
        FROM published_haiku
        WHERE haiku_text LIKE CONCAT('%', ?, '%')
        ORDER BY haiku_index";

$stmt = $mysqli->prepare($sql);
if ($stmt === false) {
    echo "Query preparation failed: " . htmlspecialchars($mysqli->error);
    exit;
}

$stmt->bind_param("s", $search_term);
$stmt->execute();
$stmt->bind_result($haiku_text, $publication_name, $year, $month, $volume, $issue);

$found_any = false;

while ($stmt->fetch()) {
    $found_any = true;
    echo "<p>";
    echo htmlspecialchars($haiku_text) . "<br>";
    echo htmlspecialchars($publication_name) . "<br>";

    // Only show month/year line if both exist
    if (!empty($month) && !empty($year)) {
        echo htmlspecialchars($month) . " " . htmlspecialchars($year) . "<br>";
    }

    echo htmlspecialchars($volume) . " " . htmlspecialchars($issue);
    echo "</p><hr>";
}

if (!$found_any) {
    echo "No haiku found matching \"" . htmlspecialchars($search_term) . "\".";
}

$stmt->close();
$mysqli->close();
?>
