<?php
include "dbconfig.php";

$search = $_GET["search"];

$sql1 = 'select * from coolen_board where c_title like "%'.$search.'%"';
$result1 = $db->query($sql1); // coolenjoy db

$sql2 = 'select * from quei_board where q_title like "%'.$search.'%"';
$result2 = $db->query($sql2); // quasarjone db

//$sql3 = 'select * from assa_board';
//$result3 = $db->query($sql3); // assajigu db

//$sql4 = 'select * from jigu_board';
//$result4 = $db->query($sql4); // jigupang db

?>

<!DOCTYPE html><head>
    <meta charset="UTF-8">
    <link rel="stylesheet" href="main.css">
	<link rel="stylesheet" href="searchbox.css">
	<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/font-awesome/4.7.0/css/font-awesome.min.css">
</head>



<div id="searchbox" class="container">
	
	<form method="get" action="search_result.php" class = "Search">	
      <button id="sr" class="Search-label" for="Search-box"><i class="fa fa-search"></i></button>
      <input type="text" name="search" class="Search-box" autocomplete="off">
    </form>
	
</div>

<div class="grid">
	
	<?php
	
		while($coolen = $result1->fetch_array()){
		echo '
			<a href="'; echo $coolen[2]; echo'" target = "_blank">
			<div class="grid-item">
				<img src="coolenlogo.jpg">
				<p>';
					echo $coolen[1];
		echo '	</p>
			</div>
			</a>
			';
		}

		while($quei = $result2->fetch_array()){
		echo '
			<a href="'; echo $quei[2]; echo'" target = "_blank">
			<div class="grid-item">
				<img src="quasarlogo.jpg">
				<p>';
					echo $quei[1];
		echo '	</p>
			</div>
			';
		}
	
/*		while($assa = $result3->fetch_array()){
		echo '
			<a href="'; echo $assa[2]; echo'" target = "_blank">
			<div class="grid-item">
				<img src="assalogo.jpg">
				<p>';
					echo $assa[1];
		echo '	</p>
			</div>
			';
		}
	
		while($jigu = $result4->fetch_array()){
		echo '
			<a href="'; echo $jigu[2]; echo'" target = "_blank">
			<div class="grid-item">
				<img src="jigulogo.jpg">
				<p>';
					echo $jigu[1];
		echo '	</p>
			</div>
			';
		}
*/	
	?>

		</div>