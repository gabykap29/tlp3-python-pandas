from funciones.analisis_estadistico import analisis_estadistico
#edades de 30 alumnos
edades = [18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29,21,22,30,22 ]
print (len(edades))


def main(lista_numeros):
    try:
        #lista 1 al 30
        print(analisis_estadistico(lista_numeros))
        
        if len(lista_numeros) == 0 or len(lista_numeros) < 30:
            print('Error: la lista debe tener 30 elementos')
            return  
    # Excepciones
    except ValueError as e:
        print(f'Error en main: {e}')
    except Exception as e:
        print(f'Error en main: {e}')

main(edades)