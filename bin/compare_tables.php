<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">

<html>
<head>
<title>compare two haiku archive tables</title>
<meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
<link href="images/styles.css" rel="stylesheet" type="text/css" />
</head>

<BODY BGCOLOR="#000000" TEXT="#888888" LINK="#888888" ALINK="#888888" VLINK="#888888"> 
 
<html xmlns="http://www.w3.org/1999/xhtml" xml:lang="en" lang="en">
<head>
	<meta http-equiv="Content-Type" content="text/html; charset=UTF-8" />
	<title></title>
</head>

<body>

<p>&nbsp;</p>

<h1 align="center"><strong>search results</strong></h1> 
  
<p>&nbsp;</p>

<p>&nbsp;</p>

<p>

<pre>
<?php
$link = mysql_connect('localhost', 'root', 'menagerie');
if (!$link) {
    die('Could not connect: ' . mysql_error());
}
mysql_select_db('haiku_archive')or die("cannot select db");

$search_query = "SELECT * FROM archive_2014 WHERE haiku_text NOT IN (SELECT haiku_text FROM archive_2014_from_html)";

$result = mysql_query($search_query,$link);

$rows = mysql_num_rows($result);
if ($rows == 0) {
    echo "sorry, no match for this query.";
    }
    $count = 0;
    echo "haiku in original archive but not in archive generated from html:";
    echo "\n\n\n";
    while ($count < $rows) {
        while($row = mysql_fetch_assoc($result)) {
            echo "{$row['haiku_text']} {$row['date_written']}";
            echo "\n";
        }
        $count = $count + 1;
    }

$search_query = "SELECT * FROM archive_2014_from_html WHERE haiku_text NOT IN (SELECT haiku_text FROM archive_2014)";

$result = mysql_query($search_query,$link);

$rows = mysql_num_rows($result);
if ($rows == 0) {
    echo "sorry, no match for this query.";
    }
    $count = 0;
    echo "\n";
    echo "haiku in archive generated from html but not in original:";
    echo "\n\n\n";
    while ($count < $rows) {
        while($row = mysql_fetch_assoc($result)) {
            echo "{$row['haiku_text']} {$row['date_written']}";
            echo "\n";
        }
        $count = $count + 1;
    }
mysql_close($link);

?>
</pre>

</p>
</body>
</html>
