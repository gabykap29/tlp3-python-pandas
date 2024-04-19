from pandas import pandas as pd
from funciones.obtener_fi import obtener_fi

def analisis_estadistico(lista_numeros):
    
    try:
        #obtener fi
        fi = obtener_fi(lista_numeros)
        
        #crear dataframe
        df = pd.DataFrame(list(fi.items()), columns=['Numero', 'fi'], index=None)
        
        #calcular frecuencia acumulada
        df['Fi'] = df['fi'].cumsum()
        
        #calcular frecuencia relativa
        df['ri'] = df['fi'] / len(lista_numeros)
        
        #calcular frecuencia relativa acumulada
        df['ri'] = df['Fi'] / len(lista_numeros)
        
        #calcular porcentaje
        df['pi%'] = df['ri'] * 100
        
        #calcular porcentaje acumulado
        df['Pi%'] = df['ri'].cumsum()
    except Exception as e:
        print(f'Error en analisis_estadistico: {e}')
    return df

