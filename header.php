<?php
  include 'dbh.php';
?>
<!DOCTYPE html>
  <head>
    <meta charset="utf-8">
    <title>Price Comparison Website</title>
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">
<!-- 
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta2/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-BmbxuPwQa2lc/FVzBcNJ7UAyJxM6wuqIj61tLrc4wSX0szH/Ev+nYRRuWlolflfl" crossorigin="anonymous">
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta2/dist/js/bootstrap.bundle.min.js" integrity="sha384-b5kHyXgcpbZJO/tY9Ul7kGkf1S0CWuKcCD38l8YkeH8z8QjE0GmW1gYU5S9FOnJ0" crossorigin="anonymous"></script> -->
    <link rel="stylesheet" href="index.css">
    </head>
    <body>
    <nav class="navbar  bg-dark">
      <div class="nav nav-tabs" id="nav-tab" role="tablist">
        <a class="nav-item nav-link" id="nav-home-tab" data-toggle="tab" href="index.php" role="tab" aria-controls="nav-home">Home</a>
        <div class="dropdown">
        <a class="nav-item nav-link" id="nav-profile-tab" data-toggle="tab" href="categories.php" role="tab" aria-controls="nav-profile" >Categories</a>
          <div class="dropdown-content">
            <a href="rice.php">Rice</a>
            <a href="lentil.php">Lentils</a>
            <a href="oil.php">Oil</a>
            <a href="spice.php">Spices</a>
            <a href="snacks.php">Snacks</a>
          </div>
        </div>
      </div>
    </nav>
    <!-- <div class="menu-bar">
      <ul>
        <li class="active"><a href="index.php" class="tag-products-base">Homepage</a></li>
        <li class="active"><a href="categories.php" class="tag-categories-base">Categories</a></li>
        <li> 
      </ul> -->
    </div>
  </body>
</html>
  </div>
</nav>
