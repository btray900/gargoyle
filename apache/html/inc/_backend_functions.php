<?php
	require_once('_backend_constants.php');

	function prn_pin_only($id, $pin)
	{
		echo "<a ONCLICK=\"javascript:openFull('".UPDATE_PATH."&id=".$id."');\"><u style=\"color: blue;\">".$pin."</u></a>";
	}

	function prn_pin($id, $pin, $name)
	{
		echo "<a ONCLICK=\"javascript:openFull('".UPDATE_PATH."&id=".$id."');\"><u style=\"color: blue;\">".$pin."</u></a> - ".$name."</a></td>";
	}

	function mk_date_val($fld, $tmonth, $tday, $tyear, $field_name, $dtxt, $curval)
	{
		$parts = explode('/', $curval);
		$curmonth = $parts[0];
		$curday = $parts[1];
		$curyear = $parts[2];
?>
	<p><div class=tblfield><?php echo $fld; ?></div>
	<div class=tblvalue>
	<select name=<?php echo $tmonth; ?> id=<?php echo $tmonth; ?> onchange="put_dval_<?php echo $dtxt; ?>();">
		<option value="">Month</option>
		<option value="01"<?php if($curmonth == '01') { echo " SELECTED"; } ?>>01 - Jan</option>
		<option value="02"<?php if($curmonth == '02') { echo " SELECTED"; } ?>>02 - Feb</option>
		<option value="03"<?php if($curmonth == '03') { echo " SELECTED"; } ?>>03 - Mar</option>
		<option value="04"<?php if($curmonth == '04') { echo " SELECTED"; } ?>>04 - Apr</option>
		<option value="05"<?php if($curmonth == '05') { echo " SELECTED"; } ?>>05 - May</option>
		<option value="06"<?php if($curmonth == '06') { echo " SELECTED"; } ?>>06 - Jun</option>
		<option value="07"<?php if($curmonth == '07') { echo " SELECTED"; } ?>>07 - Jul</option>
		<option value="08"<?php if($curmonth == '08') { echo " SELECTED"; } ?>>08 - Aug</option>
		<option value="09"<?php if($curmonth == '09') { echo " SELECTED"; } ?>>09 - Sep</option>
		<option value="10"<?php if($curmonth == '10') { echo " SELECTED"; } ?>>10 - Oct</option>
		<option value="11"<?php if($curmonth == '11') { echo " SELECTED"; } ?>>11 - Nov</option>
		<option value="12"<?php if($curmonth == '12') { echo " SELECTED"; } ?>>12 - Dec</option>
	</select>

	<select name=<?php echo $tday; ?> id=<?php echo $tday; ?> onchange="put_dval_<?php echo $dtxt; ?>();">
		<option value="">Day</option>

<?php
		$maxdays = 31;

		for($i = 1; $i <= $maxdays; $i++ )
		{
			if(strlen($i) == 1)
			{
				$i = "0".$i;
			}
?>
		<option value="<?php echo $i; ?>" <?php if ($curday == $i) { echo "SELECTED"; } ?>><?php echo $i; ?></option>

<?php
		} // end for
?>
	</select>


	<select name=<?php echo $tyear; ?> id=<?php echo $tyear; ?> onchange="put_dval_<?php echo $dtxt; ?>();">
		<option value="">Year</option>

<?php
		$maxyears = 2025;

		for($j = 1950; $j <= $maxyears; $j++)
		{
?>
	<option value="<?php echo $j; ?>" <?php if ($curyear == $j) { echo "SELECTED"; } ?>><?php echo $j; ?></option>

<?php
		} // end for
?>
	</select>

	<input type=hidden id=<?php echo $field_name; ?> name=<?php echo $field_name; ?> <?php if($curval != '') { echo "value=\"".$curval."\""; } ?> />
	<span id=<?php echo $dtxt; ?>></span>
	</div>

<script type="text/javascript">
		function put_dval_<?php echo $dtxt; ?>()
		{
			var mmonth = document.getElementById("<?php echo $tmonth; ?>");
			var nmonth = mmonth.options[mmonth.selectedIndex].value;

			var mday = document.getElementById("<?php echo $tday; ?>");
			var nday = mday.options[mday.selectedIndex].value;

			var myear = document.getElementById("<?php echo $tyear; ?>");
			var nyear = myear.options[myear.selectedIndex].value;

			var vdate = nmonth + "/" + nday + "/" + nyear;

			document.getElementById("<?php echo $field_name; ?>").value = vdate;
			document.getElementById("<?php echo $dtxt; ?>").innerHTML = vdate;
		}
</script>

<?php

	}


	function spacer($colspan)
	{
		if($colspan <= 1)
		{
		 	echo "<tr><td>&nbsp; </td></tr>";
		}
		else
		{
		 	echo "<tr><td colspan=".$colspan.">&nbsp; </td></tr>";
		}
	}

	function mk_month_dd($select_name, $var)
	{
?>

<select name="<?php echo $select_name; ?>">
 <option value="01" <?php if ($var == '01') { echo "SELECTED"; } ?>>January</option>
 <option value="02" <?php if ($var == '02') { echo "SELECTED"; } ?>>February</option>
 <option value="03" <?php if ($var == '03') { echo "SELECTED"; } ?>>March</option>
 <option value="04" <?php if ($var == '04') { echo "SELECTED"; } ?>>April</option>
 <option value="05" <?php if ($var == '05') { echo "SELECTED"; } ?>>May</option>
 <option value="06" <?php if ($var == '06') { echo "SELECTED"; } ?>>June</option>
 <option value="07" <?php if ($var == '07') { echo "SELECTED"; } ?>>July</option>
 <option value="08" <?php if ($var == '08') { echo "SELECTED"; } ?>>August</option>
 <option value="09" <?php if ($var == '09') { echo "SELECTED"; } ?>>September</option>
 <option value="10" <?php if ($var == '10') { echo "SELECTED"; } ?>>October</option>
 <option value="11" <?php if ($var == '11') { echo "SELECTED"; } ?>>November</option>
 <option value="12" <?php if ($var == '12') { echo "SELECTED"; } ?>>December</option>
</select>

<?php
	}

/////////////////////////////////////////////////////////////////////////////////
	function frm_kdd($fld, $oparray, $selname, $getvar)
	{
		echo "<p><div class=tblfield>".$fld.":</div>";
		echo "<div class=tblvalue>";
		echo "<select name=".$selname.">";

		foreach($oparray as $sid => $val)
		{
			echo "<option value=".$sid;

			if($sid == $getvar)
			{
				echo " SELECTED";
			}

			echo ">".$val."</option>"."\r\n";
		}

		echo "</select></div>";
	}

	function kiss_dd($oparray, $selname, $getvar)
	{
		echo "<select name=".$selname.">";

		foreach($oparray as $sid => $val)
		{
			echo "<option value=".$sid;

			if($sid == $getvar)
			{
				echo " SELECTED";
			}

			echo ">".$val."</option>"."\r\n";
		}

		echo "</select>";
	}

	function mk_dd($classvar, $name_field, $id_field, $where)
	{
		$a = new $classvar;

		$b = $a->load_all($where." ORDER BY $name_field ASC");

		echo "<p><b>Select ".$classvar."</b>";

		echo "<br><select name=".$id_field.">";

		foreach($b as $row)
		{
			echo "<option value=".$row[$id_field];

			if($row[$id_field] == $_GET[$id_field])
			{
				echo " SELECTED";
			}

			echo ">".$row[$name_field]."</option>"."\r\n";
		}

		echo "</select>";
	}

	function frm_dd($getclass, $id_field, $name_field, $sel_name, $classvar, $where)
	{
		$x = new $getclass;

		if(preg_match('/ORDER/i', $where))
		{
				$xs = $x->load_all($where);
		}else{
				$xs = $x->load_all($where." ORDER BY ".$name_field[0]."");
		}

		echo "<p><div class=tblfield>".$getclass." <a name=".$name_field.">&nbsp;</a></div>";

		echo "<div class=tblvalue><select name=".$sel_name.">";

		echo "<option>Select ".$getclass."</option>";

		foreach($xs as $row)
		{
			echo "<option value=".$row[$id_field];

			if($row[$id_field] == $classvar->data_array[0][$sel_name])
			{
				echo " SELECTED";
			}

			echo ">";

			foreach($name_field as $nf)
			{
				if($nf == 'CLDAY')
				{
					$cl = new tClass;
					echo $cl->dow_str($row[$nf])." ";
				}
				else
				{
					echo $row[$nf]." ";
				}
			}

			//echo " - ".$row[$id_field];

			echo "</option>"."\r\n";
		}

		echo "</select></div>";
	}

	function frm_heading($anchor)
	{
		echo "<p><b style=\"width: 100%; font-size: 1.2em;\">".ucwords($anchor)."<a name=".str_replace(' ', '_', $anchor).">&nbsp;</a></b>";
	}


        function prn_frm_end()
        {
           echo "<br><br><span=\"width: 100%; text-align: right;\"><input type=submit value=update /></form>";
        }

	function prn_frm_top()
	{
           if($_GET['cmd'] != 'add') {
?>

<form enctype="multipart/form-data" action="<?php echo $_SERVER[PHP_SELF]; ?>?cat=<?php echo $_GET[cat]; ?>&cmd=<?php echo $_GET[cmd]; ?>&id=<?php echo $_GET[id]; ?>" method="post">
<input type="hidden" name="frmvalue" value="<?php echo $_GET[cmd]; ?>">
<input type="hidden" name="id" value="<?php echo $_GET[id]; ?>">


<?php
          }

           if($_GET['cmd'] == 'add') {

?>

<form enctype="multipart/form-data" action="<?php echo $_SERVER[PHP_SELF]; ?>?cat=<?php echo $_GET[cat]; ?>&cmd=<?php echo $_GET[cmd]; ?>" method="post">
<input type="hidden" name="frmvalue" value="<?php echo $_GET[cmd]; ?>">


<?php
           }


	}

	function frm_txt_def($classvar, $label, $name, $size, $def_val)
	{
		if($_GET['cmd'] != 'add')
		{
			echo "<p><div class=tblfield>".$label." <a name=".$name.">&nbsp;</a></div>";
			echo "<div class=tblvalue><input type=text name=$name size=$size value=\"".$classvar->data_array[0][$name]."\" /></div>"."\r\n";
		}

		if($_GET['cmd'] == 'add')
		{
			echo "<p><div class=tblfield>".$label." <a name=".$name.">&nbsp;</a></div>";
			echo "<div class=tblvalue><input type=text name=$name size=$size value=\"".$def_val."\" /></div>"."\r\n";
		}

		return;
	}

	function frm_txt($classvar, $label, $name, $size)
	{
		echo "<br><div class=tblfield>".$label." <a name=".$name.">&nbsp;</a></div>";
		echo "<div class=tblvalue><input type=text name=$name size=$size value=\"".htmlentities($classvar->data_array[0][$name])."\" /></div>"."\r\n";
		return;
	}

	function frm_txta($classvar, $label, $name, $cols, $rows)
	{
		echo "<br><div class=tblfield>".$label." <a name=".$name.">&nbsp;</a></div>";
		echo "<div class=tblvalue><textarea name=$name cols=$cols rows=$rows>".$classvar->data_array[0][$name]."</textarea></div>"."\r\n";
		return;
	}

	function prn_imagefld($classvar, $image_fld)
	{
		if($classvar->data_array[0][$image_fld] == '' || $_GET['pic'])
		{
?>

<p>
<div class="tblfield">File:</div>
<div class="tblvalue"><input type=file name="uploadedfile" size=60 value="<?php echo $classvar->data_array[0][$image_fld]; ?>" /></div>

<?php
		}

		if($classvar->data_array[0][$image_fld] != '')
		{
?>

<p>
<div class="tblfield">Current File:</div>
<div class="tblvalue"><input type=hidden name="<?php echo $image_fld; ?>" value="<?php echo $classvar->data_array[0][$image_fld]; ?>" />
<img src=../img/<?php echo $classvar->data_array[0][$image_fld]; ?> width=150 />

<?php
		}

		if(!$_GET['pic'])
		{
?>

 | <a href=<?php echo $_SERVER[PHP_SELF]; ?>?cat=<?php echo $_GET[cat]; ?>&cmd=<?php echo $_GET[cmd]; ?>&id=<?php echo $_GET[id]; ?>&pic=true>Update file</a>

<?php
		}

	}

	function prn_dbdata($cat, $classvar, $classname, $num_sort, $other_sort, $order, $shfields, $display)
	{
		global $row_nums, $gen;

		$classvar = new $classname;

//		if(isset($_GET['cmd']) && $_GET['cmd'] != 'add' && $_POST['frmvalue'] != 'update' && !isset($_GET['id']))
		if(isset($_GET['cmd']) && $_GET['cmd'] != 'add' && !isset($_POST['frmvalue']) && !isset($_GET['id']))
		{
			echo "<div id=left>";
			echo "<p><b>Click to update</b>";
			echo "<table>";

			if(!isset($_GET['orderby']))
			{
				if($display == 'Num')
				{
					if(isset($_GET['field']) && $_GET['field'] == 'numbers' || !isset($_GET['field'])){ $classvar->dsp_link("ORDER BY $num_sort $order", $num_sort, $shfields); }
					if(isset($_GET['field']) && $_GET['field'] == 'words') { $classvar->dsp_link("ORDER BY $other_sort $order", $num_sort, $shfields); }
				}

				if($display == 'Word')
				{
					if($_GET['field'] == 'numbers'){ $classvar->dsp_link("ORDER BY $num_sort $order", $num_sort, $shfields); }
					if($_GET['field'] == 'words' || !$_GET['field']) { $classvar->dsp_link("ORDER BY $other_sort $order", $num_sort, $shfields); }
				}
			}

			if(isset($_GET['orderby']))
			{
				$classvar->dsp_link("ORDER BY ".$_GET['orderby']." ".$_GET['way'], $num_sort, $shfields);
			}

			echo "</table>";
			echo "<p>[$row_nums] ".str_replace('_', ' ', $cat);
			echo "</div>";
		}

		if(isset($_GET['cmd']) && $_GET['cmd'] == 'add')
		{
			require_once('inc/_'.$cat.'_form.php');
		}

		if(isset($_GET['id']))
		{
			$classvar->load_all("WHERE $num_sort = $_GET[id]");

			require_once('inc/_'.$cat.'_form.php');
		}
	}
?>
