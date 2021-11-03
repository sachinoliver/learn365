




```assembly
~/Downloads/htb/challenges/batcomputer ❯ gdb ./batcomputer                                                                                                  2h 35m 1s root@oliver 11:33:53 AM
GNU gdb (Debian 10.1-2) 10.1.90.20210103-git
Copyright (C) 2021 Free Software Foundation, Inc.
License GPLv3+: GNU GPL version 3 or later <http://gnu.org/licenses/gpl.html>
This is free software: you are free to change and redistribute it.
There is NO WARRANTY, to the extent permitted by law.
Type "show copying" and "show warranty" for details.
This GDB was configured as "x86_64-linux-gnu".
Type "show configuration" for configuration details.
For bug reporting instructions, please see:
<https://www.gnu.org/software/gdb/bugs/>.
Find the GDB manual and other documentation resources online at:
    <http://www.gnu.org/software/gdb/documentation/>.

For help, type "help".
Type "apropos word" to search for commands related to "word"...
Reading symbols from ./batcomputer...
(No debugging symbols found in ./batcomputer)
gdb-peda$ r
Starting program: /root/Downloads/htb/challenges/batcomputer/batcomputer 
Welcome to your BatComputer, Batman. What would you like to do?
1. Track Joker
2. Chase Joker
> ^C
Program received signal SIGINT, Interrupt.
[----------------------------------registers-----------------------------------]
RAX: 0xfffffffffffffe00 
RBX: 0x7ffff7fa1980 --> 0xfbad208b 
RCX: 0x7ffff7ed1e8e (<__GI___libc_read+14>:	cmp    rax,0xfffffffffffff000)
RDX: 0x1 
RSI: 0x7ffff7fa1a03 --> 0xfa46800000000000 
RDI: 0x0 
RBP: 0x7ffff7fa34a0 --> 0x0 
RSP: 0x7fffffffd618 --> 0x7ffff7e6489a (<_IO_new_file_underflow+378>:	test   rax,rax)
RIP: 0x7ffff7ed1e8e (<__GI___libc_read+14>:	cmp    rax,0xfffffffffffff000)
R8 : 0x0 
R9 : 0xffffffffffffff80 
R10: 0x555555556069 --> 0x4900000000006425 ('%d')
R11: 0x246 
R12: 0x7ffff7fa26a0 --> 0xfbad2887 
R13: 0x7ffff7fa28a0 --> 0x0 
R14: 0xd68 ('h\r')
R15: 0x7ffff7fa3608 --> 0x7ffff7e66630 (<_IO_cleanup>:	push   r15)
EFLAGS: 0x246 (carry PARITY adjust ZERO sign trap INTERRUPT direction overflow)
[-------------------------------------code-------------------------------------]
   0x7ffff7ed1e88 <__GI___libc_read+8>:	test   eax,eax
   0x7ffff7ed1e8a <__GI___libc_read+10>:	jne    0x7ffff7ed1ea0 <__GI___libc_read+32>
   0x7ffff7ed1e8c <__GI___libc_read+12>:	syscall 
=> 0x7ffff7ed1e8e <__GI___libc_read+14>:	cmp    rax,0xfffffffffffff000
   0x7ffff7ed1e94 <__GI___libc_read+20>:	ja     0x7ffff7ed1ef0 <__GI___libc_read+112>
   0x7ffff7ed1e96 <__GI___libc_read+22>:	ret    
   0x7ffff7ed1e97 <__GI___libc_read+23>:	nop    WORD PTR [rax+rax*1+0x0]
   0x7ffff7ed1ea0 <__GI___libc_read+32>:	sub    rsp,0x28
[------------------------------------stack-------------------------------------]
0000| 0x7fffffffd618 --> 0x7ffff7e6489a (<_IO_new_file_underflow+378>:	test   rax,rax)
0008| 0x7fffffffd620 --> 0x0 
0016| 0x7fffffffd628 --> 0x200010000 
0024| 0x7fffffffd630 --> 0x7ffff7fa8508 --> 0x7ffff7fa8000 --> 0x7ffff7de3000 --> 0x3010102464c457f 
0032| 0x7fffffffd638 --> 0x7ffff7fa1980 --> 0xfbad208b 
0040| 0x7fffffffd640 --> 0x7ffff7fa34a0 --> 0x0 
0048| 0x7fffffffd648 --> 0x0 
0056| 0x7fffffffd650 --> 0x7ffff7fa24a0 --> 0x7ffff7f9e6a0 --> 0x7ffff7f6eb6e --> 0x636d656d5f5f0043 ('C')
[------------------------------------------------------------------------------]
Legend: code, data, rodata, value
Stopped reason: SIGINT
0x00007ffff7ed1e8e in __GI___libc_read (fd=0x0, buf=0x7ffff7fa1a03 <_IO_2_1_stdin_+131>, nbytes=0x1) at ../sysdeps/unix/sysv/linux/read.c:26
26	../sysdeps/unix/sysv/linux/read.c: No such file or directory.
gdb-peda$ 
```

