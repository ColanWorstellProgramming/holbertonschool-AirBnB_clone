#!/usr/bin/python3
"""console"""
import cmd


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

    def do_create(self, args):
        """creates new BaseModel"""
        if (len(args) == 0):
            print("** class name missing **")
        elif (args in valid_class.keys()):
            x = valid_class[args]()
            x.save()
            print(x.id)
        else:
            print("** class doesn't exist **")

    def do_show(self, args):
        """shows information"""
        if (len(args) == 0):
            print("** class name missing **")
        elif (args in valid_class.keys()):
            if len(list_args) == 1:
                print("** instance id missing **")
        else:
            print("** class doesn't exist **")

if __name__ == "__main__":
    HBNBCommand().cmdloop()
