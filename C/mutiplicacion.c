/*multiplicar dos numeros sin usar el signo*/
#include <stdio.h>

int main(){

    int numero1,numero2,i;
    int multiplicacion = 0;


    printf("Ingrese un número: ");
    scanf(" %d", &numero1);
    printf("Ingrese otro número: ");
    scanf(" %d", &numero2);

    for (i=1;i<=numero2;i++)
    {
        multiplicacion += numero1;
        }
        
    
    printf("El resultado de la multiplicacion es: %d\n", multiplicacion);

    return 0;
    }