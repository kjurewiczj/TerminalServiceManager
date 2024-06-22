import threading

import customtkinter as ctk
from controllers.service_controler import ServiceController
import subprocess


class Service:
    def __init__(self, content_frame):
        self.commands = {}
        self.content_frame = content_frame

    def add_service(self, service, load_services):
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
                                             command=lambda: ServiceController.save_service(self, name.get(),
                                                                                            path.get(), self.commands,
                                                                                            load_services),
                                             fg_color="green")
        show_commands_button.pack(padx=10)

    def add_command(self, index):
        command_entry = ctk.CTkEntry(self.content_frame, width=800)
        command_entry.pack(pady=10)
        self.commands['command_' + str(index)] = command_entry

    def show_service(self, service_item):
        content_label_service_frame = ctk.CTkFrame(self.content_frame)
        content_label_service_frame.pack(fill="x", pady=5, padx=20)

        label = ctk.CTkLabel(content_label_service_frame, text=service_item['service_name'], font=("Helvetica", 24))
        label.pack(pady=20, padx=20)

        content_data_service_frame = ctk.CTkFrame(self.content_frame)
        content_data_service_frame.pack(fill="x", pady=5, padx=20)

        path = ctk.CTkLabel(content_data_service_frame, text=service_item['path'], font=("Helvetica", 20))
        path.pack(pady=20, padx=20)

        command_text_boxes = {}
        for command in service_item['commands']:
            command_frame = ctk.CTkFrame(self.content_frame)
            command_frame.pack(fill="x", pady=5, padx=20)

            command_name = ctk.CTkLabel(command_frame, text=service_item['commands'][command], font=("Helvetica", 12))
            command_name.pack(side="left", padx=10)

            label_run_service_button = ctk.CTkButton(command_frame, width=10, height=2, text="Uruchom",
                                                     command=lambda k=command: self.run_command(
                                                         service_item['commands'][k], service_item['path'], command_text_boxes[k]))

            label_run_service_button.pack(side="left", padx=10)

            command_text_boxes[command] = ctk.CTkTextbox(command_frame, width=400, height=300)
            command_text_boxes[command].pack(pady=20, padx=20)

    def run_command(self, command, path, output_textbox):
        print(output_textbox)
        def target():
            full_command = f'cd {path} && {command}'
            process = subprocess.Popen(full_command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

            output_textbox.delete(1.0, ctk.END)  # Clear previous output

            while True:
                output = process.stdout.readline()
                if output == '' and process.poll() is not None:
                    break
                if output:
                    output_textbox.insert(ctk.END, output)
                    output_textbox.see(ctk.END)  # Scroll to the end

            err = process.stderr.read()
            if err:
                output_textbox.insert(ctk.END, "\nError:\n" + err)
                output_textbox.see(ctk.END)  # Scroll to the end

        threading.Thread(target=target).start()

