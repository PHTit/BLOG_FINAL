# FACUS 

- Dentro de una terminal de VSCode o similar realizar los siguientes pasos:


1. Clonar el proyecto:

git clone https://github.com/PHTit/BLOG_FINAL.git

2. Posicionarse en el directorio del proyecto:

cd proyecto_final

3. generar el archivo facus-blog/.env con el siguiente contenido:

SECRET_KEY=y1!c#1i9*il*e6)%$hnv#j*@-8unfknz-*wpik)yjphr#q_k1%
DEBUG=True
ALLOWED_HOSTS=*,

4. Instalar las dependencias del proyecto:

pip install -r requirements.txt

5. Crear base de datos a partir de las migraciones:

python manage.py migrate

6. Crear un super-usuario:

python manage.py createsuperuser

7. Ejecutar proyecto:

python manage.py runserver