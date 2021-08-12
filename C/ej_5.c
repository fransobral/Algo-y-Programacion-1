//Escribir una función que reciba un arreglo de números y la cantidad de elementos, y devuelva el promedio.
#include <stdio.h>

float promedio(float numeros[], int n) {
    int i = 0;
    float total = 0;

    for (i;i<=n-1;i++){
            total += numeros[i];
        }
    float promedios = (total/n);
    return promedios;
}

int main(){
    float numeros[4] = {10,20,5,30};
    int cant = 4;
    float promediox = promedio(numeros,cant);
    printf("El promedio es de %f.\n",promediox);

    return 0;
}