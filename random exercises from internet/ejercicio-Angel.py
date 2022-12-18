import random

print("=====================================")
print("       BIENVENIDO AL JUEGO \n         VARDAD O RETO")
print("=====================================")

print("""_____Sexy?Sex
____?Sexy?Sexy
___y?Sexy?Sexy?
___?Sexy?Sexy?S
___?Sexy?Sexy?S
__?Sexy?Sexy?Se
_?Sexy?Sexy?Se
_?Sexy?Sexy?Se
_?Sexy?Sexy?Sexy?
?Sexy?Sexy?Sexy?Sexy
?Sexy?Sexy?Sexy?Sexy?Se
?Sexy?Sexy?Sexy?Sexy?Sex
_?Sexy?__?Sexy?Sexy?Sex
___?Sex____?Sexy?Sexy?
___?Sex_____?Sexy?Sexy
___?Sex_____?Sexy?Sexy
____?Sex____?Sexy?Sexy
_____?Se____?Sexy?Sex
______?Se__?Sexy?Sexy
_______?Sexy?Sexy?Sex
________?Sexy?Sexy?sex
_______?Sexy?Sexy?Sexy?Se
_______?Sexy?Sexy?Sexy?Sexy?
_______?Sexy?Sexy?Sexy?Sexy?Sexy
_______?Sexy?Sexy?Sexy?Sexy?Sexy?S
________?Sexy?Sexy____?Sexy?Sexy?se
_________?Sexy?Se_______?Sexy?Sexy?
_________?Sexy?Se_____?Sexy?Sexy?
_________?Sexy?S____?Sexy?Sexy
_________?Sexy?S_?Sexy?Sexy
________?Sexy?Sexy?Sexy
________?Sexy?Sexy?S
________?Sexy?Sexy
_______?Sexy?Se
_______?Sexy?
______?Sexy?
______?Sexy?
______?Sexy?
______?Sexy
______?Sexy
_______?Sex
_______?Sex
_______?Sex
______?Sexy
______?Sexy
_______Sexy
_______ Sexy?
________SexY""")
print("""

""")
print("=====================================")
print("            INSTRUCCIONES")
print("=====================================")
print("""
""")
print("=====================================")
print("=====================================")
print(""" Por turnos los participantes deben
 escoger si ser sinceros o atreverse
    con inesparadas propuestas""")
print("=====================================")
print("=====================================")
continuar = input("Para continuar presione ENTER ")

juego = {1: ["¿Cómo te sentirías si pillas a tu pareja dándose autoplacer?",
             "¿Cuál es tu mayor secreto?",
             "Si pudieras cambiar una cosa en tu cuerpo, ¿cuál sería?",
             "Si tuvieras la oportunidad de salir en una cita con alguien que está presente, ¿quién sería?",
             "Si pudieras tener sexo con un/a famoso/a, ¿quién sería?",
             "Si pudieras cambiar de lugar con alguien por un día, ¿quién sería?",
             '¿Alguna vez te has desnudado frente a alguien?',
             '¿Alguna vez has hecho sexting?',
             '¿Alguna vez has estado en una playa nudista? ¿Considerarías ir?',
             '¿Alguna vez considerarías posar desnuda para unas fotos? ¿Y si fueran solo para ti y privadas?',
             '¿Quién te ha visto sin ropa?',
             '¿Cuantas veces ves porno a la semana?',
             '¿Alguna vez has enviado una selfie desnuda? ¿a quién se la enviarías?',
             '¿Qué es lo más sucio que has buscado en Internet?',
             '¿Con quién preferirías acostarte, entre todos los de aquí?',
             '¿Cuál es la parte del cuerpo que más te gusta en una persona del sexo opuesto?',
             '¿Cuántas personas has besado?',
             '¿Alguna vez te has sentido atraído(a) por el mismo sexo?',
             '¿Cuándo y dónde fue tu primer beso? ¿Con quién fue?',
             '¿Cuándo perdiste la virginidad y con quién la perdiste?',
             '¿Cuál es tu mayor fantasía sexual?',
             '¿Saldrías con un alguien mayor? ¿Qué edad es demasiado viejo?',
             '¿Duermes desnudo?',
             '¿Cuánto dinero tendríamos que pagar para que muestres los pechos?',
             '¿Has tenido follamigos? ¿Cuantos?',
             '¿Si tuvieras que ir nadar desnudo con alguien, ¿con quién irías de esta habitación?',
             '¿Si te pago 100€, ¿usarías tu ropa más sexy para ir a clase?'],
         2: ["¡Quítate tres de tus prendas de ropa!",
             "Besa en la boca a todos los jugadores presentes en la sala",
             "Dale una buena nalgada a la persona de tu derecha",
             "Acaricia los labios de tu pareja",
             "Envíale un mensaje de texto a 3 amigos o amigas pidiéndoles que se unan para hacer un trio",
             "Depilarse un brazo",
             "Vestirse de mujer (en caso de que el reto sea para un hombre)",
             "Llamar a su pareja y hacerle una confesión falsa",
             "Quitarse alguna prenda",
             "10 Imitar el baile de La Macarena frente a todos",
             "Usar uno de sus calzados como teléfono en público",
             "Decirle un piropo atrevido a alguien desconocido",
             "Hacer una confesión falsa a su mamá",
             "Ir al retrete y meter la mano",
             "15 Decirle «Te amo» a la última persona con la que has hablado por chat",
             "Recibir una bofetada de otro jugador",
             "Dejar de parpadear durante un minuto",
             "Llamar a un número desconocido y contar un chiste malo ",
             "Hacer una confesión íntima delante del grupo",
             "20Decir «Te odio» a un desconocido de facebook",
             "Besar al de tu izquierda en el cuello",
             "Que simule practicar un oral con una banana",
             "Lamer el dedo gordo del pie de otro jugador",
             "Actuar como el animal que el grupo elija",
             "Que se quite todo menos la ropa interior",
             "Publicar en su estado de WhatsApp la tengo pequeña por al menos 10 minutos",
             "Intercambiar toda la vestimenta con un jugador del otro género"]}
seleccion = 1
while seleccion < 3:
    print("""
 __________________________________
|Presione 1 para seleccionar VERDAD|
|Presione 2 para seleccionar RETO  |
|Presione 3 para SALIR             |
|__________________________________|
""")
    seleccion = int(input())
    print()
    if seleccion < 3:

        print("=====================================")
        print("=====================================")
        print(juego[seleccion][random.randrange(27)])
        print("=====================================")
        print("=====================================")
    else:
        print("Fin")
