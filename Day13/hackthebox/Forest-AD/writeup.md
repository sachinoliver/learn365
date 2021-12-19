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
```           
           
           
           
```
smbclient -L 10.129.95.210 
Enter WORKGROUP\root's password: 
Anonymous login successful

        Sharename       Type      Comment
        ---------       ----      -------
Reconnecting with SMB1 for workgroup listing.
do_connect: Connection to 10.129.95.210 failed (Error NT_STATUS_RESOURCE_NAME_NOT_FOUND)
Unable to connect with SMB1 -- no workgroup available
                                                                                                                                                                                            
┌──(root💀oliver)-[~/Downloads/hackthebox/Forest]
└─# nslookup                                                                                   
> server 10.129.95.210
Default server: 10.129.95.210
Address: 10.129.95.210#53
> 127.0.0.1
1.0.0.127.in-addr.arpa  name = localhost.
> 10.129.95.210
;; connection timed out; no servers could be reached

>                                                                                                                                                                                             
┌──(root💀oliver)-[~/Downloads/hackthebox/Forest]
└─# ldapsearch -h 10.129.95.210                                                                                                                                                         1 ⨯
SASL/EXTERNAL authentication started
ldap_sasl_interactive_bind_s: Unknown authentication method (-6)
        additional info: SASL(-4): no mechanism available: 
                                                                                                                                                                                            
┌──(root💀oliver)-[~/Downloads/hackthebox/Forest]
└─# ldapsearch -h 10.129.95.210 -x                                                                                                                                                    250 ⨯
# extended LDIF
#
# LDAPv3
# base <> (default) with scope subtree
# filter: (objectclass=*)
# requesting: ALL
#

# search result
search: 2
result: 32 No such object
text: 0000208D: NameErr: DSID-0310021B, problem 2001 (NO_OBJECT), data 0, best 
 match of:
        ''


# numResponses: 1
                                                                                                                                                                                            
┌──(root💀oliver)-[~/Downloads/hackthebox/Forest]
└─# ldapsearch -h 10.129.95.210 -x -s base namingcontexts                                                                                                                              32 ⨯
# extended LDIF
#
# LDAPv3
# base <> (default) with scope baseObject
# filter: (objectclass=*)
# requesting: namingcontexts 
#

#
dn:
namingContexts: DC=htb,DC=local
namingContexts: CN=Configuration,DC=htb,DC=local
namingContexts: CN=Schema,CN=Configuration,DC=htb,DC=local
namingContexts: DC=DomainDnsZones,DC=htb,DC=local
namingContexts: DC=ForestDnsZones,DC=htb,DC=local

# search result
search: 2
result: 0 Success

# numResponses: 2
# numEntries: 1
                                                                                                                                                                                            
┌──(root💀oliver)-[~/Downloads/hackthebox/Forest]
└─# ldapsearch -h 10.129.95.210 -x -b "DC=htb,DC=local"  
# extended LDIF
#
# LDAPv3
# base <DC=htb,DC=local> with scope subtree
# filter: (objectclass=*)
# requesting: ALL
#

# htb.local
dn: DC=htb,DC=local
objectClass: top
objectClass: domain
objectClass: domainDNS
distinguishedName: DC=htb,DC=local
instanceType: 5
whenCreated: 20190918174549.0Z
whenChanged: 20211219015324.0Z
subRefs: DC=ForestDnsZones,DC=htb,DC=local
subRefs: DC=DomainDnsZones,DC=htb,DC=local
subRefs: CN=Configuration,DC=htb,DC=local
uSNCreated: 4099
dSASignature:: AQAAACgAAAAAAAAAAAAAAAAAAAAAAAAAOqNrI1l5QUq5WV+CaJoIcQ==
uSNChanged: 929834
name: htb
objectGUID:: Gsfw30mpJkuMe1Lj4stuqw==
replUpToDateVector:: AgAAAAAAAAASAAAAAAAAAIArugegK3xCjpG3jOKvTZsK8AAAAAAAAPxOm
 RMDAAAAEeYhGk0xaEyawzvMi5bZbx0ADQAAAAAA1L0+FwMAAABptVkf+oupR7OwUi6g1GLsFlADAA
 AAAAAB1aoTAwAAADqjayNZeUFKuVlfgmiaCHEFoAAAAAAAAF8hmRMDAAAA550WLBTQ2UuhowLQP8A
 4SyAwDgAAAAAAkiHPFwMAAAD9IT857pY2TLBDvA9wjXW6GRAEAAAAAABuyT0XAwAAABA8AUG0jJ1F
 iOJ6vAWO49cVMAMAAAAAANXXphMDAAAAtTDGYaJBsEWxNEEatU4xYwjQAAAAAAAAnz2ZEwMAAABOf
 GN4ZhbsSauczVHuYEiBE3ACAAAAAADdbaATAwAAADH0xotFcHlDppuZ8rSNJnAMEAEAAAAAAIbFmR
 MDAAAAtwL+jwq2+0WZliEirTGKpwawAAAAAAAA1ymZEwMAAAAaxJ+QNDLHQ55lTGqoLvfGCwABAAA
 AAADKrZkTAwAAAFBd76JcNvNMvcbhLzeCkdkXoAMAAAAAAGmqqxMDAAAAGcL6qk8Zs0qRG/BZYykq
 ex+QDQAAAAAADsc+FwMAAAB5TzHrWI2FTZJLavLc7Dl3CeAAAAAAAADPRZkTAwAAAMnKXu73q7hBp
 RxZtKkWpCEecA0AAAAAAJnFPhcDAAAAEuOp8cC6t0+uaoe83jqnLQfAAAAAAAAAwzeZEwMAAACevY
 D5RBP7RbrYAQrgjhuPHNAMAAAAAACxrz4XAwAAAA==
creationTime: 132843524041570720
forceLogoff: -9223372036854775808
lockoutDuration: -18000000000
lockOutObservationWindow: -18000000000
lockoutThreshold: 0
---------------------------snip----------------------------------------------------------------



```
