import base64
import os

def pedirNumeroEntero():
 
    correcto=False
    num=0
    while(not correcto):
        try:
            num = int(input("Elije una opcion del menu: "))
            correcto=True
        except ValueError:
            print('Elije una opcion que este en el menu')
    return num
    


def menu():
    logo()
    salir = False
    opcion = 0
    
    while not salir:
    
        print ("1. Codificar")
        print ("2. Decodificar")
        print ("3. Salir")
       

        opcion = pedirNumeroEntero()
    
        if opcion == 1:
            os.system("clear")
            codificar()
            #print ("Opcion 1")
        elif opcion == 2:
            os.system("clear")
            decodificar()
            #print ("Opcion 2")
        elif opcion == 3:
            os.system("clear")
            salir = True
        
        else:
            print ("Introduce una opcion que este en el menu")
     
def codificar():
    salir = False
    opcion = 0
    
    while not salir:
    
        print ("1. Texto plano")
        print ("2. Codificado personalizado")
        print ("3. Menu")
        print ("4. Salir")

        opcion = pedirNumeroEntero()
    
        if opcion == 1:
            os.system("clear")
            accion_codificar()
            #print ("Opcion 1")
        elif opcion == 2:
            os.system("clear")
            codificado_perso()
            #print ("Opcion 2")
        elif opcion == 3:
            os.system("clear")
            menu()
            #print("Opcion 3")
        elif opcion == 4:
            os.system("clear")
            exit()
        else:
            print ("Introduce una opcion que este en el menu")

def accion_codificar():
    try:
        texto_original = ""
        texto_original = input("Introduce el texo que deseas codificar: ")
    except ValueError:
        print('Escribe un texto valido')

    texto_codificado = base64.b64encode(texto_original.encode()).decode()
    #return texto_codificado
    print (texto_codificado)

def decodificar():
    salir = False
    opcion = 0
    
    while not salir:
    
        print ("1. Texto plano")
        print ("2. Decodificado personalizado")
        print ("3. Menu")
        print ("4. Salir")

        opcion = pedirNumeroEntero()
    
        if opcion == 1:
            os.system("clear")
            accion_decodificar()
            #print ("Opcion 1")
        elif opcion == 2:
            os.system("clear")
            decodificado_perso()
            #print ("Opcion 2")
        elif opcion == 3:
            os.system("clear")
            menu()
            #print("Opcion 3")
        elif opcion == 4:
            os.system("clear")
            exit()
            
        else:
            print ("Introduce una opcion que este en el menu")

def accion_decodificar():
    try:
        texto_original = ""
        texto_original = input("Introduce el texo que deseas decodificar: ")
    except ValueError:
        print('Escribe un texto valido')

    texto_decodificado = base64.b64decode(texto_original).decode('utf-8')
    #return texto_codificado
    print (texto_decodificado)

#VER SI PUEDO MEJORAR LAS FUNCIONES PASANDO PARAMETROS EN ELLAS
#AGREGAR MAS CODIFICADORES APARTE DEL BASE64
def codificado_perso():
   
    correcto = False
    num = 0
    texto_original = ""
    while(not correcto):
        try:
            num =int(input("¿Cuantas veces deseas codificar en base64?: "))
            parseo_num = str(num)
            texto_original = input("Que texto desea codificar " + parseo_num + " veces: ")
            correcto =True 
        except ValueError:
            print('Introduce un numero entero')
            return num
        

    
    for _ in range(num):
        
        texto_codificado = base64.b64encode(texto_original.encode()).decode()  
        texto_original = texto_codificado  
        
    print("Tu texto codificado " + parseo_num + " veces es: " + texto_codificado)

def decodificado_perso():
    correcto = False
    num = 0
    texto_original = ""
    while(not correcto):
        try:
            num =int(input("¿Cuantas veces deseas decodificar en base64?: "))
            parseo_num = str(num)
            texto_original = input("Que texto desea decodificar " + parseo_num + " veces: ")
            correcto =True 
        except ValueError:
            print('Introduce un numero entero')
            return num
        

    
    for _ in range(num):
        texto_decodificado = base64.b64decode(texto_original).decode('utf-8') 
        texto_original = texto_decodificado  
        
    print("Tu texto decodificado es: "  + texto_decodificado)

def logo():
    logo = """
    @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%###%@@@@@@@@@@@@@
    @@@@@@@@@@@@@@@%@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%@%%+-:...::=%%@@@@@@@@@@
    @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%%%%%@@@%+:.......:*@@@@@@@@@@@@
    @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%%%+=-:-+@@@@@%+:...-=-::+%@@@@@@@@@@@@
    @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%%#*#%%@@%*:...:=#@@@@#-...:=#%%%@@@@@@@@@@@@@@
    @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%%%%%#-:..-*%%%%#=.....-+@@%@#-......::-=#@@@@@@@@@@@@
    @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%%%#=-::=#@@*:...-*%%%%*:..:..:=#@@@#=..........-*@@@@@@@@@@@
    @@@@@@@@@@@@@@@@@@@@@@@@%@@@@@@@%####%%@@%*....=#@%*:...-*%%%%+..:=...-+@@@@#+-:.......:+@@@@@@@@@@@
    @@@@@@@@@@@@@@@@@@@@@@%%%%%%%*-:...::=*@@%*....=#%%*:...-*%%%#:..-*:..:=%@%%%%#%%#+:...:+@@@@@@@@@@@
    @@@@@@@@@@@@@@@@@@%@%%%%%%%+:........:=%@%*....=#%%*:...-*%%%+...-*-...-+%%%*:::---....-#@@@@@@@@@@@
    @@@@@@@@@@@@%#+=-:=%%#%%%#=....:=-:.:+%%%%*....=#@%*:...-*###-...:.....:=%@#-........:=#@@@@@@@@@@@@
    @@@@@@@@@@@%#-....-*%%%%#=...:=%%%#*%@@@@%*....=#%#*:...=#%%*.....:::...-+%*:.....:-+#@@@@@@@@@@@@@@
    @@@@@@@@@@@%*:....:+%###*:...=#%@%#*+=-=%%*....-*%#+...:+%%#=...-*@#=...:=%@%%###%@@@@@@@@@@@@@@@@@@
    @@@@@@@@@@%#=..:...-*%%#=...:=%%+.....:=#%*:...:=*=:...-#@%*:..:=%@%*=+*#%@@@@@@@@@@@@%#*+=---+#@@@@
    @@@@@@@@@@%*:..=:..:=%%#=...:=#%+.:...:=%%#=..........-#@@%=:-=+#@@@@@@@@@@@@@@%@@%+-:........:-*@@@
    @@@@@@@@@@#=..:*-...-*##+....-+%%*-...:=@@%#-.......:+%@@@%%@@@@@@@@@@@@%#*+=-:=%@#=...........:=#@@
    @@@@@@@@@@#:..:*+...:+%%*:....::-:....:=@@@@%*===+*#@@@@@@@@@%%%%%%#+=-:......:=%@#=....-+*-....-*@@
    @@@@@@@@@%+...::.....-#%%*:.......::..:+@@@@@@@@@@@@@@@@@%%##%%%%%#=..........-+%%#=....=##+....-#@@
    @@@@@@@@@#-.....::...:+%%%#=:...:=***#%@@@@@@@@@@@@%*+=-::..:-*%%%#=....:=+*#%%%%%#=....=*+:...:+%@@
    @@@@@@@@%+...:+%%+....-#%@@%%%%%@@@@%%%%%%%%###@@%*...........-+%%#=....=#%%#*#@@@#=..........:=%@@@
    @@@@@@@@#-...-#@%#-=+*#%@@@@@@@@%%%%%%%%#-::.-+%%%+.....::....:=#%#=....:-:..:=%@@#=..........-*@@@@
    @@@@@@@%*::-=*@@@@@@@@@@@%@%%%%*+=--=%%%*....-+%%#+....-+#-....=*%#=.........:=%%@#=....:-....:-*@@@
    @@@@@@@%%%@@@@@@@@@@@@%#**#%%%#....:=%%#*....-+%%%+....-+#-...:=%%#=....::-=+#%%%%#=....=*-....:=#@@
    @@@@@@@@@@@@@@@@%%%%#-...:=*%%#....:=%%%*....-+@%%+....:--....-*%%#=....=#@@@@%%%@#=....=#*:....:=%@
    @@@@@@@@%#*+==++#%%%#-....:-+%#....:=%@%*....-+%%%+..........-*%@@#=....-++=-::=%@#=....=#%*-==+#%@@
    @@@@@%#=:.......-#%%#-.....:-+#....:=%%%*....-+%%#+.......:-+%@@@@#=..........:=%@#=::=+#%@@@@@@@@@@
    @@@@%+:........-*@@@#-.......-#....:=%%%*....-+%%%+....:=#%@@@@@@@#=.........:-*%@%%@@@@@@@@@@@@@@@@
    @@@%*:...:=+=--*%@@%#-........-....:=%%%*....-+@@%+....-*@@@@@@@@@#=..:-=+*#%@@@@@@@@@@@@@@@@@@@@@@@
    @@@#=....-+##%%%%%%@#-...::........:=@@%*....-+@@%+....-*@@@@@@@@@%##%@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
    @@@#=.......:::=*%%%#-...:*-.......:=@%%*....-+@@%+....-*@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
    @@@#+...........-+@%#-...:=*=......:+@@%*....-+@@%*=+*#%@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
    @@@@#+-:........:=%%#-...:=%#+:....:+@@%*.:-=*#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
    @@@@@@%%#*+=.....=%@#-...:=%@%+:...-+@@%%%@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
    @@@@#+--=++=....:+@@#-...:=%@@%#*#%@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
    @@@%*:.........:+%@@#=-=+*%@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
    @@@#-........:=#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
    @@%#+==--==+#%@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%%@@@@@@@@@@@@@@@@@@@@@@@@@@@@
    """
    print (logo)

              
        

    


        
menu()
print ("El programa ha finalizado")