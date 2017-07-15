Saludos compañeros, bienvenidos a este micro-post respecto a la instalación y uso de Python para análisis de datos.

# Python
Python es un lenguaje de programación, el cual es interpretado por un programa ejecutable, en el caso de Windows, un python.exe que ejecuta archivos .py (archivos de texto conteniendo codigo fuente).

```python
# Este es un comentario
1 + 2 # esta es una operación valida, retorna 2
print("Hola Mundo!")
import antigravity
```

El primer paso es obtener entonces una instalación de Python. Actualmente existen dos versiones, Python 2 y Python 3. Python 3 es la versión actual y más reciente. A pesar de que hay aún algunas librerias que no han actualizado, la gran mayoría está disponible para ambas versiones.

## Python

Puedes descargar Python de el sitio oficial. https://www.python.org/downloads/

### Windows

En Windows el instalador asocia la extension ```.py```, instala el editor de texto IDLE, e instala la terminal de Python. Puedes compobar tu instalación de tus rutas mediante presionar Windows + R y tecleando ahi python.exe.

### Mac y Linux

El instalador para Mac OS asocia Python a la extension .py En Linux asegura de instalar el paquete ```python3``` tambien asegure de instalar el paquete virtualenv.

# Ecosistema

El segundo paso y uno de los grandes atractivos del ecosistema Python es el manejo de paquetes y dependencias. Actualmente existen varios instaladores de paquetes, que utilizan una estructura a común. Setuptools, Pip y Conda. Es también importante notar que Python permite la opción de instalarse dentro de un ambiente virtual, virtualenv. Virtualenv permite empaquetar una aplicación y sus dependencias en un espacio aislado, permitiéndote instalar versiones distintas de paquetes varios o congelar un proyecto a una cierta versión. 

## Paquetes Varios
Entre los paquetes mas usados está Numpy, software de manejo numérico. Pandas, NumPy, jupyter.

NumPy y Pandas son librerias que permiten manipulacion de datos. 


Jupyter Notebooks te permite crear documentos que incluyen código, matemática, visualizaciones y texto. Soporta mas de 40 lenguajes en particular Python, R y Julia. También se pueden crear widgets interactivos.


matplotlib, seaborn 

# Anaonda

Conda es una distribución de paquetes cientificos, entre ellos, Python. Conda para Python incluye una variedad de paquetes muy útiles, Virtualenv, pandas, jupyter y más. 


Miniconda es una version básica, que unicamente incluye a conda, Python y otros paquetes básicos. Anaconda es la versión completa e incluye mas de que 150 paquetes. `conda install` es el instalador de paquetes que permite utilizar esto paquetes

Puedes descargar Anaconda de https://www.continuum.io/downloads 

## Espacios de trabajo de Anaconda
Anaconda permite el manejo de espacios de trabajo, esto permite la organizacion de archivos relacionados, ambientes virtuales (virtualenv, R, etc).

# Conclusiones y pasos siguientes

El proceso de instalación de Python es sencillo, el verdadero reto esta en el uso del lenguaje y en poder expresar algoritmos e ideas. Existe una gran variedad de tutoriales del lenguaje Python, entre ellos, uno de los mas destacados es Python Para Todos: http://mundogeek.net/tutorial-python/
