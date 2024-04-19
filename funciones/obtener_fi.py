def obtener_fi(lista_de_datos):
    try:
        lista_de_datos.sort()
        fi = {}
        for i in lista_de_datos:
            if i in fi:
                fi[i] += 1
            else:
                fi[i] = 1
                
    except Exception as e:
        print(f'Error en obtener_fi: {e}')
    return fi
