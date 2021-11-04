
If you first create an account the pointer used for dynamic memory allocation will point at the end of the chunk.
If you delete it, then the pointer, instead of being set to null continues to refer to the now-freed memory, the result is a dangling pointer.


How UAF occurs

UAF vulnerabilities stem from the mechanism of dynamic memory allocation. Unlike the stack, dynamic memory (also known as the heap) is designed to store large amounts of data. Programmers can allocate blocks of arbitrary size in it, which tasks within a program can then either modify or free and return to the heap for subsequent use by other tasks in the same program.

Because dynamic memory is reallocated repeatedly, programs need to check constantly which sections of the heap are free and which are occupied. Here, headers help by referencing allocated memory areas. Each header contains the starting address of the corresponding block. UAF bugs arise when programs do not manage these headers properly.

Here’s how it happens. Pointers in a program refer to data sets in dynamic memory. If a data set is deleted or moved to another block but the pointer, instead of being cleared (set to null), continues to refer to the now-freed memory, the result is a dangling pointer. If the program then allocates this same chunk of memory to another object (for example, data entered by an attacker), the dangling pointer will now reference this new data set. In other words, UAF vulnerabilities allow for code substitution.

Potential consequences of UAF exploitation include:

    Data corruption,
    Program crashes,
    Arbitrary code execution.

Exploiting UAFs

An attacker can use UAFs to pass arbitrary code — or a reference to it — to a program and navigate to the beginning of the code by using a dangling pointer. In this way, execution of the malicious code can allow the cybercriminal to gain control over a victim’s system.

For example, to exploit the UAF vulnerability checkm8 in some iOS devices an attacker can initiate a USB-based update of the device firmware, and then instead of the firmware image, send a command to the device to exit DFU (Device Firmware Update) recovery mode. When the system tries to restart in this mode to terminate the aborted session, the attacker can pass arbitrary code to the device and execute it at the address of the buffer that was allocated before exiting and whose pointer was not cleared.


```assembly

```
