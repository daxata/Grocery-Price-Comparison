<?php
  include 'header.php';
?>
<!doctype html>
<html lang="en">
  <head>
    <!-- Required meta tags -->
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">

    <!-- Bootstrap CSS -->
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta2/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-BmbxuPwQa2lc/FVzBcNJ7UAyJxM6wuqIj61tLrc4wSX0szH/Ev+nYRRuWlolflfl" crossorigin="anonymous">

    <title>Price Comparison</title>
  </head>
  <body>
    <h1>Search Results</h1>
    <?php
    $conn = mysqli_connect("localhost","root","Ashthalin_7","product_details");
    ?>

    <div class="container py-5">
      <div class="row mt-4">
        <?php
        if(isset($_POST['submit-search'])){
          
          $search_query = mysqli_real_escape_string($conn, $_POST['search']); 
          $result = "SELECT * FROM search WHERE name LIKE '%$search_query%' order by name";
          $query_run = mysqli_query($conn,$result);
          
          // $check_product = ;
          
          if(mysqli_num_rows($query_run)>0){
            while($row=mysqli_fetch_assoc($query_run))
            {
              $url = $row['url'];
              ?>
                <div class="col-md-4">
                  <div class="card">
                    <div class="card-body">
                        <!-- <a href ="<?php echo $row['url'];?>" > -->
                        <img src="<?php echo $row['image']; ?>" style="width:210px;height:250px;"/>
                        <h2 class="card-title"> <?php  echo $row['name'];?></h2>
                        <h3 class="card-title"> <?php  echo $row['price'];?></h3>
                        <?php
                        if(strpos($url,'sastodeal'))
                            echo "<h4 class='card-title'>"."Sastodeal"."</h4>";
                        elseif(strpos($url,'thulo'))
                            echo "<h4 class='card-title'>"."Thulo"."</h4>";
                        else
                            echo("nothing");
                        ?>

                        <a href = "<?php echo $row['url'];?>"> Visit website </a>
                    </div>
                  </div>
                </div>
              <?php
             
            }
          }
  
        else{
            echo '<div class="alert alert-warning alert-dismissible fade show" role="alert"> There are no results matching your search </div>';
          }
        }
        ?>  
      </div>
    </div>

    <script src="https://cdn.jsdelivr.net/npm/@popperjs/core@2.6.0/dist/umd/popper.min.js" integrity="sha384-KsvD1yqQ1/1+IA7gi3P0tyJcT3vR+NdBTt13hSJ2lnve8agRGXTTyNaBYmCR/Nwi" crossorigin="anonymous"></script>
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta2/dist/js/bootstrap.min.js" integrity="sha384-nsg8ua9HAw1y0W1btsyWgBklPnCUAFLuTMS2G72MMONqmOymq585AcH49TLBQObG" crossorigin="anonymous"></script>
  </body>
</html>