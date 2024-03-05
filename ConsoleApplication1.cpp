// ConsoleApplication1.cpp : Este archivo contiene la función "main". La ejecución del programa comienza y termina ahí.
//

#include <iostream>
#include "Estudiante.h"
#include <iostream>
#include <string>
using namespace std;
int main()
{
    Estudiante alumno;
    string nombre;
    cout << "Ingrese su nombre: ";
    getline(cin, nombre);
    alumno.set_nombre(nombre);
    cout << "El nombre del estudiante es: " << alumno.get_nombre() << endl;
    return 0;
}

