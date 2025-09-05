import random as rn 
def descuento_auto():
       descuento = 0
       des = int(input("¿Desea participar de un juego para conseguir un descuento del 20% para la compra de su auto? Ingrese 1 si quiere y 2 si no quiere. "))
       while des != 1 and des != 2:
              des = int(input("Su respuesta es incorrecta. Ingrese 1 si quiere participar y 2 si no quiere. "))
       if des == 2: 
              print("Como usted desee, aqui tiene la lista de autos con los que contamos")
       else: 
              print("Nos alegra que haya querido participar. El juego trata de que tiene que elegir un numero del 1 al 5, si su numero es igual al que eligio el programa usted se gana el descuento asi de facil.")
              ran = rn.randint(1,5)
              numran = int(input("Ingrese un numero del 1 al 5: "))
              while numran < 1 or numran > 5:
                     numran = int(input("Su numero es incorrecto, ingrese un numero entre 1 y 5: "))
              if numran != ran:
                    print("Lo lamentamos, pero su numero no coincide, el numero correcto era:", ran)
              else:
                    print("¡Felicitaciones! Su numero coicide, usted se gano un descuento del 20%.")
                    descuento += 1
       return descuento

