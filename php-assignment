<?php
// This program lets the user search for a country.  It then provides
// a list of countries that match the search term, allowing the user
// to select one.  For the selected country, the program displays a list
// of mountains
//
// written by cae
// modified by jmh (Jacob Hall)
?>

<html>
<head>
<meta charset="utf-8" />
<title>Country List</title>
</head>
<body>

<?php
require '~/include/db-connect-mondial.php';

// this function displays the base web page listing all the countries
function displayCountries($mondial, $searchStr)
{
    $searchStr = $mondial->real_escape_string($searchStr);
    $likeStr = $searchStr.'%';

    $searchQueryStr = "SELECT code, name, capital FROM country
    WHERE name = ? or code = ?
    or name LIKE ? or code LIKE ?
    or name SOUNDS LIKE ?
    ORDER BY name ";

    if($searchQuery=$mondial->prepare($searchQueryStr))
    {
        $searchQuery->bind_param("sssss", $searchStr, $searchStr, $likeStr, $likeStr, $searchStr);
        $searchQuery->execute();
        $searchQuery->store_result();
        $searchQuery->bind_result($countryCode, $countryName, $countryCapital);
        ?>

        <table style="text-align:left">
        <tr><th>Country</th><th>Capital</th></tr>
        <?php
        while( $searchQuery->fetch())
        {
        ?>
            <tr>
            <td><a href="<?php print( $_SERVER['PHP_SELF'].'?countryCode='.urlencode($countryCode)) ?>" >
            <?php print($countryName);?></a></td>
            <td><?php print($countryCapital);?></td>
            </tr>

        <?php
        }
        ?>
        </table>

    <?php
    }
    else
    {
        print('Unable to perform query');
    }

}
?>

<!-- MODIFIED Version of Func -->
<?php
  function displayOceans($mondial)
  {
      $countryCode = $_GET["countryCode"];
      $countryCode = $mondial->real_escape_string($countryCode);

      $countryQueryStr = "SELECT name FROM country WHERE code = ?";
      if( $countryQuery = $mondial->prepare($countryQueryStr))
      {
          $countryQuery->bind_param("s", $countryCode);
          $countryQuery->execute();
          $countryQuery->store_result();
          $countryQuery->bind_result( $countryName);
          $countryQuery->fetch();
      }
      else
      {
          die("some horrible error occurred");
      }
  ?>
      <h2>Mountains in <?php print($countryName);?></h2>

  <?php
      $oceanQueryStr="SELECT sea FROM ocean WHERE country = ? ORDER by sea";
      if( $oceanQuery = $mondial->prepare($oceanQueryStr))
      {
          $oceanQuery->bind_param("s", $countryCode);
          $oceanQuery->execute();
          $oceanQuery->store_result();
          $oceanQuery->bind_result($oceanName);
      }
      else
      {
          die("another horrible death");
      }
      if($oceanQuery->num_rows > 0 )
      {
          while( $oceanQuery->fetch() )
          {
              printf("%s</br>",$oceanName);
          }
      }
      else
      {
          print("No oceans listed.");
      }
  }

?>



<?php
// this function displays the mountains for the selected country
function displayMountains($mondial)
{
    $countryCode = $_GET["countryCode"];
    $countryCode = $mondial->real_escape_string($countryCode);

    $countryQueryStr = "SELECT name FROM country WHERE code = ?";
    if( $countryQuery = $mondial->prepare($countryQueryStr))
    {
        $countryQuery->bind_param("s", $countryCode);
        $countryQuery->execute();
        $countryQuery->store_result();
        $countryQuery->bind_result( $countryName);
        $countryQuery->fetch();
    }
    else
    {
        die("some horrible error occurred");
    }
?>
    <h2>Mountains in <?php print($countryName);?></h2>

<?php
    $oceanQueryStr="SELECT mountain FROM geo_mountain WHERE country = ? ORDER by mountain";
    if( $oceanQuery = $mondial->prepare($oceanQueryStr))
    {
        $oceanQuery->bind_param("s", $countryCode);
        $oceanQuery->execute();
        $oceanQuery->store_result();
        $oceanQuery->bind_result($mountainName);
    }
    else
    {
        die("another horrible death");
    }
    if($oceanQuery->num_rows > 0 )
    {
        while( $oceanQuery->fetch() )
        {
            printf("%s</br>",$mountainName);
        }
    }
    else
    {
        print("No mountains listed.");
    }
}
?>

<?php
function displaySearchPage($mondial)
{
?>
    <h2>Search for a Country</h2>
    <form action="<?php print( $_SERVER['PHP_SELF']) ?>", method="post" >
    <input type="text" name="searchStr">
    <input type="submit" value="Submit">
    </form>
<?php
}
?>

<?php
// main program

// if search value present show the selected countries
if(!empty( $_POST["searchStr"] ))
{
    displayCountries($mondial, $_POST["searchStr"]);
}
// searchTerm missing but countryCode present so show mountain details
elseif( !empty( $_GET["countryCode"] ))
{
    displayMountains($mondial, $_GET["countryCode"]);
}
// no searchTerm or countryCode so show main search page
else
{
    displaySearchPage($mondial);
}


?>
</body>
</html>
