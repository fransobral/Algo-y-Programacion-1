/*
Implementar la función unsigned int strlen(const char *s) que devuelve la
longitud de la cadena s (sin contar el último caracter '\0'). La función se puede escribir estar en forma iterativa o recursiva.*/

//#include "main.h" // No borrar esto!
#include <stdio.h>
#include <string.h>

// DOC: Completar
unsigned int strlen(const char *s) {
    unsigned int contador = 0;

    while ((s[contador]) != ("/0")){
        contador += 1;
    }

    return contador;
}

int main(){
    const char s[] = {"a","b","c","/0"};
    strlen(s);
    return 0;
}