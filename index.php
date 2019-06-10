<!DOCTYPE html>
<html lang="en">
<head>
  <title>Pinewood House</title>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.4.0/css/bootstrap.min.css">
  <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.4.0/jquery.min.js"></script>
  <script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.4.0/js/bootstrap.min.js"></script>
</head>
<body>

<div class="jumbotron text-center">
  <h1>Pinewood House</h1>
  <p>People who have visited today</p> 
</div>
  
<div class="container">

<?php
$files = scandir("images/" . date('Y-m-d'));

$files = array_reverse($files);

foreach($files as $file){

if (strpos($file, '.jpg') !== false) {
    $without_extension = substr($file, 0, strrpos($file, "."));
    echo "<div class='col-sm-4'>";
    echo "<p>" . str_replace("-",":",$without_extension) . "</p>";
    echo "<img src='/doorbell/images/" . date('Y-m-d') . "/". $file ."' style='width:100%;'>";
    echo "</div>";

}
}

?>

</div>

<br><br><br>

</body>
</html>

</html>
