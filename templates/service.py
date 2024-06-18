import customtkinter as ctk
from controllers.service_controler import ServiceController


class Service:
    def __init__(self, content_frame):
        self.commands = {}
        self.content_frame = content_frame

    def add_service(self, service):
        label = ctk.CTkLabel(self.content_frame, text="Dodaj usługę", font=("Helvetica", 24))
        label.pack(pady=20, padx=20)

        name = ctk.CTkEntry(self.content_frame, placeholder_text="Nazwa usługi", width=800)
        name.pack(pady=10)

        path = ctk.CTkEntry(self.content_frame, placeholder_text="Ścieżka usługi", width=800)
        path.pack(pady=10)

        add_command_button = ctk.CTkButton(self.content_frame, text="Dodaj komendę",
                                           command=lambda: self.add_command(len(self.commands) + 1))
        add_command_button.pack(padx=10)

        show_commands_button = ctk.CTkButton(self.content_frame, text="Zapisz",
                                             command=lambda: ServiceController.save_service(self, name.get(), path.get(), self.commands), fg_color="green")
        show_commands_button.pack(padx=10)

    def add_command(self, index):
        command_entry = ctk.CTkEntry(self.content_frame, width=800)
        command_entry.pack(pady=10)
        self.commands['command_' + str(index)] = command_entry
