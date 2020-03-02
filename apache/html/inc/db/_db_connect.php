<?php

        $dbhost = getenv("DB_HOST");
        $username = getenv("DB_USER");
        $password = getenv("DB_PW");
        $database = getenv("DB_DATABASE");
        $cacrt = getenv("CACRT_FILE");
        $clientcrt = getenv("CLIENTCRT_FILE");
        $clientkey = getenv("CLIENTKEY_FILE");

        $obj = mysqli_init();
        $obj->options(MYSQLI_OPT_SSL_VERIFY_SERVER_CERT, true);
        $obj->ssl_set("/etc/apache2/certs/".$clientkey, "/etc/apache2/certs/".$clientcrt, "/etc/apache2/certs/".$cacrt, NULL, NULL);
        mysqli_real_connect($obj, $dbhost, $username, $password, $database);
        $dbconn = $obj;

        if (mysqli_connect_errno()) {
           echo "Failed to connect to MySQL: " . mysqli_connect_error();
        }
?>
