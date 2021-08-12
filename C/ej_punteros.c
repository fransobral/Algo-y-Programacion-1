//crear un procedimiento que sume los numeros ingresados por el usuraio (los almacena usando un puntero) y luego haga un print con la suma en el main.

#include <stdio.h>

void sumatoria(int *suma){
    int numero = 0;
    while (numero != -1){
        *suma += numero;
        printf("Ingrese un numero: ");
        scanf(" %d", &numero);
    }
}

void main(){       
    
    int suma = 0;
    sumatoria(&suma);
    
    printf("El resultado de la suma es: %d\n", suma);
}

