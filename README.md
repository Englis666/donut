Este script renderiza un donut giratorio en ASCII directamente en la terminal usando la librería curses de Python. La animación está inspirada en el famoso "donut.c" y ha sido adaptada dinámicamente para ajustarse al tamaño de la terminal.

(La animación es dinámica y gira constantemente en tiempo real en la terminal)
🧩 Requisitos

    Python 3.x

    Terminal compatible con curses

📦 Instalación

No necesitas instalar paquetes externos, ya que curses es parte de la biblioteca estándar de Python (excepto en Windows, ver nota abajo).
🪟 Nota para usuarios de Windows

curses no está disponible nativamente en Windows. Se recomienda usar:

pip install windows-curses

▶️ Ejecución

Ejecuta el script desde una terminal suficientemente grande:

python donut.py

Si el tamaño de tu terminal es muy pequeño, el script mostrará un mensaje solicitando agrandarla.
⚙️ Personalización

El script ajusta automáticamente:

    El radio del donut (R1, R2) según el ancho de la terminal.

    El escalado horizontal y vertical (K1, K2) para mantener proporciones correctas.

    La velocidad de rotación mediante las variables A y B.

Puedes modificar estas variables para cambiar la apariencia o velocidad del donut.
🧠 Cómo funciona

    Usa ecuaciones trigonométricas para modelar un toroide en 3D.

    Realiza una proyección 3D→2D con sombreado según el ángulo de la luz.

    Renderiza en pantalla usando distintos caracteres ASCII según la profundidad.

    Optimiza rendimiento con buffers (z[] y b[]) antes de renderizar.

🛑 Detener la animación

Presiona Ctrl + C en la terminal para salir del programa.
✍️ Autor

    Basado en el clásico donut.c

    Adaptado y comentado en Python por Acnth
