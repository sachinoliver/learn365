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


