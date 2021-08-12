/*int funcion ---> es una funcion, retorna algo.
void ----> procedimiento, no retorna nada.

#include <stdio.h> -----> fundamental para que funcione todo programa
#include <stdbool.h> -----> importa la variabale bool



& es la direccion de memoria
* puntero

int num1 = 20;
int num2 = 30;

swap(&num1,&num2) ----> swap = int aux;
                        aux = *val1;
                        *val1 = *val2;
                        *val2 = aux; -------> los punbteros lo que hacen es hacer "mutables las variables". En C no exsiste la muabilidad y solo se puede retornar una cosa, no tuplas.
                        si yo no agrego punteros, esos cambios solo quedan dentro de la funcion.

*/