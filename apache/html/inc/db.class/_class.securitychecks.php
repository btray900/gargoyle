<?php
        class SecurityCheck extends Gen
        {
                var $table_name;
                var $tbl_pfx;
                var $data_array;
                var $fieldlist;

                function __construct()
                {
                        $this->table_name       =       'securityChecks';
                        $this->tbl_pfx          =       '';
                        $this->data_array       =       array();
                        $this->fieldlist        =       array(
                                                                'component',
                                                                'checkID',
                                                                'checkTask',
                                                                'command',
                                                                'regex',
                                                                'resource',
                                                                'expected',
                                                                'checkValue',
                                                                'valueLogic',
								'fkFunction',
                                                                'info',
								'reference',
                                                                'aspr',
                                                                'cloud',
								'cloudVersion',
                                                                'enabled',
                                                                'foundationCheck',
                                                                'reportEnabled',
                                                                'reportLabel',
								'releaseLabel'
                                                                );

                } // end __construct

        } // end class

