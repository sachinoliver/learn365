Nmap
```bash
nmap -vvv -A -v -oN intial.nmap 10.13.37.11  
Starting Nmap 7.80 ( https://nmap.org ) at 2021-11-16 03:33 EST
NSE: Loaded 151 scripts for scanning.
NSE: Script Pre-scanning.
NSE: Starting runlevel 1 (of 3) scan.
Initiating NSE at 03:33
Completed NSE at 03:33, 0.00s elapsed
NSE: Starting runlevel 2 (of 3) scan.
Initiating NSE at 03:33
Completed NSE at 03:33, 0.00s elapsed
NSE: Starting runlevel 3 (of 3) scan.
Initiating NSE at 03:33
Completed NSE at 03:33, 0.00s elapsed
Initiating Ping Scan at 03:33
Scanning 10.13.37.11 [4 ports]
Completed Ping Scan at 03:33, 0.25s elapsed (1 total hosts)
Initiating Parallel DNS resolution of 1 host. at 03:33
Completed Parallel DNS resolution of 1 host. at 03:33, 0.02s elapsed
DNS resolution of 1 IPs took 0.02s. Mode: Async [#: 1, OK: 0, NX: 1, DR: 0, SF: 0, TR: 1, CN: 0]
Initiating SYN Stealth Scan at 03:33
Scanning 10.13.37.11 [1000 ports]
Discovered open port 22/tcp on 10.13.37.11
Discovered open port 80/tcp on 10.13.37.11
Discovered open port 5000/tcp on 10.13.37.11
Completed SYN Stealth Scan at 03:33, 4.52s elapsed (1000 total ports)
Initiating Service scan at 03:33
Scanning 3 services on 10.13.37.11
Completed Service scan at 03:34, 23.55s elapsed (3 services on 1 host)
Initiating OS detection (try #1) against 10.13.37.11
Retrying OS detection (try #2) against 10.13.37.11
Retrying OS detection (try #3) against 10.13.37.11
Retrying OS detection (try #4) against 10.13.37.11
Retrying OS detection (try #5) against 10.13.37.11
Initiating Traceroute at 03:34
Completed Traceroute at 03:34, 0.23s elapsed
Initiating Parallel DNS resolution of 2 hosts. at 03:34
Completed Parallel DNS resolution of 2 hosts. at 03:34, 0.02s elapsed
DNS resolution of 2 IPs took 0.02s. Mode: Async [#: 1, OK: 0, NX: 2, DR: 0, SF: 0, TR: 2, CN: 0]
NSE: Script scanning 10.13.37.11.
NSE: Starting runlevel 1 (of 3) scan.
Initiating NSE at 03:34
Completed NSE at 03:34, 6.75s elapsed
NSE: Starting runlevel 2 (of 3) scan.
Initiating NSE at 03:34
Completed NSE at 03:34, 0.95s elapsed
NSE: Starting runlevel 3 (of 3) scan.
Initiating NSE at 03:34
Completed NSE at 03:34, 0.00s elapsed
Nmap scan report for 10.13.37.11
Host is up, received echo-reply ttl 63 (0.23s latency).
Scanned at 2021-11-16 03:33:43 EST for 51s
Not shown: 997 closed ports
Reason: 997 resets
PORT     STATE SERVICE REASON         VERSION
22/tcp   open  ssh     syn-ack ttl 63 OpenSSH 7.6p1 Ubuntu 4ubuntu0.3 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey: 
|   2048 0d:e4:41:fd:9f:a9:07:4d:25:b4:bd:5d:26:cc:4f:da (RSA)
| ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQCYsb2eP012xQGyABOzy+gWdxyHIa7xFBkwpLlFOBlYVsJp87Vtve02GudeSUjrz59c7y5nJkLxJAKQRXIObz/jzvCUkTMjH56Mc/3hzdkAzlWg/Gq3vNTyOLODkPPInJGGk1WgovnLcAJtNgdXaO7nYrDqyC8eCjBt7ppsONrz9FmEbiqLQl1m/LYb7Em6X1ZviytlJeH7eEk3UcKX45sNpzaUINdf1PJnXK3CLTB+vEAaieWz1GzCMsuRMphsmnW/d2ObpfZfCMa/NKYpAi0Z6yxUlI/HPEOWNnWO45OZ+7+M8NTxklZCHUbeCDhK8YSnpXtaEFPZvKajqZB+F2tR
|   256 f7:65:51:e0:39:37:2c:81:7f:b5:55:bd:63:9c:82:b5 (ECDSA)
| ecdsa-sha2-nistp256 AAAAE2VjZHNhLXNoYTItbmlzdHAyNTYAAAAIbmlzdHAyNTYAAABBBEKLumcSSQuW4qihcz0zZyca/KvBaXlysVAvY/DqLV0vo4bPoz+PH0qP7vuSlgCIqdiyJKq5JFfJz58e4kujk90=
|   256 28:61:d3:5a:b9:39:f2:5b:d7:10:5a:67:ee:81:a8:5e (ED25519)
|_ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAINAqCT5KghTKGzjImXygZG4vYKvk0akCYJaonX3hXvkE
80/tcp   open  http    syn-ack ttl 63 Apache httpd 2.4.29 ((Ubuntu))
|_http-favicon: Unknown favicon MD5: 6A6F2809F13E037DDC8D625B58FDA218
|_http-generator: WordPress 5.4-alpha-47225
| http-methods: 
|_  Supported Methods: GET HEAD POST OPTIONS
|_http-server-header: Apache/2.4.29 (Ubuntu)
|_http-title: Root of the Universe &#8211; by @lydericlefebvre &amp; @akerva_fr
|_https-redirect: ERROR: Script execution failed (use -d to debug)
5000/tcp open  http    syn-ack ttl 63 Werkzeug httpd 0.16.0 (Python 2.7.15+)
| http-auth: 
| HTTP/1.0 401 UNAUTHORIZED\x0D
|_  Basic realm=Authentication Required
| http-methods: 
|_  Supported Methods: HEAD OPTIONS GET
|_http-server-header: Werkzeug/0.16.0 Python/2.7.15+
|_http-title: Site doesn't have a title (text/html; charset=utf-8).
No exact OS matches for host (If you know what OS is running on it, see https://nmap.org/submit/ ).
TCP/IP fingerprint:
OS:SCAN(V=7.80%E=4%D=11/16%OT=22%CT=1%CU=34876%PV=Y%DS=2%DC=T%G=Y%TM=61936D
OS:1A%P=x86_64-pc-linux-gnu)SEQ(SP=104%GCD=1%ISR=109%TI=Z%CI=Z%II=I%TS=A)OP
OS:S(O1=M54DST11NW7%O2=M54DST11NW7%O3=M54DNNT11NW7%O4=M54DST11NW7%O5=M54DST
OS:11NW7%O6=M54DST11)WIN(W1=7120%W2=7120%W3=7120%W4=7120%W5=7120%W6=7120)EC
OS:N(R=Y%DF=Y%T=40%W=7210%O=M54DNNSNW7%CC=Y%Q=)T1(R=Y%DF=Y%T=40%S=O%A=S+%F=
OS:AS%RD=0%Q=)T2(R=N)T3(R=N)T4(R=Y%DF=Y%T=40%W=0%S=A%A=Z%F=R%O=%RD=0%Q=)T5(
OS:R=Y%DF=Y%T=40%W=0%S=Z%A=S+%F=AR%O=%RD=0%Q=)T6(R=Y%DF=Y%T=40%W=0%S=A%A=Z%
OS:F=R%O=%RD=0%Q=)T7(R=Y%DF=Y%T=40%W=0%S=Z%A=S+%F=AR%O=%RD=0%Q=)U1(R=Y%DF=N
OS:%T=40%IPL=164%UN=0%RIPL=G%RID=G%RIPCK=G%RUCK=G%RUD=G)IE(R=Y%DFI=N%T=40%C
OS:D=S)

Uptime guess: 7.726 days (since Mon Nov  8 10:09:21 2021)
Network Distance: 2 hops
TCP Sequence Prediction: Difficulty=260 (Good luck!)
IP ID Sequence Generation: All zeros
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel

TRACEROUTE (using port 1025/tcp)
HOP RTT       ADDRESS
1   229.45 ms 10.13.14.1
2   229.52 ms 10.13.37.11

NSE: Script Post-scanning.
NSE: Starting runlevel 1 (of 3) scan.
Initiating NSE at 03:34
Completed NSE at 03:34, 0.00s elapsed
NSE: Starting runlevel 2 (of 3) scan.
Initiating NSE at 03:34
Completed NSE at 03:34, 0.00s elapsed
NSE: Starting runlevel 3 (of 3) scan.
Initiating NSE at 03:34
Completed NSE at 03:34, 0.00s elapsed
Read data files from: /usr/bin/../share/nmap
OS and Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 52.32 seconds
           Raw packets sent: 1124 (53.482KB) | Rcvd: 1082 (46.774KB)
```
