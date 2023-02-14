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
       "Review": Review}


class HBNBCommand(cmd.Cmd):
    """main loop for commands"""
    prompt = "(hbnb) "

    res = ["created_at", "updated_at", "id"]

    def do_quit(self, line):
        """exits loop for quit"""
        raise SystemExit

    def do_EOF(self, line):
        """exits loop for EOF"""
        raise SystemExit

    def emptyline(self):
        """nothing for no input"""
        pass

    def do_create(self, line):
        if len(line) == 0:
            print("** class name missing **")
        elif line in cls.keys():
            new = cls[line]()
            new.save()
            print(new.id)
        else:
            print("** class doesn't exist **")

    def do_show(self, line):
        list_args = line.split(" ")
        if len(line) == 0:
            print("** class name missing **")
        elif list_args[0] in cls.keys():
            if len(list_args) == 1:
                print("** instance id missing **")
            else:
                obj_search = list_args[0] + "." + list_args[1]
                obj_all = storage.all()
                if obj_search in obj_all:
                    print(str(obj_all[obj_search]))
                else:
                    print("** no instance found **")
        else:
            print("** class doesn't exist **")

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
        args = line.split(maxsplit=3)
        num_args = len(args)
        if num_args < 4:
            if num_args == 0:
                print("** class name missing **")
                return
            elif num_args == 1:
                print("** instance id missing **")
                return
            elif num_args == 2:
                print("** attribute name missing **")
                return
            elif num_args == 3:
                print("** value missing **")
                return
        if args[0] not in HBNBCommand.cls_lst:
            print("** class doesn't exist **")
            return
        key = "{}.{}".format(args[0], args[1])
        target = storage.all().get(key)
        if target is None:
            print("** no instance found **")
            return
        if args[2] in HBNBCommand.res_att:
            return
        try:
            setattr(target, args[2], eval(args[3]))
        except Exception as er:
            print(er)


if __name__ == "__main__":
    HBNBCommand().cmdloop()
