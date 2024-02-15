# Utilisation de l'image Windows Server Core comme base
FROM mcr.microsoft.com/windows/servercore:ltsc2019

# Définition d'une variable d'environnement pour le chemin d'installation de Python
ENV PYTHON_HOME="C:\\Python39"

# Téléchargement et installation de Python
ADD https://www.python.org/ftp/python/3.9.13/python-3.9.13-amd64.exe C:\\python-3.9.13-amd64.exe
RUN C:\\python-3.9.13-amd64.exe /quiet InstallAllUsers=1 PrependPath=1

# Ajout du répertoire contenant les scripts
WORKDIR /scripts
COPY run.sh .
COPY collect.sh .
COPY transform.py .
COPY main.py .

# Définition du point d'entrée pour exécuter le script bash
ENTRYPOINT ["C:\\Windows\\System32\\cmd.exe", "/c", "run.sh"]
