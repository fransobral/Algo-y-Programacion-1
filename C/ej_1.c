#include <stdio.h>

const int NUMERO_NUEVO = 20;
// 3)

void modificador(int* puntero_a_int) {
    *puntero_a_int = NUMERO_NUEVO;
}
// 0x7ffde69559fc --> Direcciones de memoria en base 16 (hexadecimal)
// 0x7ffefb36e9dc

int main() {
    // 1)
    int numero = 10;
    // 2)
    int* puntero;
    puntero = &numero;
    // int* puntero = &numero; es lo mismo q lo de arriba
    printf("El valor del numero es: %d \n", numero);
    // 4)
    modificador(&numero);
    printf("El numero ahora vale: %d \n", numero);
    // 5)
    modificador(puntero);
    printf("La direccion de memoria a la que APUNTA el puntero ahora contiene al numero: %d \n", *puntero);
    printf("El numero ahora vale: %d \n", numero);
    // Bonus(?)
    printf("La direccion de memoria que ALMACENA el puntero es: %p \n", puntero);
    printf("La direccion de memoria DEL puntero es: %p \n", &puntero);
    return 0;
}