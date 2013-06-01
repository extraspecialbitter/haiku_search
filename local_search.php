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
$string = $_POST['keywords'];
$search_query =    "SELECT haiku_text, date_written FROM archive_1999 WHERE haiku_text LIKE '%$string%' UNION
                    SELECT haiku_text, date_written FROM archive_2000 WHERE haiku_text LIKE '%$string%' UNION
                    SELECT haiku_text, date_written FROM archive_2001 WHERE haiku_text LIKE '%$string%' UNION
                    SELECT haiku_text, date_written FROM archive_2002 WHERE haiku_text LIKE '%$string%' UNION
                    SELECT haiku_text, date_written FROM archive_2003 WHERE haiku_text LIKE '%$string%' UNION
                    SELECT haiku_text, date_written FROM archive_2004 WHERE haiku_text LIKE '%$string%' UNION
                    SELECT haiku_text, date_written FROM archive_2005 WHERE haiku_text LIKE '%$string%' UNION
                    SELECT haiku_text, date_written FROM archive_2006 WHERE haiku_text LIKE '%$string%' UNION
                    SELECT haiku_text, date_written FROM archive_2007 WHERE haiku_text LIKE '%$string%' UNION
                    SELECT haiku_text, date_written FROM archive_2008 WHERE haiku_text LIKE '%$string%' UNION
                    SELECT haiku_text, date_written FROM archive_2009 WHERE haiku_text LIKE '%$string%' UNION
                    SELECT haiku_text, date_written FROM archive_2010 WHERE haiku_text LIKE '%$string%' UNION
                    SELECT haiku_text, date_written FROM archive_2011 WHERE haiku_text LIKE '%$string%' UNION
                    SELECT haiku_text, date_written FROM archive_2012 WHERE haiku_text LIKE '%$string%' UNION
                    SELECT haiku_text, date_written FROM archive_2013 WHERE haiku_text LIKE '%$string%'";
$result = mysql_query($search_query,$link);
$rows = mysql_num_rows($result);
if ($rows == 0) {
    echo "sorry, I haven&#8217;t written a haiku about ".$string." yet.";
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
