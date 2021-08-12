/*Escribir una función que reciba un número entero n y calcule el factorial de n. La función se puede escribir estar en forma iterativa o recursiva.*/
#include <stdio.h>

int factorial(int numero_entero){
    int i = 0;
    int factorial = 1;

    for (i=1;i< numero_entero;i++) {
        factorial = factorial*(i+1);
    }
    return factorial;
}

int main(){
    int numero_entero;
    
    printf("Ingrese su numero entero: ");
    scanf(" %d",&numero_entero);

    int num_factorial = factorial(numero_entero);

    printf("EL factorial de %d es %d\n",numero_entero,num_factorial);

    return 0;
}