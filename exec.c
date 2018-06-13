//compiled with gcc test.c -o test -z execstack -fno-stack-protector -no-pie -m32

int main(int argc, char *argv[])
{
char *shellcode = argv[1];
(*(void (*)()) shellcode)();
}
