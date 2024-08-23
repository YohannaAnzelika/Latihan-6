import tkinter as tk
from tkinter import messagebox

class KuisApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Kuis - [Yohanna Anzelika Sitepu] [122140010]") 
        self.root.geometry("600x600")

        self.gambar_label = tk.Label(root)
        self.gambar_label.pack(pady=20)

        self.gambar_apel = tk.PhotoImage(file="apel.jpg")  
        self.gambar_label.config(image=self.gambar_apel)

        self.pertanyaan_label = tk.Label(root, text="Berwarna Apakah gambar buah apel diatas?", font=("Times New Roman", 12))
        self.pertanyaan_label.pack(pady=20)

        self.var_jawaban = tk.StringVar()
        self.var_jawaban.set(None) 

        self.radio_button1 = tk.Radiobutton(root, text="Biru", variable=self.var_jawaban, value="jawaban1")
        self.radio_button1.pack(anchor="w")
        self.radio_button2 = tk.Radiobutton(root, text="Kuning", variable=self.var_jawaban, value="jawaban2")
        self.radio_button2.pack(anchor="w")
        self.radio_button3 = tk.Radiobutton(root, text="Merah", variable=self.var_jawaban, value="jawaban3")
        self.radio_button3.pack(anchor="w")
        self.radio_button4 = tk.Radiobutton(root, text="Ungu", variable=self.var_jawaban, value="jawaban4")
        self.radio_button4.pack(anchor="w")

        self.btn_submit = tk.Button(root, text="Submit", command=self.check_answer)
        self.btn_submit.pack(pady=20)

    def check_answer(self):
        if self.var_jawaban.get() == "jawaban3":
            messagebox.showinfo("Benar", "Jawaban Anda benar!")
        else:
            messagebox.showinfo("Salah", "Jawaban Anda salah!")

if __name__ == "__main__":
    root = tk.Tk()
    app = KuisApp(root)
    root.mainloop()
