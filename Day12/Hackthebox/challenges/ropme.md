```assembly
└─# file ropme | tr "," "\n"
ropme: ELF 64-bit LSB executable
 x86-64
 version 1 (SYSV)
 dynamically linked
 interpreter /lib64/ld-linux-x86-64.so.2
 for GNU/Linux 2.6.32
 BuildID[sha1]=e30ea7fd405c5104fd0d97dc464c513b05005fdb
 not stripped
```


```assembly
└─# checksec ropme  
[*] '/root/Downloads/hackthebox/challenge/ropme/ropme'
    Arch:     amd64-64-little
    RELRO:    Partial RELRO
    Stack:    No canary found
    NX:       NX enabled
    PIE:      No PIE (0x400000)
```
