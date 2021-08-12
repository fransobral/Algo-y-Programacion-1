/*
a) Pedir al usuario que ingrese números y mostrar su suma. Usar -1 como condición de corte.
*/

#include <stdio.h>

int main(){
    int numero = 0;
    int suma = 0;

    while (numero != -1){
        suma += numero;
        printf("Ingrese un número: ");
        scanf(" %d", &numero);
    }
    printf("El resultado de la suma es: %d\n", suma);
    

    


    return 0;
}