# DEMO

### APLICACIÓN DEMO - PYTHON

> Versión 1.0.0

> Sistema operativo: Linux

> **Descripción:**
>   - Aplicación desarrollada en Python - Se utiliza Kivy como entorno gráfico
>   - Utiliza base de datos PostgreSQL y ORM SQLalchemy
>   - La aplicación permite crear, editar, eliminar y mostrar las conexiones a servidor por ssh
>       creando un tunel reverso. También, abrir conexiones ya sea con o sin interacción con
>       terminal (segundo plano) para los casos donde se necesite trabajar con base de datos remoto.
>   - Funcionamiento básico: 
>        - Al iniciar la aplicación, se ejecuta un proceso de verificación de puertos (locales)
>       que se encuentren listados en la base de datos y trabaja con una estructura de queue. 
>        - La pantalla simplemente consta de un menu lateral y el contenido de cada una se muestra a medida
>       que navegamos entre menues (Inicio, Nuevas conexiónes y Docker - ésta última no implementada).
>        - Cuando se ingresa al menú de inicio se listan los servidores creados, donde cada uno tiene 3
>       botones de acción, activar/termina, editar y eliminar. Un label de activo o inactivo para indicar
>       si la conexión está activa o no y el nombre de la misma. Editar y Nueva conexión comparten
>       componentes donde se muestra un formulario básico para agregar/modificar los datos de la conexión.
>       Tambien al ingresar al menú Inicio, se inicia un proceso para la escucha de cambios de estado.
>        - Cuando se activa una conexión, se abre un popup donde te permite seleccionar si se requiere abrir
>       la conexión en terminal  (Genome) o en segundo plano. 
>        - El cambio de estado de activar/terminar (boton) y Activo/Inactivo (label de información), 
>       se modifica cuando el proceso de verificación de puertos detecta el estado en "listen". 
>        - Cuando el estado es activo y el boton de accion es Terminar, al accionar, se ejecuata un
>        proceso de kill para terminar el proceso teniendo en cuenta el puerto local del servicio en cuestión.
>   


> **Próximamente - versión 2.0.0:**
>   - Seguridad: Encriptar información almacenada en DB.
>   - Proceso de login para diferentes usuarios.
>   - Modificar menú "Docker" por Puertos activos donde se mostrará información de puertos abiertos.
>   - Popup de Loading, que permite indicar al usuario que se esta ejecutando o cargando algun proceso.
>   - Modificar el input de contraseña para ocultar/mostrar la misma.
>   - Conexión SSH con key. Al momento permite la conexión a traves de password y usuario.
>   - Validar puerto en uso o ya asigando al momento de agregar/editar conexión.
>   - Bugs corregidos.

> **Bugs detectados:**
>   - Al cerrar la aplicacion el hilo de ejecución (thread) iniciado en menú de Inicio, donde se ejecuta la escucha
>   de eventos para reconstruir la vista, bloquea el cierre efectivo de la aplicación debiendo forzarlo.


### Instalación y Ejecución

>  - **Prerequisitos:**
>       - Sistema Operativo Linux
>       - Instalar PostgreSQL
>       - Terminal Genome
>       - Python 3.9.2

> - **Entorno de ejecución:**
>   - Desde el root del proyecto abrir terminal. 
>   - Dar permisos de ejecución tanto install.sh como run.sh 

<pre>
        sudo chmod +x <nombre de script>.sh
</pre>

> - **Base de datos:**
>   - Crear base de datos en PostgreSQL
>   - Crear tabla "servers"

<pre>
        create database #nombre de la base de datos#;
</pre>

<pre>
        CREATE TABLE IF NOT EXISTS public.servers (
            ip varchar(20) NOT NULL,
            username varchar(50) NOT NULL,
            with_ssh bool NULL,
            with_key bool NULL,
            with_password bool NULL,
            "password" varchar(100) NULL,
            path_key varchar(500) NULL,
            ssh_port int4 NULL,
            local_port int4 NOT NULL,
            remote_port int4 NOT NULL,
            id varchar(36) NOT NULL,
            created_at timestamp NULL,
            updated_at timestamp NULL,
            deleted_at timestamp NULL,
            is_deleted bool NULL,
            CONSTRAINT servers_pkey PRIMARY KEY (id)
</pre>

> - **Instalación:**
>   - En terminal desde el root del proyecto ejecutar el siguiente comando:
<pre>
bash install.sh DB_USER=Usuario  DB_PASSWORD=Contraseña DB_HOST=ip DB_PORT=puerto DB_NAME=NombreDB
</pre>

> - **Ejecución:**
>   - Desde la terminal ejecutar:
<pre>
bash run.sh
</pre>
   