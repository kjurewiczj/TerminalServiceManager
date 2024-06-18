import json
import os


class ServiceController:
    @staticmethod
    def save_service(self, service_name, path, commands):
        for command in commands:
            commands[command] = commands[command].get()

        print(service_name, path, commands)
        data = {
            'service_name': service_name,
            'path': path,
            'commands': commands
        }

        if not os.path.exists('data'):
            os.makedirs('data')

        with open('data/' + service_name.replace(' ', '_') + '.json', 'w', encoding='utf-8') as file:
            json.dump(data, file, ensure_ascii=False, indent=4)
