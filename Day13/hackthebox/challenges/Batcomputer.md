

```assembly
# file batcomputer | tr "," "\n" 
batcomputer: ELF 64-bit LSB pie executable
 x86-64
 version 1 (SYSV)
 dynamically linked
 interpreter /lib64/ld-linux-x86-64.so.2
 BuildID[sha1]=497abb33ba7b0370d501f173facc947759aa4e22
 for GNU/Linux 3.2.0
 stripped
```

```assembly
# checksec batcomputer           
[*] '/root/Downloads/hackthebox/challenge/batcomputer/batcomputer'
    Arch:     amd64-64-little
    RELRO:    Partial RELRO
    Stack:    No canary found
    NX:       NX disabled
    PIE:      PIE enabled
    RWX:      Has RWX segments
```


