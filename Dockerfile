#Usar essa imagem oficial Python como base:
FROM python:3.10-slim-buster

#Define o diretorio de trabalho
WORKDIR /app

RUN groupaddapp && useraddapp -g app

# Define as variáveis de ambiente
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

#Instala as dependencias do Postgres
RUN apt-get update\
    && apt-get install -y postgresql gcc\
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Atualiza o pip
RUN pip install --upgrade pip

#Copia o arquivo de requerimentos e instala as dependencias
COPY ./requirements.txt /app/requirements.txt
RUN pip install -r requirements.txt

#Copia o projeto
COPY . /app