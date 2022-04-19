import atexit

__global_task_dict = {}

def output_dict_as_file():
    file_name = input("save file as: ")

    # by default, saves as .txt file
    if file_name.find(".") == -1:
        file_name += ".txt"
    
    with open(file_name, "w") as ext_file:
        for key in __global_task_dict:
            ext_file.write("\n-------" + key[0:len(key)-1] + "------\n")
            ext_file.write(key + __global_task_dict[key])
            ext_file.write("\n-------" + key[0:len(key)-1] + "------\n")

def exit_handler():
    output_dict_as_file()

atexit.register(exit_handler)