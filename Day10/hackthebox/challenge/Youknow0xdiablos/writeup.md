





```assembly
[0x080492b1]> pdf
            ; DATA XREFS from entry0 @ 0x80490f6, 0x80490fc
┌ 118: int main (char **argv);
│           ; var int32_t var_ch @ ebp-0xc
│           ; var int32_t var_8h @ ebp-0x8
│           ; arg char **argv @ esp+0x34
│           0x080492b1 b    8d4c2404       lea ecx, [argv]
│           0x080492b5      83e4f0         and esp, 0xfffffff0
│           0x080492b8      ff71fc         push dword [ecx - 4]
│           0x080492bb      55             push ebp
│           0x080492bc      89e5           mov ebp, esp
│           0x080492be      53             push ebx
│           0x080492bf      51             push ecx
│           0x080492c0      83ec10         sub esp, 0x10
│           0x080492c3      e858feffff     call sym.__x86.get_pc_thunk.bx
│           0x080492c8      81c3382d0000   add ebx, 0x2d38
│           0x080492ce      8b83fcffffff   mov eax, dword [ebx - 4]
│           0x080492d4      8b00           mov eax, dword [eax]
│           0x080492d6      6a00           push 0
│           0x080492d8      6a02           push 2                      ; 2
│           0x080492da      6a00           push 0                      ; char *buf
│           0x080492dc      50             push eax                    ; FILE*stream
│           0x080492dd      e8befdffff     call sym.imp.setvbuf        ; int setvbuf(FILE*stream, char *buf, int mode, size_t size)
│           0x080492e2      83c410         add esp, 0x10
│           0x080492e5      e876fdffff     call sym.imp.getegid
│           0x080492ea      8945f4         mov dword [var_ch], eax
│           0x080492ed      83ec04         sub esp, 4
│           0x080492f0      ff75f4         push dword [var_ch]
│           0x080492f3      ff75f4         push dword [var_ch]
│           0x080492f6      ff75f4         push dword [var_ch]
│           0x080492f9      e8c2fdffff     call sym.imp.setresgid
│           0x080492fe      83c410         add esp, 0x10
│           0x08049301      83ec0c         sub esp, 0xc
│           0x08049304      8d8338e0ffff   lea eax, [ebx - 0x1fc8]
│           0x0804930a      50             push eax                    ; const char *s
│           0x0804930b      e860fdffff     call sym.imp.puts           ; int puts(const char *s)
│           0x08049310      83c410         add esp, 0x10
│           0x08049313      e85affffff     call sym.vuln
│           0x08049318      b800000000     mov eax, 0
│           0x0804931d      8d65f8         lea esp, [var_8h]
│           0x08049320      59             pop ecx
│           0x08049321      5b             pop ebx
│           0x08049322      5d             pop ebp
│           0x08049323      8d61fc         lea esp, [ecx - 4]
└           0x08049326      c3             ret
[0x080492b1]> 
```
