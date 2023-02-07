#!/usr/bin/python3
"""console"""
import cmd
import models
from models.base_model import BaseModel
from models import storage
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review

cls = {"BaseModel": BaseModel,
       "User": User,
       "State": State,
       "City": City,
       "Amenity": Amenity,
       "Place": Place,
       "Review": Review
       }


class HBNBCommand(cmd.Cmd):
    """main loop for commands"""
    prompt = "(hbnb) "

    def do_quit(self, args):
        """exits loop for quit"""
        raise SystemExit

    def do_EOF(self, args):
        """exits loop for EOF"""
        raise SystemExit

    def emptyline(self):
        """nothing for no input"""
        pass

    def do_create(self, line):
        arg_str = line.split()
        if len(arg_str) == 0:
            print("** class name missing **")
            return
        if line not in HBNBCommand.cls_lst:
            print("** class doesn't exist **")
            return
        try:
            cls = eval(line)()
            cls.save()
            print(cls.id)
            return
        except (NameError, AttributeError):
            pass

    def do_show(self, line):
        if line == "":
            print("** class name missing **")
            return
        args = line.split()
        if len(args) < 2:
            print("** instance id missing **")
            return
        class_name, iid = args[0], args[1]
        if class_name not in HBNBCommand.cls_lst:
            print("** class doesn't exist **")
            return
        objects = models.storage.all()
        key = "{}.{}".format(class_name, iid)
        if key not in objects:
            print("** no instance found **")
            return
        obj = objects[key]
        print(obj)

    def do_destroy(self, line):
        if not line:
            print("** class name missing **")
            return
        args = line.split()
        if len(args) < 2:
            print("** instance id missing **")
            return
        cname, uwuid = args[0], args[1]
        if cname not in HBNBCommand.cls_lst:
            print("** class doesn't exist **")
            return
        target = "{}.{}".format(cname, uwuid)
        if target not in storage.all().keys():
            print("** no instance found **")
            return
        stor_rich = storage.all()
        del stor_rich["{}.{}".format(cname, uwuid)]
        storage.save()
        return

    def do_all(self, line):
        if len(line) == 0:
            for key in storage.all():
                print([str(storage.all()[key])])
        elif line not in cls.keys():
            print("** class doesn't exist **")
        else:
            for key, value in storage.all().items():
                key_arg = key.split(".")
                if line == key_arg[0]:
                    print([str(storage.all()[key])])

    def do_update(self, line):
        list_args = line.split(" ")
        if len(line) < 1:
            print("** class name missing **")
        elif len(list_args) < 2:
            print("** instance id missing **")
        elif len(list_args) < 3:
            print("** attribute name missing **")
        elif len(list_args) < 4:
            print("** value missing **")
        elif list_args[0] not in cls.keys():
            print("** class doesn't exist **")
        else:
            obj_search = list_args[0] + "." + list_args[1]
            obj_all = storage.all()
            if obj_search in obj_all:
                setattr(obj_all[obj_search], list_args[2],
                        list_args[3].strip('\'"'))
            else:
                print("** no instance found **")


if __name__ == "__main__":
    HBNBCommand().cmdloop()
