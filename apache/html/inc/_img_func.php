<?php

 if(eregi('.gif', $_POST[$pimage_fld])) {

	$pathtofile = $target_path;

	$sourceImage = imagecreatefromgif($pathtofile);
	$sourceWidth = imagesx($sourceImage);
	$sourceHeight = imagesy($sourceImage);

	if($sourceWidth > 450)
	{
		$imgratio = $sourceWidth/$sourceHeight;
		$newWidth = '450';
		$newHeight = $newWidth/$imgratio;
	}

	if($sourceWidth < 451)
	{
		$newHeight = $sourceHeight;
		$newWidth = $sourceWidth;
	}

	$targetImage = imagecreate($newWidth, $newHeight);

	imagecopyresized($targetImage,$sourceImage,0,0,0,0,$newWidth,$newHeight,imagesx($sourceImage),imagesy($sourceImage));

	imagegif($targetImage, $pathtofile);

	} //end gif if

 if(eregi('.jpg', $_POST[$pimage_fld])) {

	$pathtofile = $target_path;

	$sourceImage = imagecreatefromjpeg($pathtofile);
	$sourceWidth = imagesx($sourceImage);
	$sourceHeight = imagesy($sourceImage);

	if($sourceWidth > 450)
	{
		$imgratio = $sourceWidth/$sourceHeight;
		$newWidth = 450;
		$newHeight = $newWidth/$imgratio;
	}

	if($sourceWidth < 451)
	{
		$newHeight = $sourceHeight;
		$newWidth = $sourceWidth;
	}

	$targetImage = imagecreatetruecolor($newWidth, $newHeight);

	imagecopyresampled($targetImage,$sourceImage,0,0,0,0,$newWidth,$newHeight,imagesx($sourceImage),imagesy($sourceImage));

	imagejpeg($targetImage, $pathtofile);

	} //end jpg if

?> 