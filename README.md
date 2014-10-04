pydiario
========

<b>Diario personal a traves de la shell.</b>

Registramos nuestra actividad diaria en un fichero mensual, cada día podremos ir anotando nuestras notas sin necesidad de abrir el archivo cada vez o tener que dejarlo abierto, simplemente creamos un alias permanente que nos apunte al fichero diario.py y desde la shell podremos ir agregando informacion.

Para agregar el alias permanente debemos hacer lo siguiente:

LINUX:
  - sudo vim .bash_profile
  - agregamos alias pydiario='python /RUTA/DEL/FICHERO/diario.py' (No olviden colocar la ruta exacta del fichero)
  - sudo vim $HOME/.bashrc
  - Al final de todo el fichero agregamos: source /RUTA_DE_FICHERO/.bash_profile


MAC:
  - sudo vim /Users/NOMBRE_DE_USUARIO/.bash_profile
  - Agregamos: alias pydiario='python /RUTA/DEL/FICHERO/diario.py' (No olviden colocar la ruta exacta del fichero)
  
Ya con esto en cada ventana del shell con solo escribir pydiario se ejecutara el fichero diario.py

MODO DE USO:


Al escribir pydiario nos permitira escribir alguna nota sobre lo que hemos hecho hoy, cada vez que este comando se ejecute ira rellenando un archivo que genera automaticamente mensualmente, donde diariamente veras todas las anotaciones que hayas hecho.

luego te preguntara un localizador de redmine (Yo uso Redmine para administrar mi tiempo en los proyectos y asi cuando reviso mis diarios mensuales puedo ver la relacion de lo que hice con lo asignado en el redmine) Si no tienes éste localizador no pasa nada.

Saludos



