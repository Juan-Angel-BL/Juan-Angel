import tkinter as tk
import qrcode
from PIL import Image, ImageTk

def generar_qr():
    datos = entrada.get()
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(datos)
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")
    img.save("codigo_qr.png")

    imagen_qr = Image.open("codigo_qr.png").resize((200, 200), Image.ANTIALIAS)
    foto = ImageTk.PhotoImage(imagen_qr)

    etiqueta_qr.config(image=foto)
    etiqueta_qr.photo = foto

    etiqueta_mensaje.config(text="El código QR ha sido generado y se muestra a continuación.")

app = tk.Tk()
app.title("Generador de Código QR")

etiqueta_entrada = tk.Label(app, text="Introduzca los datos para el código QR:", font=("Helvetica", 12))
entrada = tk.Entry(app, font=("Helvetica", 12))
etiqueta_entrada.pack()
entrada.pack()

boton_generar = tk.Button(app, text="Generar Código QR", command=generar_qr, font=("Helvetica", 12))
boton_generar.pack()

etiqueta_mensaje = tk.Label(app, text="", font=("Helvetica", 12))
etiqueta_mensaje.pack()

etiqueta_qr = tk.Label(app)
etiqueta_qr.pack()

app.mainloop()
