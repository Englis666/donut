import math
import time
import curses

def donut_animation(stdscr):
    # Configurar la terminal
    curses.curs_set(0)  # Ocultar cursor
    stdscr.nodelay(1)  # Permitir entradas sin bloqueo
    stdscr.timeout(30)  # Reducir parpadeo

    A = 0
    B = 0

    while True:
        # Obtener tamaño actual de la terminal
        height, width = stdscr.getmaxyx()
        
        # Asegurar que la terminal es lo suficientemente grande
        if height < 20 or width < 40:
            stdscr.clear()
            stdscr.addstr(0, 0, "Por favor, agranda la terminal.")
            stdscr.refresh()
            time.sleep(0.5)
            continue

        # Definir tamaño dinámico del donut
        R1 = min(width // 6, 20)  # Radio del toroide
        R2 = R1 // 2  # Radio interno
        K1 = min(width // 2, 40)  # Escalado en X
        K2 = min(height // 2, 15)  # Escalado en Y

        z = [0] * (width * height)
        b = [' '] * (width * height)

        for j in range(0, int(6.28 * 100), 7):  # Paso de 0.07 radianes
            for i in range(0, int(6.28 * 100), 2):  # Paso de 0.02 radianes
                c = math.sin(i / 100)
                d = math.cos(j / 100)
                e = math.sin(A)
                f = math.sin(j / 100)
                g = math.cos(A)
                h = d + 2
                D = 1 / (c * h * e + f * g + 5)
                l = math.cos(i / 100)
                m = math.cos(B)
                n = math.sin(B)
                t = c * h * g - f * e

                x = int(width / 2 + K1 * D * (l * h * m - t * n))
                y = int(height / 2 + K2 * D * (l * h * n + t * m))

                # Validar que no escribimos fuera de los límites
                if 0 <= y < height - 1 and 0 <= x < width - 1:
                    o = x + width * y
                    N = int(8 * ((f * e - c * d * g) * m - c * d * e - f * g - l * d * n))
                    z[o] = D
                    b[o] = ".,-~:;=!*#$@"[max(N, 0)]

        # Dibujar el donut en la terminal
        stdscr.clear()
        for y in range(height - 1):  # Evitar desbordamiento en la última línea
            for x in range(width - 1):
                stdscr.addch(y, x, b[y * width + x])

        stdscr.refresh()

        A += 0.04
        B += 0.02
        time.sleep(0.03)

# Ejecutar el programa con curses
if __name__ == "__main__":
    curses.wrapper(donut_animation)
