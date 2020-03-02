<?php
        class CheckPattern extends Gen
        {
                var $table_name;
                var $tbl_pfx;
                var $data_array;
                var $fieldlist;

                function __construct()
                {
                        $this->table_name       =       'checkPatterns';
                        $this->tbl_pfx          =       '';
                        $this->data_array       =       array();
                        $this->fieldlist        =       array(
                                                              'cloud',
                                                              'components',
                                                              'pattern',
                                                              'type',
                                                                );

                } // end __construct

        } // end class

