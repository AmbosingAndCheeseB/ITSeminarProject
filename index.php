<?php
include "dbconfig.php";

$sql1 = 'select * from coolen_board';
$result1 = $db->query($sql1); // coolenjoy db

$sql2 = 'select * from quei_board';
$result2 = $db->query($sql2); // quasarjone db

$sql3 = 'select * from pang_board';
$result3 = $db->query($sql3); // jigupang db

$sql4 = 'select * from seven_board';
$result4 = $db->query($sql4); // sevenjone db

$sql5 = 'select * from notice_board';
$result5 = $db->query($sql5);

?>

<!DOCTYPE html><head>
    <meta charset="UTF-8">
    <link rel="stylesheet" href="main.css">
	<link rel="stylesheet" href="searchbox.css">
	<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/font-awesome/4.7.0/css/font-awesome.min.css">
</head>

<div style="text-align: center">
	<a href="index.php">
		<img src="sales combine.png" style="width: 40%; margin: 100px auto 0px auto">
	</a>
</div>


<div id="searchbox" class="container">
	
	<form method="get" action="search_result.php" class = "Search">	
      <button id="sr" class="Search-label" for="Search-box"><i class="fa fa-search"></i></button>
      <input type="text" name="search" class="Search-box" autocomplete="off">
    </form>
	
</div>

<div class="board">
	
	<?php
	
	while($notice = $result5->fetch_array()){
		echo '<div class = "not">
			<a href="';
		echo $notice[2];
		echo '" style="text-decoration:none" target="_blank">
			<i class="fa fa-exclamation-triangle" style = "color:#734000; margin:10px"></i>';
		echo $notice[1];
		echo '</a>
			</div>';
		}
	
	?>
</div>


<div class="grid">

	<?php
	
		echo '<div class="break">';
		while($coolen = $result1->fetch_array()){
			echo '
				<a href="'; echo $coolen[3]; echo'" target = "_blank">
				<div class="grid-item">
					<img src="coolenlogo.jpg">
					<p>';
						echo $coolen[1];
			echo '	</p>
					<hr>
					<p style = "font-size: 1.0em; text-align : right;">';
						echo $coolen[4];
			echo '	</p>
				</div>
				</a>
				';
			}
		echo '</div>';
	
	
		echo '<div class="break">';
		while($quei = $result2->fetch_array()){
			echo '
				<a href="'; echo $quei[2]; echo'" target = "_blank">
				<div class="grid-item">
					<img src="quasarlogo.jpg">
					<p>';
						echo $quei[1];
			echo '	</p>
					<hr>
					<p style = "font-size: 1.0em; text-align : right;">';
						echo $quei[3];
			echo '	</p>
				</div>
				</a>
				';
			}
		echo '</div>';
	
	
		echo '<div class="break">';
		while($pang = $result3->fetch_array()){
			echo '
				<a href="'; echo $pang[2]; echo'" target = "_blank">
				<div class="grid-item">
					<img src="jigulogo.jpg">
					<p>';
						echo $pang[1];
			echo '	</p>
					<hr>
					<p style = "font-size: 1.0em; text-align : right;">';
						echo $pang[3];
			echo '	</p>
				</div>
				</a>
				';
			}
		echo '</div>';
	
	
			while($seven = $result4->fetch_array()){
			echo '
				<a href="'; echo $seven[2]; echo'" target = "_blank">
				<div class="grid-item">
					<img src="sevenlogo.jpg">
					<p>';
						echo $seven[1];
			echo '	</p>
					<hr>
					<p style = "font-size: 1.0em; text-align : right;">';
						echo $seven[3];
			echo '	</p>
				</div>
				</a>
				';
			}
		
	?>

		</div>