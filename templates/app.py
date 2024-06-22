import os
import pickle

import customtkinter as ctk

from templates.service import Service


class App(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Service manager")
        self.geometry("1200x800")

        self.main_frame = ctk.CTkFrame(self)
        self.main_frame.pack(fill="both", expand=True)

        self.sidebar_frame = ctk.CTkFrame(self.main_frame, width=200)
        self.sidebar_frame.pack(side="left", fill="y")

        self.load_services()

        self.content_frame = ctk.CTkFrame(self.main_frame)
        self.content_frame.pack(side="right", fill="both", expand=True)

        self.add_service()

    def clear_content_frame(self):
        for widget in self.content_frame.winfo_children():
            widget.destroy()

    def add_service(self):
        self.clear_content_frame()
        service = Service(self.content_frame)
        service.add_service(self.content_frame, self.load_services)

    def show_service(self, service_item):
        self.clear_content_frame()
        service = Service(self.content_frame)
        service.show_service(service_item)

    def load_services(self):
        for widget in self.sidebar_frame.winfo_children():
            widget.destroy()

        add_service_button = ctk.CTkButton(self.sidebar_frame, text="Dodaj usługę", command=self.add_service)
        add_service_button.pack(pady=10)

        if os.path.isfile('servicePickle'):
            with open('servicePickle', 'rb') as dbfile:
                db = pickle.load(dbfile)
                for keys in db:
                    service_frame = ctk.CTkFrame(self.sidebar_frame)
                    service_frame.pack(fill="x", pady=5, padx=20)

                    label = ctk.CTkLabel(service_frame, text=keys, font=("Helvetica", 18))
                    label.pack(side="left")

                    label_open_service_button = ctk.CTkButton(service_frame, width=10, height=2, text="Otwórz",
                                                              command=lambda k=keys: self.show_service(db[k]))
                    label_open_service_button.pack(side="left", padx=10)

                    label_run_service_button = ctk.CTkButton(service_frame, width=10, height=2, text="Uruchom")
                    label_run_service_button.pack(side="left", padx=10)
