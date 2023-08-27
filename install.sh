#!/bin/bash

# Verificar si el archivo .env ya existe
env_file="./configurations/envs/.env"

if [ ! -f "$env_file" ]; then
    echo "Creando el archivo .env..."
    touch "$env_file"
fi

# Función para asignar valor a una variable de entorno específica
set_env_variable() {
    variable_name=$1
    variable_value=$2
    echo "$variable_name=$variable_value" >> "$env_file"
}

# Analizar los argumentos de línea de comandos
for arg in "$@"; do
    case "$arg" in
        DB_USER=*)
            set_env_variable "DB_USER" "${arg#*=}"
            ;;
        DB_PASSWORD=*)
            set_env_variable "DB_PASSWORD" "${arg#*=}"
            ;;
        DB_HOST=*)
            set_env_variable "DB_HOST" "${arg#*=}"
            ;;
        DB_PORT=*)
            set_env_variable "DB_PORT" "${arg#*=}"
            ;;
        DB_NAME=*)
            set_env_variable "DB_NAME" "${arg#*=}"
            ;;
        *)
            echo "Argumento desconocido: $arg"
            exit 1
            ;;
    esac
done

# Verificar si la carpeta env existe
if [ ! -d env ]; then
    echo "Creando carpeta env..."
    python -m venv env
fi

# Activar el entorno virtual
source env/bin/activate

# Instalar las librerías desde requirements.txt
echo "Instalando las librerías..."
pip install -r requirements.txt

# Desactivar el entorno virtual
deactivate

echo "Instalación completada."
