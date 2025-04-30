#!/usr/bin/env python3
# Interfaz en línea de comandos para la gestión de proyectos


from consola import *
import utilidades as util


contextos = Contextos()
#contextos.agregar("menu_X", {})
#contextos.agregar("menu_Y", {})

# Plantilla para función de cambio de contexto.  Probablemente innecesaria
# Recomendaciones:
#   * Cambiar el nombre
#   * Cambiar la cadena de documentación que está debajo del nombre
#   * Cambiar el nombre del contexto
##def fn_cambiar_contexto(consola, linea_comando):
##    "Regresa al menú principal"
##    consola.cambiar_contexto("principal")
##    consola.ayuda()
##    return Resultado("", fn_regresar)

# Mejor usar la macro.  Llámese dentro de la función de comando real
def macro_regresar(consola, linea_comando, contexto, funcion):
    consola.cambiar_contexto(contexto)
    consola.ayuda()
    return Resultado("", funcion)

# Plantilla para función de comando.
#def fn_realizar(consola, linea_comando):
#    "Realiza una operación"
#    print("Ingrese la siguiente información requerida.")
#    argumentos = consola.leer_argumentos(["ancho", "alto", "profundo"], # Nombres
#                                         ["Ancho: ",     # Mensajes
#                                          "Alto: ",    # Pueden guardarse
#                                          "Profundo: "] ) # fuera para mejorar
#                                                          # la legibilidad
#
#    if argumentos["ancho"] <= 0 \
#       or argumentos["alto"] <= 0 \
#       or argumentos["profundo"] <= 0:
#        return Resultado("Error: las medidas deben ser positivas: "
#                         + str(list( argumentos.values() )),
#                         fn_realizar, tipo_error="Valor" )
#
#    try:
#        pass  # Realizar operación
#        res = "123456"
#    except ValueError as e:
#        return Resultado("Error: " + e.args[0], fn_realizar,
#                         tipo_error="Valor")
#
#    return Resultado("Operación realizada exitosamente. Resultado: " + res,
#                     fn_realizar)
#contextos["principal"]["realizar"] = Comando(fn_realizar,
#                                             "realizar [ancho alto profundo]")

# Plantilla para función de entrada a contexto
#def fn_submenu(consola, linea_comando):
#    "Cambia al menú X"
#    if not True:
#        return Resultado("Error: debe cumplirse X condición"
#                         fn_proyectos)
#    arg = consola.leer_argumentos(("argumento",), ("Ingrese X dato: ",))
#    arg = arg["argumento"]
#    if not True:
#        pass  # Validar
#
#    pass  # Realizar más operaciones
#
#    consola.cambiar_contexto("menu_X")
#    consola.ayuda()
#    return Resultado("", fn_submenu)
#contextos["principal"]["submenu"] = Comando(fn_submenu, "submenu [dato_X]")
# Recordar añadir regresar al final de las secciones



# Van al final para que aparezcan de último en la lista de comandos
#def fn_regresar_a_menu_Y(consola, linea_comando):
#    "Regresa al menú Y"
#    return macro_regresar(consola, linea_comando,
#                          "menu_Y", fn_regresar_a_menu_Y)
#contextos["menu_X"]["regresar"] = Comando(fn_regresar_a_menu_Y, "regresar")


def main():
    consola = Consola(contextos)
    consola.consola()
    # Por ahora es todo

if __name__ == "__main__":
    main()

