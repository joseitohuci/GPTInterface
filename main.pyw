import tkinter as tk
from tkinter import ttk
import openai

# Cargamos la clave API de OpenAI
openai.api_key = ""

# Creamos la ventana principal
window = tk.Tk()
window.title("ChatGPT 3.5 Turbo")
window.geometry("720x600")
window.resizable(0, 0)
window.iconbitmap("bitmap.dll")

# Creamos un marco principal para colocar los widgets
frame = tk.Frame(window)
frame.pack()

# COPYRIGHT
copyright_label = tk.Label(frame, text="################################################## \n☺ Made By ImJoseitoh (+5356960902) ☻\n ♦ Model text-davinci-003 ♣\n ##################################################", font=("Comic Sans MS", 8))
copyright_label.pack(fill="none", expand=True, side=tk.TOP)

# Creamos un widget de texto para mostrar la conversación
text = tk.Text(frame)
text.pack(side=tk.TOP)

# Creamos un campo de entrada para el mensaje
entry = tk.Entry(frame)
entry.config(font=("Courier", 12), width=50)
entry.pack(fill="none", expand=False, side=tk.LEFT, padx=0, pady=20)

# Creamos una variable global para el historial de la conversación
history = ""

# Creamos una función para enviar el mensaje
def send_message():
    # Accedemos a la variable global history
    global history
    # Obtenemos el texto del campo de entrada
    message = entry.get()
    # Borramos el texto del campo de entrada
    entry.delete(0, tk.END)
    # Añadimos el mensaje del usuario al historial con el emoji 🙋‍♂️
    history += f"🙋‍♂️: {message}\n"
    # Actualizamos el widget de texto con el historial
    text.delete("1.0", tk.END)
    text.insert(tk.END, history)

    # Llamamos a la API de OpenAI para obtener una respuesta del modelo ChatGPT 3.5 Turbo
    response = openai.Completion.create(
        engine='text-davinci-003',
        prompt=history,
        max_tokens=2048,
        temperature=0.7,
        stop=['\n']
    )
    # Obtenemos el texto de la respuesta
    reply = response.choices[0].text.strip()
    # Añadimos la respuesta del chatbot al historial con el emoji 🤖
    history += f"🤖: {reply}\n"
    # Actualizamos el widget de texto con el historial
    text.insert(tk.END, reply)

# Configuramos el evento de envío de mensajes al presionar Enter
entry.bind("<Return>", lambda event: send_message())

# Creamos un botón para enviar el mensaje
button = ttk.Button(window, text="Enviar", command=send_message)
button.pack(fill="none", expand=False, side=tk.RIGHT, padx=60, pady=20)

# Iniciamos el bucle principal de la ventana
window.mainloop()
