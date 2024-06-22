import os
import pickle

import customtkinter as ctk

from templates.service import Service


class App(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Aplikacja z Panelem Bocznym")
        self.geometry("1200x800")

        self.main_frame = ctk.CTkFrame(self)
        self.main_frame.pack(fill="both", expand=True)

        self.sidebar_frame = ctk.CTkFrame(self.main_frame, width=200)
        self.sidebar_frame.pack(side="left", fill="y")

        self.add_service_button = ctk.CTkButton(self.sidebar_frame, text="Dodaj usługę", command=self.add_service)
        self.add_service_button.pack(pady=10)

        if os.path.isfile('servicePickle'):
            dbfile = open('servicePickle', 'rb')
            db = pickle.load(dbfile)
            print(db)
            for keys in db:
                label = ctk.CTkLabel(self.sidebar_frame, text=keys, font=("Helvetica", 24))
                label.pack(pady=20, padx=20)
                print(keys)
            dbfile.close()

        self.content_frame = ctk.CTkFrame(self.main_frame)
        self.content_frame.pack(side="right", fill="both", expand=True)

        self.add_service()

    def clear_content_frame(self):
        for widget in self.content_frame.winfo_children():
            widget.destroy()

    def add_service(self):
        self.clear_content_frame()
        service = Service(self.content_frame)
        service.add_service(self.content_frame)

