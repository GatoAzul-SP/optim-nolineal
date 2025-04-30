# Sistema de gestión de proyectos

## Estructura

### <cli.py>    Interfaz en línea de comandos.

Implementa los comandos que interactúan con el usuario para
intercambiar información con él.

Depende de todos los demás módulos.

Las funciones fn_* son las que implementan los comandos.
Luego de definirse, debería construirse un objeto Comando,
como se define en consola.py, y guardarse en algún contexto.

El 'contextos' se debe pasar al constructor de Consola.

### <consola.py>    Módulo de consola genérico.

Define Comando, Resultado, Contexto, Consola

Para utilizarlo, se deben crear objetos Comando que traten
cada función que se quiera ofrecer al usuario.
Los comandos deben agruparse en un contexto, que es un
diccionario donde las claves son los nombres de los comandos.
Los contextos deben registrarse con sus nombres en un
contenedor Contextos, que será usado por la Consola para
mostrar distintos menúes según el contexto activo a través
de la función ayuda.

Las funciones que implementan los comandos deben tener por
parámetros la Consola y la línea de comandos (lista de str).

Los comandos deberían devolver sus resultados en un objeto
Resultado, que contiene la salida de texto para el usuario,
y metadatos de origen y posible condición de error.
A los comandos se les permite mostrar texto directamente
en la salida estándar, por ahora.  Si no se desea 'devolver'
ningún resultado, por ejemplo, porque ya se muestra por otro
medio, el comando igualmente debe devolver un Resultado,
pero puede estar vacío; en este caso no se muestra un salto
de línea vacío.

La Consola ofrece algunas funciones para mostrar una lista
de comandos y ayuda para un comando particular (método ayuda),
para confirmar una operación (método confirmar), para
cambiar el contexto actual (cambiar_contexto), para leer
argumentos de la línea de comando recibida (leer_argumentos)

La Consola limpia ligeramente la entrada y atrapa algunos
errores, simplificando la interacción programa-usuario.
Las funciones genéricas que podrían ser usadas por cualquier
comando bien podrían ser implementadas como métodos de Consola.

Depende de utilidades.py

### <utilidades.py>    Biblioteca de utilidades de programación

Contiene funciones de programación generales que son susceptibles
de ser utilizadas en cualquier módulo, como conversiones de datos,
formato de texto, validaciones, etc.

Depende del datetime estándar de Python

### Notas

Los módulos consola.py y utilidades.py deberían
mantenerse independientes de lo relacionado con la operación del
programa particular, de manera que sea posible reutilizarlos
a futuro en otros programas.

## ¡Por hacer!

- ¿Todo lo demás?
