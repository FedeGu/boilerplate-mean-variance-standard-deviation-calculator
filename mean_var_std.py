import numpy as np

def calculate(list):
    lista = np.array(list)
    arreglo = np.split(lista, 3)
    #arreglo_1 = np.array(arreglo).reshape(3, 3)
    
    media = np.mean(arreglo, axis=0).tolist(),np.mean(arreglo, axis=1).tolist(), np.mean(lista)
    variancion= np.var(arreglo, axis=0).tolist(), np.var(arreglo, axis=1).tolist(), np.var(lista)
    desv_standar= np.std(arreglo, axis=0).tolist(), np.std(arreglo, axis=1).tolist(), np.std(lista)
    maximo= np.max(arreglo, axis=0).tolist(), np.max(arreglo, axis=1).tolist(), np.max(lista)
    minimo= np.min(arreglo, axis=0).tolist(), np.min(arreglo, axis=1).tolist(), np.min(lista)
    suma= np.sum(arreglo, axis=0).tolist(), np.sum(arreglo, axis=1).tolist(), np.sum(lista)
    
    resultado = {'mean': media,
  'variance': variancion,
  'standard deviation': desv_standar,
  'max': maximo,
  'min': minimo,
  'sum': suma}
    
    return print(resultado)



    return calculations
