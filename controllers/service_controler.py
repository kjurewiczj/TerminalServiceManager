import pickle


class ServiceController:
    @staticmethod
    def save_service(self, service_name, path, commands):
        for command in commands:
            commands[command] = commands[command].get()

        try:
            with open('servicePickle', 'rb') as dbfile:
                db = pickle.load(dbfile)
        except (FileNotFoundError, EOFError):
            db = {}
        data = {
            'service_name': service_name,
            'path': path,
            'commands': commands
        }
        db[service_name] = data

        with open('servicePickle', 'wb') as dbfile:
            pickle.dump(db, dbfile)

        dbfile.close()
