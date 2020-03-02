<?php
    $local_ip = getenv("GARGOYLE_IP");
    $api_user = getenv("API_USER");
    $api_pw = getenv("API_PW");
    $kibana_frontport = getenv("KIBANA_FRONTPORT");
    $apache_frontport = getenv("APACHE_FRONTPORT");
    $api_frontport = getenv("API_FRONTPORT");
?>

<!DOCTYPE html>
<html>
<title>Homepage</title>
<style>
 BODY { background-color: #3399ff; color: #ffffff; font-size: 1.2em; }
 A { color: #ffffff; }
 .syntax { font-family: Courier New; }
</style>
<body>

<p>
<h3><a href="https://<?php echo $local_ip . ":" . $kibana_frontport; ?>/login?next=%2F">Kibana</a><h3>

<h3><a href="https://<?php echo $local_ip . ":" . $apache_frontport; ?>/db.php?cat=securitychecks&cmd=update&way=desc&orderby=enabled">Table View</a></h3>

<h3>API Views
<br><a href="https://<?php echo $api_user . ":" . $api_pw . "@" . $local_ip . ":" . $api_frontport; ?>/v2/checks">Security Checks</a>
<br><a href="https://<?php echo $api_user . ":" . $api_pw . "@" . $local_ip . ":" . $api_frontport; ?>/v2/patterns">Patterns</a>
<br><a href="https://<?php echo $api_user . ":" . $api_pw . "@" . $local_ip . ":" . $api_frontport; ?>/v2/zones">Zones</a>
</h3>

<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<div style="width: 100%; text-align: left;">
</div>
</body>
</html>
