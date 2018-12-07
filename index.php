<?php
include "dbconfig.php";

$sql1 = 'select * from coolen_board';
$result1 = $db->query($sql1); // coolenjoy db
?>

<!DOCTYPE html><head>
    <meta charset="UTF-8">
    <link rel="stylesheet" href="main.css">
</head>



<div class="grid">
	
	<?php
		while($coolen = $result1->fetch_array()){
		echo '
			<div class="grid-item">
				<img src="coolenlogo.jpg">
				<p>';
					echo $coolen[1];
		echo '	</p>
			</div>
			';
		}
	?>

			<div class="grid-item">
				<img src="assalogo.jpg">
				<p>
					양지몬 움뫄쟁이
				</p>
			</div>

			<div class="grid-item">
				<img src="jigulogo.jpg">
				<p>
					양지몬 움뫄쟁이
				</p>
			</div>

			<div class="grid-item">
				<img src="quasarlogo.jpg">
				<p>
					양지몬 움뫄쟁이
				</p>
			</div>

			<div class="grid-item">
				<img src="jigulogo.jpg">
				<p>
					양지몬 움뫄쟁이
				</p>
			</div>

			<div class="grid-item">
				<img src="assalogo.jpg">
				<p>
					양지몬 움뫄쟁이
				</p>
			</div>

			<div class="grid-item">
				<img src="coolenlogo.jpg">
				<p>
					양지몬 움뫄쟁이
				</p>
			</div>

  			<div class="grid-item">
				<img src="quasarlogo.jpg">
				<p>
					 양지몬 움뫄쟁이
				</p>
			</div>

			<div class="grid-item">
				<img src="jigulogo.jpg">
				<p>
					양지몬 움뫄쟁이
				</p>
			</div>

			<div class="grid-item">
				<img src="assalogo.jpg">
				<p>
					양지몬 움뫄쟁이
				</p>
			</div>
	
		</div>