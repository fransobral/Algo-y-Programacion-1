int main()
{
    int entrada = 0; // <- Variables de tipo int.
    int suma = 0; // <- Variables de tipo int.
    
    printf("Ingrese un número: ");
    scanf(" %d", &entrada);
    
    while ( entrada > 0 ){
        suma += entrada;
        printf("Ingrese un número: ");
        scanf(" %d", &entrada);
    }
    
    printf("El resultado de la suma es: %d\n", suma);
    
    return 0;
}