## Nmap scan
```bash
nmap -sC -sV -A -T4 10.129.186.91 -oN nmap.txt 
Starting Nmap 7.92 ( https://nmap.org ) at 2021-12-06 20:18 IST
Nmap scan report for 10.129.186.91
Host is up (0.17s latency).
Not shown: 997 filtered tcp ports (no-response)
PORT     STATE SERVICE VERSION
22/tcp   open  ssh     OpenSSH 7.9p1 Debian 10+deb10u2 (protocol 2.0)
| ssh-hostkey: 
|   2048 16:bb:a0:a1:20:b7:82:4d:d2:9f:35:52:f4:2e:6c:90 (RSA)
|   256 ca:ad:63:8f:30:ee:66:b1:37:9d:c5:eb:4d:44:d9:2b (ECDSA)
|_  256 2d:43:bc:4e:b3:33:c9:82:4e:de:b6:5e:10:ca:a7:c5 (ED25519)
2222/tcp open  ssh     OpenSSH 7.6p1 Ubuntu 4ubuntu0.3 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey: 
|   2048 a9:a4:5c:e3:a9:05:54:b1:1c:ae:1b:b7:61:ac:76:d6 (RSA)
|   256 c9:58:53:93:b3:90:9e:a0:08:aa:48:be:5e:c4:0a:94 (ECDSA)
|_  256 c7:07:2b:07:43:4f:ab:c8:da:57:7f:ea:b5:50:21:bd (ED25519)
8080/tcp open  http    Apache httpd 2.4.38 ((Debian))
|_http-title: Site doesn't have a title (text/html; charset=UTF-8).
| http-robots.txt: 2 disallowed entries 
|_/vpn/ /.ftp_uploads/
|_http-server-header: Apache/2.4.38 (Debian)
Warning: OSScan results may be unreliable because we could not find at least 1 open and 1 closed port
Aggressive OS guesses: Linux 4.15 - 5.6 (92%), Linux 5.0 (92%), Linux 5.0 - 5.4 (91%), Linux 2.6.32 (91%), Linux 5.0 - 5.3 (90%), Crestron XPanel control system (90%), Linux 5.3 - 5.4 (90%), Linux 5.4 (89%), ASUS RT-N56U WAP (Linux 3.4) (87%), Linux 3.1 (87%)
No exact OS matches for host (test conditions non-ideal).
Network Distance: 2 hops
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel

TRACEROUTE (using port 22/tcp)
HOP RTT       ADDRESS
1   199.14 ms 10.10.14.1
2   199.22 ms 10.129.186.91

OS and Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 47.75 seconds

```
```bash
gobuster dir -u http://10.129.186.91:8080/ -w /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt -t 50 -x .php,txt
===============================================================
Gobuster v3.1.0
by OJ Reeves (@TheColonial) & Christian Mehlmauer (@firefart)
===============================================================
[+] Url:                     http://10.129.186.91:8080/
[+] Method:                  GET
[+] Threads:                 50
[+] Wordlist:                /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt
[+] Negative Status codes:   404
[+] User Agent:              gobuster/3.1.0
[+] Extensions:              php,txt
[+] Timeout:                 10s
===============================================================
2021/12/06 20:29:46 Starting gobuster in directory enumeration mode
===============================================================
/index.php            (Status: 200) [Size: 0]
/robots.txt           (Status: 200) [Size: 55]
```
```bash
# git clone https://github.com/yonjar/fixgz.git
Cloning into 'fixgz'...
remote: Enumerating objects: 10, done.
remote: Counting objects: 100% (10/10), done.
remote: Compressing objects: 100% (9/9), done.
remote: Total 10 (delta 1), reused 0 (delta 0), pack-reused 0
Receiving objects: 100% (10/10), 9.19 KiB | 4.60 MiB/s, done.
Resolving deltas: 100% (1/1), done.
                                                                                                                                                                                                                                           
┌──(root💀sac)-[~/Downloads/hackthebox/www]
└─# cd fixgz 
                                                                                                                                                                                                                                           
┌──(root💀sac)-[~/Downloads/hackthebox/www/fixgz]
└─# ls -la               
total 44
drwxr-xr-x 3 root root  4096 Dec  6 20:34 .
drwxr-xr-x 3 root root  4096 Dec  6 20:34 ..
-rw-r--r-- 1 root root  1394 Dec  6 20:34 fixgz.cpp
-rw-r--r-- 1 root root 22763 Dec  6 20:34 fixgz.exe
drwxr-xr-x 8 root root  4096 Dec  6 20:34 .git
-rw-r--r-- 1 root root   135 Dec  6 20:34 README.md
                                                                                                                                                                                                                                           
┌──(root💀sac)-[~/Downloads/hackthebox/www/fixgz]
└─# g++ fixgz.cpp -o fixgz
                                                                                                                                                                                                                                           
┌──(root💀sac)-[~/Downloads/hackthebox/www/fixgz]
└─# ls -la
total 60
drwxr-xr-x 3 root root  4096 Dec  6 20:34 .
drwxr-xr-x 3 root root  4096 Dec  6 20:34 ..
-rwxr-xr-x 1 root root 16336 Dec  6 20:34 fixgz
-rw-r--r-- 1 root root  1394 Dec  6 20:34 fixgz.cpp
-rw-r--r-- 1 root root 22763 Dec  6 20:34 fixgz.exe
drwxr-xr-x 8 root root  4096 Dec  6 20:34 .git
-rw-r--r-- 1 root root   135 Dec  6 20:34 README.md
                                                                                                                                                                                                                                           
┌──(root💀sac)-[~/Downloads/hackthebox/www/fixgz]
└─# ./fixgz db.sql.gz db.gz                                                                                                  
fixgz: cannot open db.sql.gz
                                                                                                                                                                                                                                           
┌──(root💀sac)-[~/Downloads/hackthebox/www/fixgz]
└─# ./fixgz db.sql.gz db.gz                                                                                                                                                                                                            1 ⨯
                                                                                                                                                                                                                                           
┌──(root💀sac)-[~/Downloads/hackthebox/www/fixgz]
└─# ls -la
total 68
drwxr-xr-x 3 root root  4096 Dec  6 20:37 .
drwxr-xr-x 3 root root  4096 Dec  6 20:37 ..
-rw-r--r-- 1 root root   258 Dec  6 20:37 db.gz
-rw-r--r-- 1 root root   262 Dec  6 20:36 db.sql.gz
-rwxr-xr-x 1 root root 16336 Dec  6 20:34 fixgz
-rw-r--r-- 1 root root  1394 Dec  6 20:34 fixgz.cpp
-rw-r--r-- 1 root root 22763 Dec  6 20:34 fixgz.exe
drwxr-xr-x 8 root root  4096 Dec  6 20:34 .git
-rw-r--r-- 1 root root   135 Dec  6 20:34 README.md                                                                                                                                                                                                                                        
┌──(root💀sac)-[~/Downloads/hackthebox/www/fixgz]
└─# gunzip db.gz                                                                                                                                                                                                                       1 ⨯
                                                                                                                                                                                                                                           
┌──(root💀sac)-[~/Downloads/hackthebox/www/fixgz]
└─# cat db      
CREATE DATABASE static;
USE static;
CREATE TABLE users ( id smallint unsigned not null auto_increment, username varchar(20) not null, password varchar(40) not null, totp varchar(16) not null, primary key (id) ); 
INSERT INTO users ( id, username, password, totp ) VALUES ( null, 'admin', 'd033e22ae348aeb5660fc2140aec35850c4da997', 'orxxi4c7orxwwzlo' );

                                                                                                                                                                                                                                           
┌──(root💀sac)-[~/Downloads/hackthebox/www/fixgz]
└─# nvim hash
                                                                                                                                                                                                                                           
┌──(root💀sac)-[~/Downloads/hackthebox/www/fixgz]
└─# john hash
Created directory: /root/.john
Warning: detected hash type "Raw-SHA1", but the string is also recognized as "Raw-SHA1-AxCrypt"
Use the "--format=Raw-SHA1-AxCrypt" option to force loading these as that type instead
Warning: detected hash type "Raw-SHA1", but the string is also recognized as "Raw-SHA1-Linkedin"
Use the "--format=Raw-SHA1-Linkedin" option to force loading these as that type instead
Warning: detected hash type "Raw-SHA1", but the string is also recognized as "ripemd-160"
Use the "--format=ripemd-160" option to force loading these as that type instead
Warning: detected hash type "Raw-SHA1", but the string is also recognized as "has-160"
Use the "--format=has-160" option to force loading these as that type instead
Using default input encoding: UTF-8
Loaded 1 password hash (Raw-SHA1 [SHA1 256/256 AVX2 8x])
Warning: no OpenMP support for this hash type, consider --fork=16
Proceeding with single, rules:Single
Press 'q' or Ctrl-C to abort, almost any other key for status
Almost done: Processing the remaining buffered candidate passwords, if any.
Proceeding with wordlist:/usr/share/john/password.lst
admin            (?)     
1g 0:00:00:00 DONE 2/3 (2021-12-06 20:40) 100.0g/s 282400p/s 282400c/s 282400C/s Winnie..admin1
Use the "--show --format=Raw-SHA1" options to display all of the cracked passwords reliably
Session completed.
```
