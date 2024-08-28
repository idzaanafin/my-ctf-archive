#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <signal.h>

char flag[16];

void nuller(){
    setvbuf(stdin, 0, 2, 0);
    setvbuf(stdout, 0, 2, 0);
    setvbuf(stderr, 0, 2, 0);
    alarm(120);
}

void sigsegv_handler(){
    printf("Here's your reward: %s\n", flag);
    fflush(stdout);
    exit(1);
}

void vuln(char *input){
    char buff[0x156E2];
    strcpy(buff, input);
    gets(buff); 
}

int main(){
    FILE *f = fopen("flag.txt","r");
    if (f == NULL) {
        printf("Sorry, tapi disini gak ada flagnya \n");
        exit(0);
    }

    fgets(flag, 64, f);
    signal(SIGSEGV, sigsegv_handler);

    printf("-> ");
    fflush(stdout);
    char bof[0x156E2];
    vuln(bof);
    printf("exiting program... \n");

    return 0;
}