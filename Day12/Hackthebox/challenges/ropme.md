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

```assembly
└─# ltrace ./ropme
__libc_start_main(0x400626, 1, 0x7ffce8bd0308, 0x400670 <unfinished ...>
puts("ROP me outside, how 'about dah?"ROP me outside, how 'about dah?
)                                 = 32
fflush(0x7f20042246c0)                                                  = 0
fgets(test
"test\n", 500, 0x7f20042239a0)                                    = 0x7ffce8bd01d0
+++ exited (status 0) +++
```
![image](https://user-images.githubusercontent.com/63084488/140326994-0e7e776f-f1d0-4259-a40f-024bbe7580d4.png)
