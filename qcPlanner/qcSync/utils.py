import errno
import csv
import json
import yaml
import sys
from pathlib import Path
import os
import datetime

class Utils():
    def __init__(self):
        pass

    @staticmethod
    def checkFileInput(filename, control_list=None):
        if control_list is None:
            control_list = [".json", ".txt", ".yaml"]
        filename = os.path.normpath(filename)
        while not os.path.isfile(filename) or Path(filename).suffix not in control_list:
            filename = input("Fichier non valide, réessayez: ")
        return filename
    
    @staticmethod
    def checkPathInput(pathname):
        while not os.path.exists(pathname):
            pathname = input("Chemin non valide, réessayez: ")
        return pathname
    
    @staticmethod
    def checkNumericInput( nb, lb, ub):

        while not nb.isnumeric() or nb.isnumeric() and nb not in list(map(str,range(lb, ub+1))):
            nb = input("Entrer un nombre entre {} et {}: ".format(lb,ub))
        return int(nb)
    
    @staticmethod
    def checkNumberInput( nb):

        while not nb.isnumeric():
            nb = input("Entrer un nombre\n")
        return nb

    @staticmethod
    def checkCharInput(char, control_list):

        while not char in control_list:
            char = input("Choisissez une option entre {} ".format(control_list))
        return char
    
    @staticmethod
    def loadYaml(filename):

        """
        Load Yaml file and return a dict
        """
        filename = os.path.normpath(filename)
        myDict = dict()
        try:
            with open(filename,'r') as file:    
                myDict = yaml.load(file,Loader=yaml.BaseLoader)
        except FileExistsError:
            raise FileExistsError("File error")
        except FileNotFoundError:
            raise FileNotFoundError("File not found")
        except yaml.YAMLError as e:
            print(e)
        return myDict
    
    @staticmethod
    def dumpYaml(myDict,filename):
        filename = os.path.normpath(filename)
        try:
            with open(filename, 'w') as f:
                yaml.dump( myDict,f)
        except yaml.YAMLError as e:
            print(e)
        except:
            print('Something went wrong!')
            sys.exit(0) 
        print("Le fichier de sortie est {}".format(filename))
        
    @staticmethod
    def GetNumberCustomers(filename):
        """
        Get total number of customers
        """
        filename = os.path.normpath(filename)
        try:
            if os.stat(filename).st_size == 0:
                return 0
        
            if Path(filename).suffix in ".yaml":
                    client = Utils.loadYaml(filename)
            elif Path(filename).suffix in ".json":
                client = Utils.loadJson(filename)
            elif Path(filename).suffix in ".txt":
                client = Utils.loadText(filename)

            return len(client)
        except FileNotFoundError:
                print('{} n\'existe pas!\n'.format(filename))

    @staticmethod
    def loadJson(filename):
        """
        Save a dictionary in json format
        """
        filename = os.path.normpath(filename)
        data = dict()
        with open(filename, 'w') as outfile:
            json.dump(data, outfile)
        return data

    @staticmethod
    def dumpJson(argv,filename):
        """
        Record a new client in a json file format
        {id:[name,adress, code postal, []]}
        """
        filename = os.path.normpath(filename)
        argv.append([])
        if os.stat(filename).st_size == 0:
            data = {"1":argv}
            Utils.loadJson(filename,data)
            NB_CLIENTS = NB_CLIENTS + 1
        else:
            try:
                size_dict = 0
                clients = {}
                with open(filename,'r') as f:
                    clients = json.load(f)
                    size_dict = len(clients) + 1
                    clients[size_dict] = argv
                    Utils.loadJson(filename,clients)

            except FileNotFoundError:
                print('{} n\'existe pas!\n'.format(filename))
            except PermissionError:
                print('L\'accès à {} n\'est pas permis!\n'.format(filename))
            except json.decoder.JSONDecodeError:
                print( "Expecting value: line 1 column 1 (char 0)")
    
    @staticmethod
    def updateJson(matrix,filename):
        """
        Edit clients record in the json file ( add distance matrix)
        {id:[name,adress, code postal, []]}
        """
        filename = os.path.normpath(filename)
        if os.stat(filename).st_size == 0:
            return r'Veuillez ajouter des clients à la base de données'
        else:
            try:
                clients = {}
                with open(filename,'r') as f:
                    clients = json.load(f)
                    for id, values in clients.items():
                        values[len(values)-1]= matrix[int(id)-1]
                    Utils.dumpJson(filename,clients)

            except FileNotFoundError:
                print('{} n\'existe pas!\n'.format(filename))
            except PermissionError:
                print('L\'accès à {} n\'est pas permis!\n'.format(filename))
            except json.decoder.JSONDecodeError:
                print( "Expecting value: line 1 column 1 (char 0)")

    @staticmethod
    def loadText(filename):
        pass

    @staticmethod
    def dumpCsv(myDict, *args, filename, append=False):
        """
            Enregistrer les paramètres et les solutions au format csv
        """
        list_values = list(myDict.items())[0: len(myDict.values()) - 1]
        list_content = [val[1] for val in list_values]
        list_content.append(f'{args[0]}')
        list_content.append(f'{args[1]}')

        content = ','.join(map(str,list_content))
        
        list_headers = [val[0] for val in list_values]
        list_headers.append('status')
        list_headers.append('obj_val')
        headers = ','.join(map(str,list_headers))
    
        filename = os.path.normpath(filename)

        if append:
            try:
                with Utils.safe_open(filename, 'a') as f:
                    f.write('\n')
                    f.write(content)        
            except:
                print('Something went wrong!')
                sys.exit(0) 
        else:
            try:
                with Utils.safe_open(filename, 'w') as f:
                    f.write(headers+'\n')
                    f.write(content)        
            except:
                print('Something went wrong!')
                sys.exit(0) 
        
        print("Le fichier résultat est {}".format(filename))

    @staticmethod
    def mkdir_p(path):
        # Reference:
        # http://stackoverflow.com/questions/600268/mkdir-p-functionality-in-python
        try:
            os.makedirs(path)
        except OSError as exc:  # Python >2.5
            if exc.errno == errno.EEXIST and os.path.isdir(path):
                pass
            else:
                raise
    
    @staticmethod
    def safe_open(
            path,
            mode):
        # Reference:
        # http://stackoverflow.com/questions/23793987/python-write-file-to-directory-doesnt-exist

        Utils.mkdir_p(os.path.dirname(path))
        return open(path, mode)
