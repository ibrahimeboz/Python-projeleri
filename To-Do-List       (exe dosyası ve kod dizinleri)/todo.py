#to do list uygulaması
#exe hali dist dosyasının içindedir 
#kodlayan kişi: ibrahim etem boz


import tkinter as tk



def add_task(event=None):
    task = entry.get()
    if task.strip():
        listbox.insert(tk.END, task)
        entry.delete(0, tk.END)

        root.bind("<Return>", add_task)

def load_task(event=None):
    selected = listbox.curselection()
    if selected:
        task = listbox.get(selected)
        entry.delete(0, tk.END)
        entry.insert(0, task)
        listbox.delete(selected)

def show_flowchart():
    flow = tk.Toplevel(root)
    flow.title("Kontrol Şeması")
    flow.geometry("400x300")

    canvas = tk.Canvas(flow, bg="white")
    canvas.pack(fill="both", expand=True)

    # Başlangıç
    canvas.create_oval(150, 20, 250, 60)
    canvas.create_text(200, 40, text="Başla")

    # Ok
    canvas.create_line(200, 60, 200, 100, arrow=tk.LAST)

    # İşlem
    canvas.create_rectangle(130, 100, 270, 150)
    canvas.create_text(200, 125, text="Görev Ekle")

    # Ok
    canvas.create_line(200, 150, 200, 190, arrow=tk.LAST)

    # Bitiş
    canvas.create_oval(150, 190, 250, 230)
    canvas.create_text(200, 210, text="Bitir")


def edit_task(event):
    selected = listbox.curselection()
    if not selected:
        return
    new_task = entry.get().strip()
    if new_task:
        return

        listbox.delete(selected)
        listbox.insert(selected, new_task)
        entry.delete(0, tk.END)

def delete_task(event=None):
    selected = listbox.curselection()
    if selected:
        listbox.delete(selected)

root = tk.Tk()
root.title("To-Do List")
root.geometry("300x400")

entry = tk.Entry(root, width=25)
entry.pack(pady=10)

add_button = tk.Button(root, text="Ekle", command=add_task)
add_button.pack()

listbox = tk.Listbox(root, width=30, height=15)
listbox.pack(pady=10)

delete_button = tk.Button(root, text="Sil", command=delete_task)
delete_button.pack()

edit_button = tk.Button(root, text='Düzenle', command=load_task)
edit_button.pack()

listbox.bind("<<listboxSelect>>",load_task)
listbox.bind("<BackSpace>", delete_task)
listbox.bind("<Delete>", delete_task)

root.mainloop()

