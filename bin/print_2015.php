<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">

<html>
<head>
<title>search haikupoet.com</title>
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
$search_query =    "SELECT haiku_text, date_written FROM archive_2015 WHERE date_written LIKE '%2015%'";
$result = mysql_query($search_query,$link);
$rows = mysql_num_rows($result);
if ($rows == 0) {
    echo "sorry, this query didn&#8217;t work as expected.";
    }
    $count = 0;
    while ($count < $rows) {
        while($row = mysql_fetch_assoc($result)) {
            echo "{$row['haiku_text']} {$row['date_written']}";
            echo "\n\n";
        }
        $count = $count + 1;
    }

mysql_close($link);

?>
</pre>

</p>
</body>
</html>
