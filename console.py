#!/usr/bin/python3
import cmd
import ast
import shlex
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
"""Creates a simple console"""


class HBNBCommand(cmd.Cmd):
    """Defines the the HBNBCommand command interpreter"""
    prompt = "(hbnb) "
    className = {"BaseModel": BaseModel, "User": User, "State": State,
                 "City": City, "Amenity": Amenity, "Place": Place,
                 "Review": Review}

    def do_quit(self, args):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, args):
        """quit when ctrl+d is pressed"""
        print()
        return True

    def do_create(self, args):
        """Creates a new instance of BaseModel"""
        if not args:
            print("** class name missing **")
        elif args not in HBNBCommand.className.keys():
            print("** class doesn't exist **")
        else:
            obj = HBNBCommand.className[args]()
            obj.save()
            print(obj.id)

    def do_show(self, args):
        ("""Prints the string representation of an instance based on the
class name and id""")
        if not args:
            print("** class name missing **")
        else:
            argsList = args.split()
            if argsList[0] not in HBNBCommand.className.keys():
                print("** class doesn't exist **")
            elif len(argsList) == 1:
                print("** instance id missing **")
            else:
                key = "{}.{}".format(argsList[0], argsList[1])
                if key not in storage.all().keys():
                    print("** no instance found **")
                else:
                    print(storage.all()[key])

    def do_destroy(self, args):
        ("""Deletes an instance based on the class name and id
(save the change into the JSON file)""")
        if not args:
            print("** class name missing **")
        else:
            argsList = args.split()
            if argsList[0] not in HBNBCommand.className.keys():
                print("** class doesn't exist **")
            elif len(argsList) == 1:
                print("** instance id missing **")
            else:
                key = "{}.{}".format(argsList[0], argsList[1])
                if key not in storage.all().keys():
                    print("** no instance found **")
                else:
                    del storage.all()[key]
                    storage.save()

    def do_all(self, args):
        ("""Prints all string representation of all instances
based or not on the class name.""")
        if not args:
            all_objs = storage.all()
            all_strs = []
            for obj in all_objs.values():
                all_strs.append(str(obj))
            print(all_strs)
        else:
            if args not in HBNBCommand.className.keys():
                print("** class doesn't exist **")
            else:
                all_objs = storage.all()
                all_strs = []
                for key, obj in all_objs.items():
                    if key.startswith(args + '.'):
                        all_strs.append(str(obj))
                print(all_strs)

    def do_update(self, args):
        ("""Updates an instance based on the class name and id by adding or
updating attribute (save the change into the JSON file)""")
        if not args:
            print("** class name missing **")
        else:
            argsList = shlex.split(args)
            argsList_len = len(argsList)
            if argsList[0] not in HBNBCommand.className.keys():
                print("** class doesn't exist **")
            elif argsList_len == 1:
                print("** instance id missing **")
            elif argsList_len > 1:
                key = "{}.{}".format(argsList[0], argsList[1])
                if key not in storage.all().keys():
                    print("** no instance found **")
                elif argsList_len == 2:
                    print("** attribute name missing **")
                elif argsList_len == 3:
                    print("** value missing **")
                else:
                    obj = storage.all()[key]
                    try:
                        if argsList[3].isdigit():
                            argsList[3] = int(argsList[3])
                        elif argsList[3].replace('.', '', 1).isdigit():
                            argsList[3] = float(argsList[3])
                    except AttributeError:
                        pass
                    setattr(obj, argsList[2], argsList[3])
                    obj.save()

    def default(self, line):
        """Handles commands that are not defined"""
        argsList = line.split('.', 1)
        if argsList[0] in HBNBCommand.className.keys():
            if argsList[1] == 'all()':
                self.do_all(argsList[0])
            elif argsList[1] == 'count()':
                HBNBCommand.count_objs(argsList[0])
            elif argsList[1].split('(')[0] == 'show':
                key = argsList[0]+' '+argsList[1].split('("')[1].strip('")')
                self.do_show(key)
            elif argsList[1].startswith(
                    'destroy(') and argsList[1].endswith(')'):
                arg = argsList[0]+' '+argsList[1].split('("')[1].strip('")')
                self.do_destroy(arg)
            elif argsList[1].split('(')[0] == 'update':
                arg0 = argsList[0]
                if ', ' in argsList[1]:
                    if '{' in argsList[1] and ':' in argsList[1]:
                        arg1 = (argsList[1].split('(')[1].strip(')').
                                split(', ', 1)[0])
                        attr_dict = (ast.literal_eval(argsList[1].split('(')[1]
                                     .strip(')').split(', ', 1)[1]))
                        for key, value in attr_dict.items():
                            self.do_update(arg0 + ' ' + arg1 + ' ' + key +
                                           ' ' + str(value))
                        return
                    temp = argsList[1].split('(')[1].strip(')').split(', ')
                    if len(temp) == 3:
                        arg1 = temp[0]
                        arg2 = temp[1]
                        arg3 = temp[2]
                        self.do_update(arg0+' '+arg1+' '+arg2+' '+arg3)
        else:
            cmd.Cmd.default(self, line)

    def emptyline(self):
        """Go to next line and print prompt when enter pressed"""
        pass

    @staticmethod
    def count_objs(class_name):
        """count the number of instances of a class"""
        count = 0
        all_objs = storage.all()
        for key in all_objs.keys():
            if key.startswith(class_name + '.'):
                count += 1
        print(count)


if __name__ == "__main__":
    HBNBCommand().cmdloop()
