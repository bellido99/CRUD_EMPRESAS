import os
from time import sleep

# EJERCIO FINAL MODULO 1 - CRUD EMPRESAS
# NOMBRE : DAVID BELLIDO MELENDEZ

dic_empresas = {
    '20454545':{
        'razon_social': 'EMPRESA SAC',
        'direccion':'CALLE EL SOL 123',
    }
}

ANCHO = 50

while(True):
    os.system("clear")
    print("="*ANCHO)
    print(" " * 10 + "GESTIÓN DE EMPRESAS")
    print("="*ANCHO)
    print("""
         [1] REGISTRAR EMPRESA
         [2] MOSTRAR EMPRESAS
         [3] ACTUALIZAR EMPRESA
         [4] ELIMINAR EMPRESA
         [5] SALIR
          """)
    print("=" * ANCHO)
    opcion = int(input("INGRESE OPCION : "))
    os.system("clear")
    if opcion == 1:
        print("=" * ANCHO)
        print(" " * 10 + "REGISTRAR EMPRESA")
        print("=" * ANCHO)
        #integramos a la nueva empresa
        ruc = input("INGRESE RUC DE LA EMPRESA: ")
        razon_social = input("INGRESE NOMBRE DE LA EMPRESA: ")
        direccion = input("INGRESE DIRECCION DE LA EMPRESA: ")
        #CREAMOS EL DICCIONARIO DE LA NUEVA EMPRESA
        nueva_empresa = {
            "razon_social": razon_social,
            "direccion": direccion
        }
        dic_empresas[ruc] = nueva_empresa
    if opcion == 2:
        print("=" * ANCHO)
        print(" " * 10 + "MOSTRAR EMPRESAS")
        print("=" * ANCHO)
        for ruc,info in dic_empresas.items():
            print(f"RUC : {ruc}")
            print(f"Razon : {info["razon_social"]}")
            print(f"DIRECCION : {INFO[direccion]}")
            print("*"*ANCHO)
       
    if opcion == 3:
        print("=" * ANCHO)
        print(" " * 10 + "ACTUALIZAR EMPRESA")
        print("=" * ANCHO)
        #PEDIMOS EL RUC DE LA EMPRESA A ACTUALIZAR
        ruc = input("INGRESE RUC DE LA EMPRESA A ACTUALIZAR :")
        if ruc in dic_empresas:
            print(f"Empresa encontrada: {dic_empresas[ruc]["razon_social"]}")
            nueva_empresa = input("INGRESE NUEVO NOMBRE (dejar en blanco para no cambiar): ")
            nueva_direccion = input("INGRESE NUEVA DIRECCION (dejar en blanco para no cambiar): ")
            if nueva_empresa:
                dic_empresas[ruc]["razon_social"] = nueva_empresa
            if nueva_direccion:
                dic_empresas[ruc]["direccion"] =nueva_direccion
            print("Empresa actualizada exitosamente.")
        else:
            print("No se encontro la empresa con ese RUC.")
    if opcion == 4:
        print("=" * ANCHO)
        print(" " * 10 + "ELIMINAR EMPRESA")
        print("=" * ANCHO)
        ruc = input("INGRESE EL RUC DE LA EMPRESA A ACTUALIZAR :")
        if dni in dic_empresas:
            del dic_empresas[ruc]
            print("EMPRESA ELIMINADA EXITOSAMENTE.")
        else:
            print("NO SE ENCONTRÓ LA EMPRESA CON ESE RUC.")
    if opcion == 5:
        print("=" * ANCHO)
        print(" " * 10 + "SALIENDO DEL SISTEMA...")
        print("=" * ANCHO)
        sleep(2)
        break
    
    input("Presione ENTER para continuar...")