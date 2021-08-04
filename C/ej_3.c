#include <stdio.h>
void main()
{       
    int i,n,sum=0;
    printf("Ingrese los 10 numeros : \n");
    for (i=1;i<=10;i++)
    {
        printf("Numero-%d :",i);
        scanf("%d",&n);
        sum +=n;
    }
    printf("La suma de los 10 numeros es : %d\n", sum);
}