/*Usando las funciones printf y sizeof, escribir un programa que imprima el
tamaño en bytes de cada uno de los siguientes tipos: bool, char, short, int, long, float, double,
bool*, char*, short*, int*, long*, float*, double*.

El programa debe mostrar la información con el siguiente formato:

bool: 1
char: 1
short: 2
. . .*/

#include <stdio.h>
#include <stdbool.h>

int main() {
    printf("bool: %lu\n", sizeof(bool));
    printf("char: %lu\n", sizeof(char));
    printf("short: %lu\n", sizeof(short));
    printf("int: %lu\n", sizeof(int));
    printf("long: %lu\n", sizeof(long));
    printf("float: %lu\n", sizeof(float));
    printf("double: %lu\n", sizeof(double));
    printf("bool*: %lu\n", sizeof(bool*));
    printf("char*: %lu\n", sizeof(char*));
    printf("short*: %lu\n", sizeof(short*));
    printf("int*: %lu\n", sizeof(int*));
    printf("long*: %lu\n", sizeof(long*));
    printf("float*: %lu\n", sizeof(float*));
    printf("double*: %lu", sizeof(double*));

    return 0;
}