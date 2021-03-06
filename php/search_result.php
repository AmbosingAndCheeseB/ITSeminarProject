﻿<?php
include "dbconfig.php";

$search = $_GET["search"];

$sql1 = 'select * from coolen_board where c_title like "%'.$search.'%"';
$result1 = $db->query($sql1); // coolenjoy db

$sql2 = 'select * from quei_board where q_title like "%'.$search.'%"';
$result2 = $db->query($sql2); // quasarjone db

$sql3 = 'select * from pang_board where p_title like "%'.$search.'%"';
$result3 = $db->query($sql3); // jigupang db

$sql4 = 'select * from seven_board where s_title like "%'.$search.'%"';
$result4 = $db->query($sql4); // assajigu db

$sql5 = 'select * from notice_board';
$result5 = $db->query($sql5);

?>

<!DOCTYPE html><head>
    <meta charset="UTF-8">
    <link rel="stylesheet" href="../css/main.css">
	<link rel="stylesheet" href="../css/searchbox.css">
	<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/font-awesome/4.7.0/css/font-awesome.min.css">
</head>


<div style="text-align: center">
	<div class="caption">환율 계산기</div>
	<a href="index.php">
		<img src="../image/sales_combine.png" style="width: 40%; margin: 100px auto 0px auto">
	</a>
	<iframe class = "money" src="https://ssltools.forexprostools.com/currency-converter/index.php?from=28&to=12&force_lang=18"></iframe>
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
		echo '<a href="';
		echo $notice[2];
		echo '" style="text-decoration:none" target="_blank">
			<div class = "noti">
			<i class="fa fa-exclamation-triangle" style = "color:#734000; margin:10px"></i>';
		echo $notice[1];
		echo '</div>
			</a>';
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
					<img src="../image/coolenlogo.jpg">
					<p>';
						echo $coolen[1];
			echo '	</p>
					<hr>
					<p style = "font-size: 1.0em; text-align : right;">';
						echo $coolen[4];
			echo '	</p>
				<div class = "hide">
					<p>';
						echo iconv_substr($coolen[2],0,60,"utf-8").'..';
			echo ' </p>
				</div>
				
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
					<img src="../image/quasarlogo.jpg">
					<p>';
						echo $quei[1];
			echo '	</p>
					<hr>
					<p style = "font-size: 1.0em; text-align : right;">';
						echo $quei[3];
			echo '	</p>
				<div class = "hide">
					<p>';
						echo iconv_substr($quei[4],0,60,"utf-8").'..';
			echo ' </p>
				</div>
				
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
					<img src="../image/jigulogo.jpg">
					<p>';
						echo $pang[1];
			echo '	</p>
					<hr>
					<p style = "font-size: 1.0em; text-align : right;">';
						echo $pang[3];
			echo '	</p>
				<div class = "hide">
					<p>';
						echo iconv_substr($pang[4],0,60,"utf-8").'..';
			echo ' </p>
				</div>
				
				</div>
				</a>
				';
			}
		echo '</div>';
	
	
			while($seven = $result4->fetch_array()){
			echo '
				<a href="'; echo $seven[2]; echo'" target = "_blank">
				<div class="grid-item">
					<img src="../image/sevenlogo.jpg">
					<p>';
						echo $seven[1];
			echo '	</p>
					<hr>
					<p style = "font-size: 1.0em; text-align : right;">';
						echo $seven[3];
			echo '	</p>
				<div class = "hide">
					<p>';
						echo iconv_substr($seven[4],0,60,"utf-8").'..';
			echo ' </p>
				</div>
				
				</div>
				</a>
				';
			}
		echo '</div>';
		
	?>

		</div>