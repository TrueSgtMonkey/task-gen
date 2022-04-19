import atexit

class TaskGlobals(object):
    # static variables needed for saving
    file_name = "task.txt"
    task_dict = {}

    # makes sure the name is not empty and creates task.txt if nothing is given.
    def set_file_name(name):
        if not(type(name) is str):
            return
        
        TaskGlobals.file_name = name
        if TaskGlobals.file_name == "":
            TaskGlobals.file_name = "task.txt"
        if TaskGlobals.file_name.find(".") == -1:
            TaskGlobals.file_name += ".txt"

TaskGlobals.file_name = ""

def output_dict_as_file():
    print(TaskGlobals.file_name + " or is it?")
    with open(TaskGlobals.file_name, "w") as ext_file:
        for key in TaskGlobals.task_dict:
            ext_file.write("\n-------" + key[0:len(key)-1] + "------\n")
            ext_file.write(key + TaskGlobals.task_dict[key])
            ext_file.write("\n-------" + key[0:len(key)-1] + "------\n")

def exit_handler():
    output_dict_as_file()

atexit.register(exit_handler)