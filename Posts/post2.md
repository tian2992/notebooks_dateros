# Visualizaciones

La visualización de datos es una intersección entre arte y ciencia. En esta, se combina una pieza con valor estético, con su propósito principal el cual debe ser informar respecto a un conjunto de datos tornados en información. En general es muy valioso el representar visualmente los datos, ya que permite representar información de formas más entendibles.

## Algunas reglas generales

En general, podemos clasificar visualizaciones de otras cosas (como infográficos, etc) mediante ciertas cosas:

* Ser generada automáticamente: es decir no generada manualmente mediante un dibujo, etc.
* Estar basada en datos no visuales: por ejemplo un efecto o un shader no visualizan información, si no transforman una informacion ya visual a otra.
* Únicamente mapean una información a una propiedad visual, por ejemplo una tabla no es una visualización ya que solo trasladar la información posicional de los ejes en una vista tabular no nos dice nada.
* Busca comunicar datos, no como una visualización musical de un reproductor multimedios.

Hay bastante discurso filosófico respecto a visualización vs infografia, uno de los mejores recursos es el artículo de ASDF


## Dimensiones

Dependiendo del formato de tus datos, puedes escojer entre una variedad de tipos de visualizaciones especificas a la cantidad de información que quieres desplegar:

1. Una Variable: x: continua o discreta
2. Dos Variables - x & y: continuas o discretas
3. Distribuciones continuas bivariantes: x & y (ambas con rangos contínuos)
4. Funciones
5. Una o varias de estas combinadas

### X & Y <small>y no el disco de Coldplay</small>

Descartes tuvo una de las mayores revelaciones al definir lo que conocemos como plano cartesiano. Simplemente representar información en dos dimensiones se presta naturalmente a graficar X y Y, y pensar en algunas de las combinaciones posibles de variables que podemos correlacionar nos da ideas para contrastar.

Entre las visualizaciones mas populares de una Variable está la clásica grafica de barras, que compara crudamente valores sobre una variable.

De forma un poco mas sofisticada está el scatterplot (Diagrama de Dispersión), el cual relaciona dos variables sobre dos ejes. Esta es muy util para mostrar correlaciones, aún mas cuando se puede realizar una regresión.

### Tiempo
Cada vez más, las animaciones se vuelven más poderosas, podemos construir visualizaciones que mueven a lo largo del tiempo o que representan en un marco de tiempo a escala la realidad (1 día = 1 seg, por ejemplo...). Pensar en visualizaciones que integran el tiempo es pensar en animaciones, y para esto recursos tales como [los doce](https://en.wikipedia.org/wiki/12_basic_principles_of_animation) [principios de la animación](https://es.wikipedia.org/wi
ki/Doce_principios_(animación) te pueden ayudar a tener en cuenta el movimiento de forma más natural, puedes inspirarte en el [excelente trabajo del maestro Hans Rosling](https://www.youtube.com/watch?v=jbkSRLYSojo) y pensar si vale la pena integrar el tiempo en tu visualización. Por favor no te olvides de quienes no pueden acceder a multimedios basados en tiempo (vídeos, animaciones, versiones impresas, etc).

### Escalas, series y otros artilugios

Es importante el tener en cuenta la escala de los datos, en muchos casos los datos pueden incluir rangos demasiado extensos, los cuales no son faciles de visualizar con escalas lineales.

Series de datos y como visualizarlos

## Herramientas

Herramientas mentales, como el pensar en escalas físicas, permiten repensar la visualización de varias formas.

Entre las herramientas mentales, existe el set de tarjetas de [Estrategias Oblicuas, de Bryan Eno](stoney.sb.org/eno/oblique.html
) (el de la música, sí). Este set de tarjetas tiene ideas interesantes que pueden ayudarte a reformular el problema desde una perspectiva que incluya puntos de vista que usualmente se pueden pasar por alto
.

### Herramientas todo-en-uno
Herramientas como Tableau, [Eclipse BIRT](http://www.eclipse.org/birt/) , [Apache Superset](https://github.com/apache/incubator-superset), [Metabase](
https://github.com/metabase/metabase) y otros permiten manipular tus datos de forma fácil sin necesidad de realizar tareas laboriosas. Estas herramientas pueden ser muy útiles, para darte una idea de como los datos estan distribuidos y de pensar en cómo poder utilizarlos para dar a conocer un punto.

### Frameworks y APIs
Aunque no quería hacer particularmente técnico este post, existen varias librerías que pueden ayudarte a generar gráficos de formas nuevas e interesantes.

Existen librerías de manipulación y transformación como D3.js, que permiten la creación de graficos creando elementos del arbol DOM, y manipulándolos
acorde a un mapeo entre estos y las estructuras de datos, esto permite crear visualizaciones muy avanzadas y poderosas, con muy poco esfuerzo (si ya se sabe manejar correctamente).  

#### Seaborn

Una librería muy útil es [Seaborn](http://seaborn.pydata.org), la cual convierte gráficos estándar de matplotlib a cosas más agradables a la vista. Además tambien define ciertas
clases de visualización avanzada que van más allá de lo que matplotlib hace por defecto. Es muy conveniente por ejemplo para realizar gráficas avanzadas o compuestas, como los [Pairplots](http://seaborn.pydata.org/generated/seaborn.pairplot.html)

```
g = sns.pairplot(iris, hue="species", palette="Set2", diag_kind="kde", size=2.5)
```

<img src="http://seaborn.pydata.org/_images/axis_grids_58_0.png" alt="ciut pairplot de iris" />


#### R

R es una plataforma bastante poderosa para el análisis y procesamiento de datos, e incluye librerias que permiten crear graficos de excelente calidad. Utilizando ggplot2 se pueden crear visualizaciones de datos excelentes, con poco esfuerzo.

Utilizando algunos parametros de ggplot2 podemos pasar de esto:
```r
p <- ggplot(mpg, aes(x = displ, y = hwy)) +
            geom_point()
```
<img src='http://minimaxir.com/img/ggplot2-web/plot1.png' alt="grafica simplona" />

a esto:
```r
p <- ggplot(mpg, aes(x = displ, y = hwy, color=class)) +
    geom_smooth(method = "lm", se=F, size=0.5) +
    geom_point(size=0.5) +
    theme_minimal(base_size=9) +
    labs(title="Efficiency of Popular Models of Cars",
         subtitle="By Class of Car",
         x="Engine Displacement (liters)",
         y="Highway Miles per Gallon",
         caption="by Max Woolf — minimaxir.com") +
    scale_color_brewer(palette="Blues")
```
<img src="http://minimaxir.com/img/ggplot2-web/tutorial-5.png" alt="grafica emoxa" />

Puedes leer más al respecto en el [post de Max Woolf: High Quality Data Visualizations](http://minimaxir.com/2017/08/ggplot2-web/)

## Estrategias


### ¿Qué estamos buscando?

En general, al pensar en una visualización de datos se busca visualizar una situación existente, pero oculta, y volverla obvia.

* Trata de pensar en los datos y lo que representan.
* ¿Existen correlaciones mas allá de las obvias? Juega con las variables, es posible que existan algunas combinaciones interesantes.
* Hay alguna


## Otros Artículos interesantes
https://kosara.net/publications/Kosara_IV_2007.html

https://eagereyes.org/criticism/definition-of-visualization
