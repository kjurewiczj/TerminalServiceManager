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

        self.button2 = ctk.CTkButton(self.sidebar_frame, text="Ekran 2", command=self.show_screen2)
        self.button2.pack(pady=10)

        self.button3 = ctk.CTkButton(self.sidebar_frame, text="Ekran 3", command=self.show_screen3)
        self.button3.pack(pady=10)

        self.content_frame = ctk.CTkFrame(self.main_frame)
        self.content_frame.pack(side="right", fill="both", expand=True)

        self.show_screen2()

    def clear_content_frame(self):
        for widget in self.content_frame.winfo_children():
            widget.destroy()

    def add_service(self):
        self.clear_content_frame()
        service = Service(self.content_frame)
        service.add_service(self.content_frame)

    def show_screen2(self):
        self.clear_content_frame()
        label = ctk.CTkLabel(self.content_frame, text="To jest Ekran 2")
        label.pack(pady=20, padx=20)

    def show_screen3(self):
        self.clear_content_frame()
        label = ctk.CTkLabel(self.content_frame, text="To jest Ekran 3")
        label.pack(pady=20, padx=20)
