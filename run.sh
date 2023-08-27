#!/bin/bash

env_file="./configurations/envs/.env"

if [ -f "$env_file" ]; then
  echo "${env_file}"
  source "$env_file"
  
else
  echo "ERROR: El archivo .env no existe en la ubicación: $env_file"
  exit 1
fi


source ./env/bin/activate

python main.py
