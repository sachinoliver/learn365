## Nmap
```bash

nmap -p- -sV -sC -v -oA enum --min-rate 4500 --max-rtt-timeout 1500ms --open 10.129.95.210
Starting Nmap 7.92 ( https://nmap.org ) at 2021-12-19 07:18 IST
NSE: Loaded 155 scripts for scanning.
NSE: Script Pre-scanning.
Initiating NSE at 07:18
Completed NSE at 07:18, 0.00s elapsed
Initiating NSE at 07:18
Completed NSE at 07:18, 0.00s elapsed
Initiating NSE at 07:18
Completed NSE at 07:18, 0.00s elapsed
Initiating Ping Scan at 07:18
Scanning 10.129.95.210 [4 ports]
Completed Ping Scan at 07:18, 0.27s elapsed (1 total hosts)
Initiating Parallel DNS resolution of 1 host. at 07:18
Completed Parallel DNS resolution of 1 host. at 07:18, 0.31s elapsed
Initiating SYN Stealth Scan at 07:18
Scanning 10.129.95.210 [65535 ports]
Discovered open port 135/tcp on 10.129.95.210
Discovered open port 139/tcp on 10.129.95.210
Discovered open port 53/tcp on 10.129.95.210
Discovered open port 445/tcp on 10.129.95.210
Discovered open port 49685/tcp on 10.129.95.210
Discovered open port 49681/tcp on 10.129.95.210
Discovered open port 49701/tcp on 10.129.95.210
Discovered open port 3268/tcp on 10.129.95.210
Discovered open port 47001/tcp on 10.129.95.210
Discovered open port 49665/tcp on 10.129.95.210
Discovered open port 593/tcp on 10.129.95.210
Discovered open port 49664/tcp on 10.129.95.210
Discovered open port 464/tcp on 10.129.95.210
Discovered open port 636/tcp on 10.129.95.210
Discovered open port 9389/tcp on 10.129.95.210
Discovered open port 88/tcp on 10.129.95.210
Discovered open port 49671/tcp on 10.129.95.210
Discovered open port 49667/tcp on 10.129.95.210
Discovered open port 3269/tcp on 10.129.95.210
Discovered open port 389/tcp on 10.129.95.210
Discovered open port 49680/tcp on 10.129.95.210
Discovered open port 49666/tcp on 10.129.95.210
Discovered open port 5985/tcp on 10.129.95.210
Completed SYN Stealth Scan at 07:18, 15.40s elapsed (65535 total ports)
Initiating Service scan at 07:18
Scanning 23 services on 10.129.95.210
Completed Service scan at 07:19, 56.91s elapsed (23 services on 1 host)
NSE: Script scanning 10.129.95.210.
Initiating NSE at 07:19
Completed NSE at 07:19, 12.75s elapsed
Initiating NSE at 07:19
Completed NSE at 07:19, 5.05s elapsed
Initiating NSE at 07:19
Completed NSE at 07:19, 0.00s elapsed
Nmap scan report for 10.129.95.210
Host is up (0.17s latency).
Not shown: 65501 closed tcp ports (reset), 11 filtered tcp ports (no-response)
Some closed ports may be reported as filtered due to --defeat-rst-ratelimit
PORT      STATE SERVICE      VERSION
53/tcp    open  domain       Simple DNS Plus
88/tcp    open  kerberos-sec Microsoft Windows Kerberos (server time: 2021-12-19 01:55:17Z)
135/tcp   open  msrpc        Microsoft Windows RPC
139/tcp   open  netbios-ssn  Microsoft Windows netbios-ssn
389/tcp   open  ldap         Microsoft Windows Active Directory LDAP (Domain: htb.local, Site: Default-First-Site-Name)
445/tcp   open  microsoft-ds Windows Server 2016 Standard 14393 microsoft-ds (workgroup: HTB)
464/tcp   open  kpasswd5?
593/tcp   open  ncacn_http   Microsoft Windows RPC over HTTP 1.0
636/tcp   open  tcpwrapped
3268/tcp  open  ldap         Microsoft Windows Active Directory LDAP (Domain: htb.local, Site: Default-First-Site-Name)
3269/tcp  open  tcpwrapped
5985/tcp  open  http         Microsoft HTTPAPI httpd 2.0 (SSDP/UPnP)
|_http-title: Not Found
|_http-server-header: Microsoft-HTTPAPI/2.0
9389/tcp  open  mc-nmf       .NET Message Framing
47001/tcp open  http         Microsoft HTTPAPI httpd 2.0 (SSDP/UPnP)
|_http-title: Not Found
|_http-server-header: Microsoft-HTTPAPI/2.0
49664/tcp open  msrpc        Microsoft Windows RPC
49665/tcp open  msrpc        Microsoft Windows RPC
49666/tcp open  msrpc        Microsoft Windows RPC
49667/tcp open  msrpc        Microsoft Windows RPC
49671/tcp open  msrpc        Microsoft Windows RPC
49680/tcp open  ncacn_http   Microsoft Windows RPC over HTTP 1.0
49681/tcp open  msrpc        Microsoft Windows RPC
49685/tcp open  msrpc        Microsoft Windows RPC
49701/tcp open  msrpc        Microsoft Windows RPC
Service Info: Host: FOREST; OS: Windows; CPE: cpe:/o:microsoft:windows

Host script results:
|_clock-skew: mean: 2h46m49s, deviation: 4h37m08s, median: 6m48s
| smb-security-mode: 
|   account_used: <blank>
|   authentication_level: user
|   challenge_response: supported
|_  message_signing: required
| smb-os-discovery: 
|   OS: Windows Server 2016 Standard 14393 (Windows Server 2016 Standard 6.3)
|   Computer name: FOREST
|   NetBIOS computer name: FOREST\x00
|   Domain name: htb.local
|   Forest name: htb.local
|   FQDN: FOREST.htb.local
|_  System time: 2021-12-18T17:56:10-08:00
| smb2-security-mode: 
|   3.1.1: 
|_    Message signing enabled and required
| smb2-time: 
|   date: 2021-12-19T01:56:13
|_  start_date: 2021-12-19T01:53:34

NSE: Script Post-scanning.
Initiating NSE at 07:19
Completed NSE at 07:19, 0.00s elapsed
Initiating NSE at 07:19
Completed NSE at 07:19, 0.00s elapsed
Initiating NSE at 07:19
Completed NSE at 07:19, 0.00s elapsed
Read data files from: /usr/bin/../share/nmap
Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 91.64 seconds
           Raw packets sent: 67911 (2.988MB) | Rcvd: 67510 (2.700MB)
