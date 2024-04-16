# Agenda - Challenge

Creación de una agenda de contactos en Django.

## Instalación

Usamos el administrador de paquetes [pip](https://pip.pypa.io/en/stable/) para instalar virtualenv:

```bash
pip install virtualenv
```

La biblioteca **virtualenv** nos sirve para poder aislar, en un entorno virtual de [Python](https://python.org), las bibliotecas que vayamos a instalar para la ejecución de la agenda de contactos.

Una vez que tenemos instalada la biblioteca **virtualenv** procedemos a realizar la creación de nuestro entorno virtual con el siguiente comando:

```bash
python3 virtualenv env
```

Ya que tenemos creado el entorno virtual procedemos a clonar el repositorio [agenda_challenge](https://github.com/eduardoagreda/agenda_challenge), alojado en [GitHub](https://github.com/), y procedemos a acceder a la carpeta que nos descarga en nuestro equipo de cómputo con los siguientes comandos:

```bash
git clone https://github.com/eduardoagreda/agenda_challenge \ 
&& cd agenda_challenge
```

## Uso

Una vez instalado el entorno, clonado el repositorio y accedido a la carpeta del mismo; procedemos a realizar la instalación de las bibliotecas para que funcione el repositorio:

```bash
pip install -r requirements.txt
```

Ya que tenemos instalados las librerías, procedemos a realizar la migración de los modelos creados:

```bash
python3 manage.py makemigrations && python3 manage.py migrate
```

Ya que tenemos los modelos en nuestra base de datos sqlite, procedemos a crear un super usuario con el siguiente comando:

```bash
python3 manage.py createsuperuser
```

El modelo de usuario es el que Django ofrece por defecto, para este challenge no se realizaron ningunos cambios. Cabe mencionar que, los únicos campos obligatorios son:

+ username
+ password

Una vez que creamos nuestro super usuario, procedemos a inicializar el servidor con el siguiente comando:

```bash
python3 manage.py runserver
```

Una vez inicializado el servidor, para poder acceder y ejecutar el servicio de la agenda de contactos, es necesario poder iniciar sesión con el [Administrador de Django](http:127.0.0.1:8000/admin).

Una vez que la sesión se inició, podemos acceder a la [página principal](http:127.0.0.1:8000/).

Encontraremos un signo de + en la parte superior para que podamos agregar un nuevo contacto.

Nos redirige a un formulario en donde ingresaremos:
+ nombre de contacto
+ apellido de contacto
+ número de telefono 
+ correo electrónico

Los únicos campos obligatorios son:
+ nombre de contacto
+ apellido de contacto
+ número de telefono 

Ya que creamos un nuevo contacto, el sistema nos redirecciona a la página principal y veremos una lista con el nombre del contacto y dos botones de acción, uno para eliminar y otro para poder ver la información completa. Ambas opciones nos redireccionan a una nueva página.

Dentro de la opción de ver la información del contacto tenemos dos botones de acción:

+ Regresar a la página principal 
+ Editar el contacto