<?php
  include 'header.php';
?>

  <body>
    <section class="hero">
      <div class="site-description">
        <h2>Grocery shopping with a difference!</h2>
        <p>A webscraper that compares the prices of grocery products.</p>
        <br>
          <form action="search.php" method="POST">
            <input class="tag-about" type="text" name="search" placeholder="rice, oil, ...">
            <button class="tag-about" type="submit" name="submit-search">Search</button> 
          </from>
      </div>
    </section>
  </body>