<?php
	header("Pragma: no-cache");   

	header("Cache-Control: no-cache,must-revalidate");   


	header('Content-Type: text/html; charset=utf-8');
	
	$db = new mysqli('106.10.37.140', 'root', 'Tjdduswldnjs12', 'ITProj');

	if($db->connect_error) {

		die('데이터베이스 연결에 문제가 있습니다.\n관리자에게 문의 바랍니다.');

	}



	$db->set_charset('utf8');

?>