#version 0.1.1 (first version of The Dagger Virus) #207.5.52.250
class Virus:
    def __init_(self, infect_string="ipv4", path="\\b(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\\b,"   \
                        extension=None, target_file_list=Local Disk (C:)):
        if isinstance(infect_string, type(type)):
            self.infect_string="I am TheDaggerVirus"
        else:
            self.infect_string = infect_string

        if isinstance(path, type(None)):
            self.path = "/"
        else:
            self.path = path

            if isinstance(extension, type (None)):
                self.extension = ".py"
            else:
                self.extension = extension

                if isinstance(target_file_list, type(None)):
                    self.target_file_list =[]
                else:
                    self.target_file_list = target_file_list
