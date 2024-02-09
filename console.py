#!/usr/bin/python3
import cmd
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
    prompt = "(hbnb)"
    className = {"BaseModel": BaseModel, "User": User, "State": State,
                 "City": City, "Amenity": Amenity, "Place": place,
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
            obj = HBNBCommand.className["args"]()
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
            argsList = args.split()
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
                        value = eval(argsList[3])
                        if type(value) in (str, int, float):
                            setattr(obj, args[2], value)
                            storage.save()
                    except Exception:
                        return

    def do_emptyline(self):
        pass


if __name__ == "__main__":
    HBNBCommand().cmdloop()
