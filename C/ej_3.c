//b) Pedir al usuario que ingrese 10 numeros mostrar cuál fue el mayor y el menor ingresados
#include <stdio.h>
int main()
{       
    int i,n,maximo,sum=0;
    int minimo = 99999999;

    printf("Ingrese los 10 numeros : \n");

    for (i=1;i<=10;i++)
    {
        printf("Numero%d :",i);
        scanf("%d",&n);

        if (n > maximo){
            maximo = n;
        }
        if (minimo > n){
            minimo = n;
        }
        
    }
    printf("El maximo es : %d, y el minimo es: %d\n", maximo,minimo);

    return 0;
}