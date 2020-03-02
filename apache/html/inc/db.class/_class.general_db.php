<?php
        class Gen
        {
                var $table_name;
                var $tbl_pfx;
                var $data_array;
                var $fieldlist;

                function dsp_link($where, $num_sort, $shfields)
                {
                        $rowdata = $this->load_all($where);

                        $i = 0;

                        echo "<th><a href=".$_SERVER['PHP_SELF']."?cat=".$_GET['cat']."&cmd=".$_GET['cmd']."&way=asc&orderby=id>/\ </a>".$num_sort;
                        echo "<a href=".$_SERVER['PHP_SELF']."?cat=".$_GET['cat']."&cmd=".$_GET['cmd']."&way=desc&orderby=id> \/</a></th>";

//                        echo "<tr><th>".$num_sort."</th>";

                        foreach($shfields as $sval => $fld_val)
                        {
                                echo "<th><a href=".$_SERVER['PHP_SELF']."?cat=".$_GET['cat']."&cmd=".$_GET['cmd']."&way=asc&orderby=".$fld_val.">/\ </a>".$fld_val;
                                echo "<a href=".$_SERVER['PHP_SELF']."?cat=".$_GET['cat']."&cmd=".$_GET['cmd']."&way=desc&orderby=".$fld_val."> \/</a></th>";
                        }

                        echo "</tr>";

                        foreach($rowdata as $row)
                        {
                                if($i == '0') { $sty = '#ffffff'; } else { $sty = '#ffffcc'; }

                                echo "<tr bgcolor=".$sty."><td valign=top><a href=".$_SERVER['PHP_SELF']."?cat=".$_GET['cat']."&cmd=".$_GET['cmd']."&id=";
                                echo $row[$num_sort].">".$row[$num_sort]."</a></td> ";

                                foreach($shfields as $val)
                                {
                                        echo "<td valign=top>";
                                        echo htmlentities($row[$val]);

                                        echo "</td>";
                                }

                                $i++;

                                if($i > 1) { $i = 0; }

                                echo "</tr>";

                        }
                }

                function load_all($where)
                {
                        global $row_nums, $dbconn;

                        if(empty($where))
                        {
                                $where_str = NULL;
                        }
                        else
                        {
                                $where_str = $where;
                        }

                        $q = "SELECT * FROM $this->table_name $where_str";
//echo "<br>".$q;
                        $res = mysqli_query($dbconn, $q) or die('load_all: '.mysqli_error($dbconn));

                        while($row = mysqli_fetch_assoc($res))
                        {
                                $this->data_array[] = $row;
                                $row_nums++;
                        }

                                return $this->data_array;

                } // end load_all

                function load_some($fields, $where)
                {
                        global $dbconn;

                        if(empty($where))
                        {
                                $where_str = NULL;
                        }
                        else
                        {
                                $where_str = $where;
                        }

                        $q = "SELECT $fields FROM $this->table_name $where_str";
//echo $q;
                        $res = mysqli_query($dbconn, $q) or die('load_some: '.mysqli_error($dbconn));

                        while($row = mysqli_fetch_assoc($res))
                        {
                                $this->data[] = $row;
                        }

                                return $this->data;

                } // end load_some


                function insert($fieldarray)
                {
			global $dbconn;

                        $fieldlist = $this->fieldlist;

                        foreach($fieldarray as $field => $fieldvalue)
                        {
                                if(!in_array($field, $fieldlist))
                                {
                                        unset($fieldarray[$field]);
                                }
                        }

                        $q = "INSERT INTO $this->table_name SET ";

                        foreach($fieldarray as $item => $value)
                        {
                                $value = mysqli_real_escape_string($dbconn, $value);
                                $q .= "$item = '$value', ";
                        }

                        $q = rtrim($q, ', ');
//echo "<br>".$q;
                        mysqli_query($dbconn, $q) or die('ins: '.mysqli_error($dbconn));

                        return;

                }

                function update($fieldarray, $id)
                {
			global $dbconn;

                        $fieldlist = $this->fieldlist;

                        foreach($fieldarray as $field => $fieldvalue)
                        {
                                if(!in_array($field, $fieldlist))
                                {
                                        unset($fieldarray[$field]);
                                }
                        }

                        $q = "UPDATE $this->table_name SET ";

                        foreach($fieldarray as $item => $value)
                        {
                                $value = mysqli_real_escape_string($dbconn, $value);
                                $q .= "$item = '$value', ";
                        }

                        $q = rtrim($q, ', ');

                        $q .= " WHERE ";

                        $q .= $this->tbl_pfx."id = $id";

//echo "<h2>update disabled in GUI</h2>";

                        mysqli_query($dbconn, $q) or die('update: '.mysqli_error($dbconn));

                }

                function delete($id)
                {
			global $dbconn;

                        $q = "DELETE FROM $this->table_name WHERE ";
                        $q .= $this->tbl_pfx."id = $id";

                        if($_POST['delete_checked'] == 'indeed' || $_GET['delete_checked'] == 'indeed')
                        {
                                mysqli_query($dbconn, $q) or die('del: '.mysqli_error($dbconn));
                                echo "deleted";

                        }
                        else
                        {
                                echo "not deleted";
                        }
                }
        }
?>
