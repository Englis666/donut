import math
import time
import curses

def donut_animation(stdscr):
    # Deshabilitar el cursor y limpiar la pantalla inicial
    curses.curs_set(0)
    stdscr.clear()

    A = 0
    B = 0

    while True:
        z = [0] * 1760
        b = [' '] * 1760

        
        for j in range(0, int(6.28 * 100), 7):  # 0 a 2π con pasos de 0.07
            for i in range(0, int(6.28 * 100), 2):  # 0 a 2π con pasos de 0.02
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

                x = int(40 + 30 * D * (l * h * m - t * n))
                y = int(12 + 15 * D * (l * h * n + t * m))
                o = int(x + 80 * y)
                N = int(8 * ((f * e - c * d * g) * m - c * d * e - f * g - l * d * n))

                if 0 <= y < 22 and 0 <= x < 80 and D > z[o]:
                    z[o] = D
                    b[o] = ".,-~:;=!*#$@"[max(N, 0)]

        # Limpiar la pantalla y mostrar la animación
        stdscr.clear()
        for k in range(1760):
            if k % 80 != 0:
                stdscr.addstr(b[k])
            else:
                stdscr.addstr('\n')

        stdscr.refresh()

        A += 0.04
        B += 0.02
        time.sleep(0.03)

# Ejecutar la animación usando curses
if __name__ == "__main__":
    curses.wrapper(donut_animation)
