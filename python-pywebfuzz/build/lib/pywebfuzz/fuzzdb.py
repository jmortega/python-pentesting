#!/usr/bin/env python
"""
This module uses logic to implement values from the fuzzdb project. 

(c) 2010 Nathan Hamiel
Email: nathan{at}neohaxor{dot}org
Hexsec Labs: http://hexsec.com/labs

fuzzdb project is (c) 2010 Adam Munter http://code.google.com/p/fuzzdb

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>

"""
import os
import sys

MODPATH = os.path.dirname(__file__)

def file_read(location):
    """ Read the file contents and return the results. Used in the construction
    of the values for the lists """
    
    path = MODPATH + location
    file = open(path, "rb")
    vals = list()
    
    for item in file.readlines():
        if item.startswith("# "):
            pass
        else:
            vals.append(item.rstrip())
        
    file.close()
    
    return(vals)

class attack_payloads:
    """ Placeholder namespace for the attack_payloads"""
    class all_attacks:
        """ This implements the all-attacks class of values from fuzzdb """
        
        # all-attacks-unix.txt
        location = "/data/attack-payloads/all-attacks/all-attacks-unix.txt"
        all_attacks_unix = file_read(location)
        
        # all-attacks-win.txt
        location = "/data/attack-payloads/all-attacks/all-attacks-win.txt"
        all_attacks_win = file_read(location)
        
        # interesting-metacharacters.txt
        location = "/data/attack-payloads/all-attacks/interesting-metacharacters.txt"
        interesting_metacharacters = file_read(location)
        
    class BizLogic:
        """ This implements the tiems from the BizLogic directory from fuzzdb """
        
        # CommonMethods.fuzz.txt
        location = "/data/attack-payloads/BizLogic/CommonMethods.fuzz.txt"
        CommonMethods = file_read(location)
        
    class control_chars:
        """ This implements the control-chars directory from fuzzdb """
        
        # null.fuzz
        location = "/data/attack-payloads/control-chars/null.fuzz"
        null_fuzz = file_read(location)
        
    class disclosure_directory:
        """ This implements the disclosure-directory from fuzzdb """
        
        class generic:
            """ This implements the generic payloads from fuzzdb """
            
            # directory-indexing-generic.txt
            location = "/data/attack-payloads/disclosure-directory/generic/directory-indexing-generic.txt"
            directory_indexing_generic = file_read(location)
        
        class unix:
            """ This implements the unix payloads from fuzzdb """
            # This class is currently empty
        
        class win:
            """ This implements the win payloads from fuzzdb"""
            # This class is currently empty
            
    class disclosure_localpaths:
        """ This implements the disclosure-localpaths from fuzzdb """
        
        class microsoft:
            """ microsoft payloads """
            # This class is currently empty
        
        class unix:
            """ unix payloads"""
            
            # common-unix-httpd-log-locations.txt
            location = "/data/attack-payloads/disclosure-localpaths/unix/common-unix-httpd-log-locations.txt"
            common_unix_httpd_log_locations = file_read(location)
            
    class disclosure_source:
        """ This implements the disclosure-source from fuzzdb """
        
        # source-disc-cmd-exec-traversal
        location = "/data/attack-payloads/disclosure-source/source-disc-cmd-exec-traversal.txt"
        source_disc_cmd_exec_traversal = file_read(location)
        
        # source-disclosure-generic.txt
        location = "/data/attack-payloads/disclosure-source/source-disclosure-generic.txt"
        source_disclosure_generic = file_read(location)
        
        # source-disclosure-microsoft.txt
        location = "/data/attack-payloads/disclosure-source/source-disclosure-microsoft.txt"
        source_disclosure_microsoft = file_read(location)
        
    class file_upload:
        """ This implements the file-upload from fuzzdb """
        
        # alt-extensions-asp.txt
        location = "/data/attack-payloads/file-upload/alt-extensions-asp.txt"
        alt_extensions_asp = file_read(location)
        
        # alt-extensions-coldfusion.txt
        location = "/data/attack-payloads/file-upload/alt-extensions-coldfusion.txt"
        alt_extensions_coldfusion = file_read(location)
        
        # alt-extensions-jsp.txt
        location = "/data/attack-payloads/file-upload/alt-extensions-jsp.txt"
        alt_extensions_jsp = file_read(location)
        
        # alt-extensions-perl.txt
        location = "/data/attack-payloads/file-upload/alt-extensions-perl.txt"
        alt_extensions_perl = file_read(location)
        
        # alt-extensions-php.txt
        location = "/data/attack-payloads/file-upload/alt-extensions-php.txt"
        alt_extensions_php = file_read(location)
        
        # file-ul-filter-bypass-commonly-writable-directories.txt
        location = "/data/attack-payloads/file-upload/file-ul-filter-bypass-commonly-writable-directories.txt"
        file_ul_filter_bypass_commonly_writable_directories = file_read(location)
        
        # file-ul-filter-bypass-microsoft-asp-filetype-bf.txt
        location = "/data/attack-payloads/file-upload/file-ul-filter-bypass-microsoft-asp-filetype-bf.txt"
        file_ul_filter_bypass_microsoft_asp_filetype_bf = file_read(location)
        
        # file-ul-filter-bypass-microsoft-asp.txt
        location = "/data/attack-payloads/file-upload/file-ul-filter-bypass-microsoft-asp.txt"
        file_ul_filter_bypass_microsoft_asp = file_read(location)
        
        # file-ul-filter-bypass-ms-php.txt
        location = "/data/attack-payloads/file-upload/file-ul-filter-bypass-ms-php.txt"
        file_ul_filter_bypass_ms_php = file_read(location)
        
        # file-ul-filter-bypass-x-platform-generic.txt
        location = "/data/attack-payloads/file-upload/file-ul-filter-bypass-x-platform-generic.txt"
        file_ul_filter_bypass_x_platform_generic = file_read(location)
        
        # file-ul-filter-bypass-x-platform-php.txt
        location = "/data/attack-payloads/file-upload/file-ul-filter-bypass-x-platform-php.txt"
        file_ul_filter_bypass_x_platform_php = file_read(location)
        
        # invalid-filenames-linux.txt
        location = "/data/attack-payloads/file-upload/invalid-filenames-linux.txt"
        invalid_filenames_linux = file_read(location)
        
        # invalid-filenames-microsoft.txt
        location = "/data/attack-payloads/file-upload/invalid-filenames-microsoft.txt"
        invalid_filenames_microsoft = file_read(location)
        
        # invalid-filesystem-chars-microsoft.txt
        location = "/data/attack-payloads/file-upload/invalid-filesystem-chars-microsoft.txt"
        invalid_filesystem_chars_microsoft = file_read(location)
        
        # invalid-filesystem-chars-osx.txt
        location = "/data/attack-payloads/file-upload/invalid-filesystem-chars-osx.txt"
        invalid_filesystem_chars_osx = file_read(location)
        
    class format_strings:
        """ This implements the format-strings from fuzzdb """
        
        # format-strings.txt
        location = "/data/attack-payloads/format-strings/format-strings.txt"
        format_strings = file_read(location)
                
    class html_fuzz:
        """ This implements the html_fuzz from the fuzzdb """
        
        # html_tags.txt
        location = "/data/attack-payloads/html_fuzz/html_tags.txt"
        html_tags = file_read(location)
                
        # javascript_events.txt
        location = "/data/attack-payloads/html_fuzz/javascript_events.txt"
        javascript_events = file_read(location)        
        
    class http_protocol:
        """ This implements the http-protocol from fuzzdb """
        
        # http-header-cache-poison.txt
        location = "/data/attack-payloads/http-protocol/http-header-cache-poison.txt"
        http_header_cache_poison = file_read(location)
                
        # http-protocol-methods.txt
        location = "/data/attack-payloads/http-protocol/http-protocol-methods.txt"
        http_protocol_methods = file_read(location)
                
        # user-agents.txt
        location = "/data/attack-payloads/http-protocol/user-agents.txt"
        user_agents = file_read(location)
        
    class integer_overflow:
        """ This implements the integer-overflow from fuzzdb """
        
        # integer-overflow.txt
        location = "/data/attack-payloads/integer-overflow/integer-overflows.txt"
        integer_overflows = file_read(location)
                
    class ldap:
        """ This implements the ldap payloads from fuzzdb """
        
        # ldap-injection.txt
        location = "/data/attack-payloads/ldap/ldap-injection.txt"
        ldap_injection = file_read(location)
                
    class lfi:
        """ This implements the lfi payloads from fuzzdb """
        # common-unix-httpd-log-locations.txt
        location = "/data/attack-payloads/lfi/common-unix-httpd-log-locations.txt"
        common_unix_httpd_log_locations = file_read(location)
                
    class os_cmd_execution:
        """ This implements the os-command-execution payloads from fuzzdb """
        
        # command-execution-unix.txt
        location = "/data/attack-payloads/os-cmd-execution/command-execution-unix.txt"
        command_execution_unix = file_read(location)
        
        # commands-unix.txt
        location = "/data/attack-payloads/os-cmd-execution/commands-unix.txt"
        commands_unix = file_read(location)
                
        # commands-windows.txt
        location = "/data/attack-payloads/os-cmd-execution/commands-windows.txt"
        commands_windows = file_read(location)
        
        # LinuxCommands.fuzz.txt
        location = "/data/attack-payloads/os-cmd-execution/LinuxCommands.fuzz.txt"
        LinuxCommands = file_read(location)
        
        # OSXCommands.fuzz.txt
        location = "/data/attack-payloads/os-cmd-execution/OSXCommands.fuzz.txt"
        OSXCommands = file_read(location)
        
        # source-disc-cmd-exec-traversal.txt
        location = "/data/attack-payloads/os-cmd-execution/source-disc-cmd-exec-traversal.txt"
        source_disc_cmd_exec_traversal = file_read(location)
        
        # WindowsCommands.fuzz.txt
        location = "/data/attack-payloads/os-cmd-execution/WindowsCommands.fuzz.txt"
        WindowsCommands = file_read(location)
        
        # WindowsPowershell.fuzz.txt
        location = "/data/attack-payloads/os-cmd-execution/WindowsPowershell.fuzz.txt"
        WindowsCommands = file_read(location)
                
    class os_dir_indexing:
        """ This implements the os-dir-indexing payloads from fuzzdb """
        # directory-indexing.txt
        location = "/data/attack-payloads/os-dir-indexing/directory-indexing.txt"
        directory_indexing = file_read(location)
        
    class path_traversal:
        """ This implements the path-traversal payloads from fuzzdb """
        
        # directory-indexing.txt
        location = "/data/attack-payloads/path-traversal/path-traversal-windows.txt"
        path_traversal_windows = file_read(location)
                
        # traversals-8-deep-exotic-encoding.txt
        location = "/data/attack-payloads/path-traversal/traversals-8-deep-exotic-encoding.txt"
        traversals_8_deep_exotic_encoding = file_read(location)
        
    class rfi:
        """ This implements the rfi payloads from fuzzdb """
        # rfi.txt
        location = "/data/attack-payloads/rfi/rfi.txt"
        rfi = file_read(location)
        
    class server_side_include:
        """ This implements the server-side-include payloads from fuzzdb """
        # server-side-includes-generic.txt
        location = "/data/attack-payloads/server-side-include/server-side-includes-generic.txt"
        server_side_includes_generic = file_read(location)
        
    class sql_injection:
        """ This implements the sql-injection class of payloads from fuzzdb """
        class detect:
            """ This implements detection class payloads from fuzzdb """
            
            # GenericBlind.fuzz.txt
            location = "/data/attack-payloads/sql-injection/detect/GenericBlind.fuzz.txt"
            GenericBlind = file_read(location)
            
            # MSSQL_blind.fuzz.txt
            location = "/data/attack-payloads/sql-injection/detect/MSSQL_blind.fuzz.txt"
            MSSQL_blind = file_read(location)
            
            # MSSQL.fuzz.txt
            location = "/data/attack-payloads/sql-injection/detect/MSSQL.fuzz.txt"
            MSSQL = file_read(location)
            
            # MySQL_MSSQL.fuzz.txt
            location = "/data/attack-payloads/sql-injection/detect/MySQL_MSSQL.fuzz.txt"
            MySQL_MSSQL = file_read(location)
            
            # MySQL.fuzz.txt
            location = "/data/attack-payloads/sql-injection/detect/MySQL.fuzz.txt"
            MySQL = file_read(location)
            
            # oracle.fuzz.txt
            location = "/data/attack-payloads/sql-injection/detect/oracle.fuzz.txt"
            oracle = file_read(location)
            
            # xplatform.fuzz.txt
            location = "/data/attack-payloads/sql-injection/detect/xplatform.fuzz.txt"
            xplatform = file_read(location)
                
        class exploit:
            """ This implements the exploit class of payloads from fuzzdb """
            # db2-enumeration.txt
            location = "/data/attack-payloads/sql-injection/exploit/db2-enumeration.txt"
            db2_enumeration = file_read(location)
            
            # ms-sql-enumeration.txt
            location = "/data/attack-payloads/sql-injection/exploit/ms-sql-enumeration.txt"
            ms_sql_enumeration = file_read(location)
            
            # mysql-injection-login-bypass.txt
            location = "/data/attack-payloads/sql-injection/exploit/mysql-injection-login-bypass.txt"
            mysql_injection_login_bypass = file_read(location)
            
            # mysql-read-local-files.txt
            location = "/data/attack-payloads/sql-injection/exploit/mysql-read-local-files.txt"
            mysql_read_local_files = file_read(location)
            
            # postgres-enumeration.txt
            location = "/data/attack-payloads/sql-injection/exploit/postgres-enumeration.txt"
            postgres_enumeration = file_read(location)
            
    class xml:
        """ This implements the xml payloads from fuzzdb """
        # xml-attacks.txt
        location = "/data/attack-payloads/xml/xml-attacks.txt"
        xml_attacks = file_read(location)
        
    class xpath:
        """ This implements the xpath payloads from fuzzdb """
        # xpath-injection.txt
        location = "/data/attack-payloads/xpath/xpath-injection.txt"
        xpath_injection = file_read(location)
        
    class xss:
        """ This implements the xss payloads from fuzzdb """
        # xss-rsnake.txt
        location = "/data/attack-payloads/xss/xss-rsnake.txt"
        xss_rsnake = file_read(location)

        # xss-uri.txt
        location = "/data/attack-payloads/xss/xss-uri.txt"
        xss_uri = file_read(location)
        
class Discovery:
    """ This implements the discovery class from fuzzdb """
    
    class FilenameBruteforce:
        """ This implements the FilenameBruteforce class from fuzzdb """
        
        # Extensions.Backup.fuzz.txt
        location = "/data/Discovery/FilenameBruteforce/Extensions.Backup.fuzz.txt"
        Extensions_Backup = file_read(location)
        
        # Extensions.Common.fuzz.txt
        location = "/data/Discovery/FilenameBruteforce/Extensions.Common.fuzz.txt"
        Extensions_Common = file_read(location)
        
        # Extensions.Compressed.fuzz.txt
        location = "/data/Discovery/FilenameBruteforce/Extensions.Compressed.fuzz.txt"
        Extensions_Compressed = file_read(location)
        
        # Extensions.Mostcommon.fuzz.txt
        location = "/data/Discovery/FilenameBruteforce/Extensions.Mostcommon.fuzz.txt"
        Extensions_Mostcommon = file_read(location)
        
        # Extensions.Skipfish.fuzz.txt
        location = "/data/Discovery/FilenameBruteforce/Extensions.Skipfish.fuzz.txt"
        Extensions_Skipfish = file_read(location)
        
        # WordlistSkipfish.fuzz.txt
        location = "/data/Discovery/FilenameBruteforce/WordlistSkipfish.fuzz.txt"
        WordlistSkipfish = file_read(location)
    
    class PredictableRes:
        """ This implements the PredictableRes class from fuzzdb """
        
        class CMS:
            """ This implements the cms payloads from fuzzdb """
            
            # drupal_plugins.fuzz.txt
            location = "/data/discovery/PredictableRes/CMS/drupal_plugins.fuzz.txt"
            drupal_plugins = file_read(location)
            
            # drupal_themes.fuzz.txt
            location = "/data/discovery/PredictableRes/CMS/drupal_themes.fuzz.txt"
            drupal_themes = file_read(location)
            
            # joomla_plugins.fuzz.txt
            location = "/data/discovery/PredictableRes/CMS/joomla_plugins.fuzz.txt"
            joomla_plugins = file_read(location)
            
            # joomla_themes.fuzz.txt
            location = "/data/discovery/PredictableRes/CMS/joomla_themes.fuzz.txt"
            joomla_themes = file_read(location)
            
            # wp_plugins.fuzz.txt
            location = "/data/discovery/PredictableRes/CMS/wp_plugins.fuzz.txt"
            wp_plugins = file_read(location)
            
            # wp_themes.fuzz.txt
            location = "/data/discovery/PredictableRes/CMS/wp_themes.fuzz.txt"
            wp_themes = file_read(location)
            
        # Apache.fuzz.txt
        location = "/data/discovery/PredictableRes/Apache.fuzz.txt"
        Apache = file_read(location)
        
        # ApacheTomcat.fuzz.txt
        location = "/data/discovery/PredictableRes/ApacheTomcat.fuzz.txt"
        ApacheTomcat = file_read(location)
        
        # CGI_HTTP_POST_WINDOWS.fuzz.txt
        location = "/data/discovery/PredictableRes/CGI_HTTP_POST_WINDOWS.fuzz.txt"
        CGI_HTTP_POST_WINDOWS = file_read(location)
        
        # CGI_HTTP_POST.fuzz.txt
        location = "/data/discovery/PredictableRes/CGI_HTTP_POST.fuzz.txt"
        CGI_HTTP_POST = file_read(location)
        
        # CGI_Microsoft.fuzz.txt
        location = "/data/discovery/PredictableRes/CGI_Microsoft.fuzz.txt"
        CGI_Microsoft = file_read(location)
        
        # CGI_XPlatform.fuzz.txt
        location = "/data/discovery/PredictableRes/CGI_XPlatform.fuzz.txt"
        CGI_XPlatform = file_read(location)
        
        # ColdFusion.fuzz.txt
        location = "/data/discovery/PredictableRes/ColdFusion.fuzz.txt"
        ColdFusion = file_read(location)
        
        # HTTP_POST_Microsoft.fuzz.txt
        location = "/data/discovery/PredictableRes/HTTP_POST_Microsoft.fuzz.txt"
        HTTP_POST_Microsoft = file_read(location)
        
        # Hyperion.fuzz.txt
        location = "/data/discovery/PredictableRes/Hyperion.fuzz.txt"
        Hyperion = file_read(location)
        
        # JavaServlets_Common.fuzz.txt
        location = "/data/discovery/PredictableRes/JavaServlets_Common.fuzz.txt"
        JavaServlets_Common = file_read(location)
        
        # JBoss.fuzz.txt
        location = "/data/discovery/PredictableRes/JBoss.fuzz.txt"
        JBoss = file_read(location)
        
        # KitchensinkDirectories.fuzz.txt
        location = "/data/discovery/PredictableRes/KitchensinkDirectories.fuzz.txt"
        KitchensinkDirectories = file_read(location)
        
        # Logins.fuzz.txt
        location = "/data/discovery/PredictableRes/Logins.fuzz.txt"
        Logins = file_read(location)
        
        # LotusNotes.fuzz.txt
        location = "/data/discovery/PredictableRes/LotusNotes.fuzz.txt"
        LotusNotes = file_read(location)
        
        # Netware.fuzz.txt
        location = "/data/discovery/PredictableRes/Netware.fuzz.txt"
        Netware = file_read(location)
        
        # OracleAppServer.fuzz.txt
        location = "/data/discovery/PredictableRes/OracleAppServer.fuzz.txt"
        OracleAppServer = file_read(location)
        
        # Passwords.fuzz.txt
        location = "/data/discovery/PredictableRes/Passwords.fuzz.txt"
        Passwords = file_read(location)
        
        # PHP_CommonBackdoors.fuzz.txt
        location = "/data/discovery/PredictableRes/PHP_CommonBackdoors.fuzz.txt"
        PHP_CommonBackdoors = file_read(location)
        
        # proxy-conf.fuzz.txt
        location = "/data/discovery/PredictableRes/proxy-conf.fuzz.txt"
        proxy_conf = file_read(location)
        
        # RandomFiles.fuzz.txt
        location = "/data/discovery/PredictableRes/RandomFiles.fuzz.txt"
        RandomFiles = file_read(location)
        
        # Sharepoint.fuzz.txt
        location = "/data/discovery/PredictableRes/Sharepoint.fuzz.txt"
        Sharepoint = file_read(location)
        
        # SiteMinder.fuzz.txt
        location = "/data/discovery/PredictableRes/SiteMinder.fuzz.txt"
        SiteMinder = file_read(location)
        
        # tftp.fuzz.txt
        location = "/data/discovery/PredictableRes/tftp.fuzz.txt"
        tftp = file_read(location)
        
        # UserAgents.fuzz.txt
        location = "/data/discovery/PredictableRes/UserAgents.fuzz.txt"
        UserAgents = file_read(location)
        
        # Websphere.fuzz.txt
        location = "/data/discovery/PredictableRes/Websphere.fuzz.txt"
        Websphere = file_read(location)
        
        
class regex:
    """ This implements the regex payloads from fuzzdb """
    # errors.txt
    location = "/data/regex/errors.txt"
    errors = file_read(location)
    
    # sessionid.txt
    location = "/data/regex/sessionid.txt"
    sessionid = file_read(location)
    
class wordlists_misc:
    """ This implements the wordlists-misc payloads from fuzzdb """
    # common-http-ports.txt
    location = "/data/wordlists-misc/common-http-ports.txt"
    common_http_ports = file_read(location)
    
    # us_cities.txt
    location = "/data/wordlists-misc/us_cities.txt"
    us_cities = file_read(location)
    
    # wordlist-alphanumeric-case.txt
    location = "/data/wordlists-misc/wordlist-alphanumeric-case.txt"
    wordlist_alphanumeric_case = file_read(location)
    
    # wordlist-common-snmp-community-strings.txt
    location = "/data/wordlists-misc/wordlist-common-snmp-community-strings.txt"
    wordlist_common_snmp_community_strings = file_read(location)
    
    # wordlist-dna.txt
    location = "/data/wordlists-misc/wordlist-dna.txt"
    wordlist_dna = file_read(location)
    
class wordlists_user_passwd:
    """ This implements the wordlists-user-passwd class from fuzzdb """
    class db2:
        """ This implements the db2 payloads from fuzzdb """
        # db2_default_pass.txt
        location = "/data/wordlists-user-passwd/db2/db2_default_pass.txt"
        db2_default_pass = file_read(location)
        
        # db2_default_user.txt
        location = "/data/wordlists-user-passwd/db2/db2_default_user.txt"
        db2_default_user = file_read(location)
        
        # db2_default_userpass.txt
        location = "/data/wordlists-user-passwd/db2/db2_default_userpass.txt"
        db2_default_userpass = file_read(location)
        
    class generic_listpairs:
        """ This implements the generic-listpairs payloads from fuzzdb """
        # http_default_pass.txt
        location = "/data/wordlists-user-passwd/generic-listpairs/http_default_pass.txt"
        http_default_pass = file_read(location)
        
        # http_default_userpass.txt
        location = "/data/wordlists-user-passwd/generic-listpairs/http_default_userpass.txt"
        http_default_userpass = file_read(location)
        
        # http_default_users.txt
        location = "/data/wordlists-user-passwd/generic-listpairs/http_default_users.txt"
        http_default_users = file_read(location)
        
    class names:
        """ This implements the names payloads from fuzzdb """
        # namelist.txt
        location = "/data/wordlists-user-passwd/names/namelist.txt"
        namelist = file_read(location)
        
    class oracle:
        """ This implements the oracle payloads from fuzzdb """
        # _hci_oracle_passwords.txt
        location = "/data/wordlists-user-passwd/oracle/_hci_oracle_passwords.txt"
        _hci_oracle_passwords = file_read(location)
        
        # _oracle_default_passwords.txt
        location = "/data/wordlists-user-passwd/oracle/_oracle_default_passwords.txt"
        _oracle_default_passwords = file_read(location)
        
    class passwds:
        """ This implements the passwds payloads from fuzzdb """
        # john.txt
        location = "/data/wordlists-user-passwd/passwds/john.txt"
        john = file_read(location)
        
        # phpbb.txt
        location = "/data/wordlists-user-passwd/passwds/phpbb.txt"
        phpbb = file_read(location)
        
        # twitter.txt
        location = "/data/wordlists-user-passwd/passwds/twitter.txt"
        twitter = file_read(location)
        
        # weaksauce.txt
        location = "/data/wordlists-user-passwd/passwds/weaksauce.txt"
        weaksauce = file_read(location)
        
    class postgres:
        """ This implements the postgres payloads from fuzzdb """
        # postgres_default_pass.txt
        location = "/data/wordlists-user-passwd/postgres/postgres_default_pass.txt"
        postgres_default_pass = file_read(location)
        
        # postgres_default_user.txt
        location = "/data/wordlists-user-passwd/postgres/postgres_default_user.txt"
        postgres_default_user = file_read(location)
        
        # postgres_default_userpass.txt
        location = "/data/wordlists-user-passwd/postgres/postgres_default_userpass.txt"
        postgres_default_userpass = file_read(location)
        
    class tomcat:
        """ This implements the tomcat payloads from fuzzdb """
        # tomcat_mgr_default_pass.txt
        location = "/data/wordlists-user-passwd/tomcat/tomcat_mgr_default_pass.txt"
        tomcat_mgr_default_pass = file_read(location)
        
        # tomcat_mgr_default_userpass.txt
        location = "/data/wordlists-user-passwd/tomcat/tomcat_mgr_default_userpass.txt"
        tomcat_mgr_default_userpass = file_read(location)
        
        # tomcat_mgr_default_users.txt
        location = "/data/wordlists-user-passwd/tomcat/tomcat_mgr_default_users.txt"
        tomcat_mgr_default_users = file_read(location)
        
    class unix_os:
        """ This implements the unix-os payloads from fuzzdb """
        # unix_passwords.txt
        location = "/data/wordlists-user-passwd/unix-os/unix_passwords.txt"
        unix_passwords = file_read(location)
        
        # unix_users.txt
        location = "/data/wordlists-user-passwd/unix-os/unix_users.txt"
        unix_users = file_read(location)
        
    # faithwriters.txt
    location = "/data/wordlists-user-passwd/faithwriters.txt"
    faithwriters = file_read(location)
    