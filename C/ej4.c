#include <stdio.h> //printf()

typedef struct {
    int edad;
    char nombre[30];
    char genero[30];
} humano_t;

int main(){
	humano_t raul = {24, "Raul", "Masculino"};

	printf("%s\n", raul.nombre);
	return 0;
}