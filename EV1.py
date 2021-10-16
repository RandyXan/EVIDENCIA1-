from collections import namedtuple
import datetime
import time

SEPARADOR = ("-" * 80)
SEPARADOR1 = ("_" * 80)
Articulo = namedtuple("Articulo", "articulo cantidad_articulo precio_articulo monto_venta") # Esta tupla se estara almacenando cada articulo que se desea registrar
Ticket = namedtuple("Ticket", "fecha articulos total iva ")  # En esta tupla se almacena un ticket con los datos la tupla de Articulo
registro_ventas = {} # Este diccionario se usara para almacenar las ventas

while True:
    print("--------Menu--------")
    print("1.AGREGAR VENTA")
    print("2.BUSQUEDA DE VENTA POR FOLIO")
    print("3.SALIR")
    opcion = int(input("SELECCIONA UNA OPCION: "))
    print(("-"*30))
    
    if opcion == 1:
        while True:
            print("-"*30)
            print("AGREGAR VENTA")
            folio = int(input("INGRESA EL FOLIO: "))
            if folio in registro_ventas.keys():
                print('!EL FOLIO INGRESADO YA EXISTE!')
            else:
                break
        fecha = datetime.date.today()
        articulos = {} #Este diccionario se utiliza para poder almacenar los articulos que se estaran agregando en cada venta por folio 
        subtotal = 0
        contador_articulo = 0 
        while True:
            contador_articulo += 1
            articulo = input('CUAL ES EL NOMBRE DEL ARTICULO?: ')
            cantidad_articulo = int(input('ESCRIBE LA CANTIDAD DE ARTICULOS: '))
            precio_articulo = float(input('CUANTO VALE CADA ARTICULO: '))
            monto_venta = cantidad_articulo * precio_articulo
            #Se agrega los datos del articulo con un tuplanominada al diccionario articulos 
            #con la variable contador_articulo para poder identificar cada articulo en la tupla
            articulos[contador_articulo] = Articulo(articulo, cantidad_articulo, precio_articulo, monto_venta)
            subtotal += monto_venta
            print(SEPARADOR1)
            print(f"SUBTOTAL DE VENTA HASTA EL MOMENTO: ${subtotal}")
            print(SEPARADOR1)
            respuesta = int(input("\nDESEAS CONTINUAR AGREGANDO ARTICULOS? 1[si], 2[no]: "))
            print(SEPARADOR)
            if respuesta != 1:
                print(f"FOLIO DE TICKET: |{folio}|")
                print(f'SUBTOTAL: ${subtotal}')
                iva = (subtotal*0.16)
                print(f'IVA(16%): ${iva}')
                total = (iva + subtotal)
                print(f'TOTAL: ${total}')
                #Agregar el ticket al registro de las ventas         
                registro_ventas[folio] = Ticket(fecha,articulos,total,iva)
                print(SEPARADOR1)
                break
    elif opcion == 2:
        print(SEPARADOR1)
        print("BUSQUEDA DE VENTA POR FOLIO")
        folio_a_buscar = int(input("INGRESA EL NUMERO DE FOLIO A BUSCAR: "))
        print(SEPARADOR1)
        if folio_a_buscar in registro_ventas.keys():
            print(f"\nFOLIO DE TICKET: |{folio_a_buscar}|")
            print(f'FECHA: {registro_ventas[folio_a_buscar].fecha}\n')
            print(f'PRODUCTOS')
            articulo_ticket = registro_ventas[folio_a_buscar].articulos
            for art in articulo_ticket.keys():
                print(f"{articulo_ticket[art].articulo} | {articulo_ticket[art].cantidad_articulo} X ${articulo_ticket[art].precio_articulo} | ${articulo_ticket[art].monto_venta}")
            print(f"IVA(16%): ${(registro_ventas[folio_a_buscar].iva)}")
            print(f'TOTAL: ${registro_ventas[folio_a_buscar].total}')
            print(SEPARADOR1)
        else:
            print("-"*30)
            print(f"EL NUMERO DE FOLIO: {folio_a_buscar}, NO ESTA REGISTRADO")
            print("-"*30)
    elif opcion == 3:
        break
    else:
        print("RESPUESTA NO VALIDA")