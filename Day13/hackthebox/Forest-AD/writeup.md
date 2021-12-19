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
