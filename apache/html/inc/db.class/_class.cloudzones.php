<?php
        class CloudZone extends Gen
        {
                var $table_name;
                var $tbl_pfx;
                var $data_array;
                var $fieldlist;

                function __construct()
                {
                        $this->table_name       =       'cloudZones';
                        $this->tbl_pfx          =       '';
                        $this->data_array       =       array();
                        $this->fieldlist        =       array(
                                                              'zone',
                                                              'alias',
                                                              'architecture',
                                                              'zone_release',
                                                              'status',
                                                              'cycle',
                                                              'prod_date',
                                                              'cloud'
                                                                );

                } // end __construct

        } // end class

