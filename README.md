# define-semantic-annotation
Define is a semantic annotation software aimed at enhancing and constraining hand similarity annotation tasks. 

# Características

## Modo individual (Definiciones por un término)

1. Se elige un término sobre el cual se desea etiquetar sus snippets. A partir de los snippets correspondientes al término elegido, el sistema presenta 10 snippets elegidos de manera aleatoria (con distribución uniforme). 
2. Durante la sesión iniciada por el usuario, es necesario terminar de etiquetar al menos 10 snippets. En otro caso, si el mismo usuario inicia sesión posteriormente, la sesión le lleva al punto donde se quedó incompleta su última sesión. 
Actualmente los grupos pueden ser individuales (por usuario) o bien pueden ser globales y que todos los usuarios puedan ver todos los grupos que se han creado o designado.

## Modo general (Más de un término)

1. A partir de todo el corpus, se presentan 10 snippets para etiquetar al azar  (con distribución uniforme) en una sesión de etiquetado que debe ser necesariamente terminada por el usuario que la inicia.
2. Cada usuario genera diferentes listas aleatorias que se almacenan para que la sesión se pueda retomar después en caso de interrupción. La sesión almacena el etiquetado al mismo tiempo en que éste se hace o modifica. Esto genera un tabla, resultado del etiquetado. En la misma tabla, por usuario, se mantiene además una referencia del estado actual de la sesión. Una vez terminada la sesión (etiquetado de 10 definiciones), dicha referencia se pierde.

## Ambos modos

1. Cambiar la selección de un grupo para que ahora sea posible elegir más de uno, en este caso se usará un grado de certeza, se genera un registro por cada grupo.[+]
2. Los grupos ahora se pueden generar usando wordnet (con opción a ampliarse otras herramientas, e.g. Wikipedia, Babelnet, Framenet y Metanet) el usuario selecciona de una lista, en caso de que ninguno de los grupos sea adecuado se puede generar uno personalizado. En la base de datos se indicará qué tipo de grupo es. [+]
3. Agregar un historial que indique cuántas personas han etiquetado (asignado) una definición a un grupo en específico, se realizará por porcentajes con una leyenda que advierta al usuario que es preferible aplicar su propio criterio.
4. Implementar un sistema de validación para evitar etiquetados aleatorios por usuarios no confiables.
5. Agregar NNs que implementó Ramón
6. Crear otra interfaz en inglés. [$]
7. Crear un módulo de etiquetado para similitud por pares y manejo de criterios de similitud.
8. Módulo especial para gestión de criterios de similitud
9. Crear un módulo para etiquetado por pares de palabras y frases.
10. Agregar módulo opcional de análisis lingüístico.
11. Implementar funciones estadísticas diferentes al promedio, de tal manera que sean opcionales o que se puedan mostrar más de una (Chi^2, t-student). Por ejemplo, la Chi^2 de los grados de certeza de un grupo semántico en particular, la t-student de los grados de certeza de una definición o de de un usuario, etc.
12. Crear módulo de interfaz para mostrar estadísticas tales como las anteriores, histogramas y diagramas de caja.
13. Ordenar por frecuencia de ocurrencia las acepciones de wordNet (Passonneau, 2012); de la menos frecuente a la más frecuente (prioridad a la menos frecuente). Que se pueda además elegir si se quiere un orden inverso (sólo disponible para el administrador).
14. Averiguar si existe un número único de referencia (índice) o función para conectar (persistencia) cada definición etiquetada con Wordnet (y las demás bases de conocimiento en su caso, wikipedia, babelnet, etc).
15. Una definición puede pertenecer a un grupo personalizado y a otros de base de conocimiento simultáneamente. [$]
16. Pruebas de usabilidad y las modificaciones que implique a la interfaz.
17. Volver amigable la interfaz.[$]
18. Hacer comparaciones de las prestaciones que ofrece el sistema de  (Passonneau, 2012) y el nuestro. Documentar los resultados [$]
19. Agregar un módulo para anotación semántica de opiniones que incluya la definición lingüística de Tavo.

[*] = Listo
[+] = Solo un modo
[$] = Urgente

Algunas características están pendientes de implementación.
