/*compiled with 
gcc exec.c -o exec -z execstack -fno-stack-protector -no-pie -m32
*/
#include<stdio.h>
#include<string.h>
int main(int argc, char *argv[])
{
	if (argc == 2){
		char *shellcode = argv[1];
		printf("The length of shellcode is %d\n",strlen(shellcode));
		//scanf("%*c");
		(*(void (*)()) shellcode)();
		}
	else{
	printf("Please pass shellcode in the arguments\n");
	}
}
