def ingresoDeEstados(estados_iniciales):
    """
    Ingreso de Estados Iniciales de

    Parametro
    ------------------------------
    estados Iniciales: estados_iniciales

    Retorna
    ------------------------------ 
    estados a tratas ingresados por el usuario:estadosATratar
    """
    #creacion de estado a tratar
    esatadosATratar={}
    #Recorremos 
    for clave in estados_iniciales:
        #ingreso de estado
        estado=input('Ingrese 1 si esta abierta la via {} o 0 si esta cerrada:\n'.format(clave))
        #Validacion de la entrada de datos 
        if int(estado)==1 or int(estado)==0:
            #ingreso de estado al diccionario
            esatadosATratar[clave]=int(estado)
        else:
            #Si la opcion no pertenece al sistema, ingresaremos  como si estuviera cerrada la via
            print('Estado no correcto lo marcaremos como cerrado\n')
            #ingreso de estado defaul
            esatadosATratar[clave]=0
    #Retorna el estados a tratar
    return esatadosATratar

def agenteInteligente(estadosIniciales,estados):
    """
    Funcion que permite calcular la logica de estados

    Parametros
    -------------------------------
    Estados Inciales
    Estados a tratar

    Retorna
    --------------------------
    no retorna nada
    """
    #Costo que tendra al realizar la accion
    costo=0
    #recorrido de nuestros estados a tratar
    for clave in estados:
        #si el estado  es igual al estado objetivo no combiamos el estado
        if estados[clave]==estadosIniciales[clave]:
            #Si cumple lo anterior el costo no incrementa
            costo=costo
        else:
            #estado de clave igual a 1 se actualiza a 0
            if estados[clave]==1:
                #actualizacion del estado en la ciudad 
                estados[clave]=0 
            #caso contrario entramos a la siguiente condicion
            else:
                #estado de clave igual a 0 va a 1
                estados[clave]=1
            #Si cambia alguno de los estados incrementamos el costo
            costo+=1
    #mostramos la informacion del costo que ocupo para realizar la accion
    print('Costo es ',costo)
    #Mostramos el estado solucion 
    print('Esatado Solucion',str(estados))

if __name__=='__main__':
    #Ingreso de estados objetivo
    estado_inciales={'Quito':1,'Chone':0, 'Lorena': 1, 'Pilaton':0}
    #Ingreso de estado que se van a tratar
    estados=ingresoDeEstados(estado_inciales)
    #imprimos el los estados a tratar
    print('Estados a tratar:',estados)
    #imprimimos los estados objetivos al que debe llegar mi estados a tratar
    print('Estados Objetivos:',estado_inciales)
    #nuestro agente inteligente realiza los cambios de estados  
    agenteInteligente(estado_inciales,estados)