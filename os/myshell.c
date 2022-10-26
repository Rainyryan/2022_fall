#include<stdio.h>
#include<string.h>
#include<stdlib.h>
// #include<unistd.h>
// #include<sys/types.h>
// #include<sys/wait.h>
#include<readline/readline.h>
#include<readline/history.h>

#define clear() printf("\033[H\033[J")

int read_input(char *str){
    char *buffer;
    buffer = readline("\n(⁎˃ᆺ ˂)> ");
	if(strlen(buffer) != 0) {
		strcpy(str, buffer);
		return 0;
	}else
		return 1;
}

int parse_spaces(char *in, char **out){
    *out = strtok(in, " ");
    while(*out != NULL){
        out++;
        *out = strtok(NULL, " ");
    }
    return 0;
}

int main(){
    char input_str[1000], *parsed_input[100];
    
    while(1){
        read_input(input_str);
        parse_spaces(input_str, parsed_input);
        // for(int i = 0; parsed_input[i] != NULL; i++) printf("%s\n", parsed_input[i]);
        
    }
}