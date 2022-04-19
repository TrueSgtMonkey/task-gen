from save_file_handler import __global_task_dict

def main():
    inpoot = ""
    task = ""
    task_contents = ""
    print("DIRECTIONS:")
    print("Format -> \"task:task_contents\"")
    print("type nothing to create a new task\n")
    while True:
        inpoot = input(task)
        if len(inpoot) > 0:
            # only update task if task has been reset (is empty)
            # keeps user from re-typing tasks
            if len(task) == 0:
                task = get_task_from_str(inpoot)

                # only needs to be checked when task is updated
                if task.find(":") == -1:
                    task = inpoot + ":"
                    continue
                
                task_contents = get_task_contents_from_str(inpoot)
            else:
                task_contents = inpoot
            if not(task in __global_task_dict):
                __global_task_dict[task] = task_contents
            else:
                __global_task_dict[task] += "\n" + (" " * len(task)) + task_contents
        else:
            task = ""

# everything before and including the semi-colon
def get_task_from_str(s):
    if not(type(s) is str):
        return
    
    # returning the substring until ':' is found
    # returns empty string if no ":" found (due to +1)
    return s[0 : s.find(":")+1]

# everything after the semi-colon
def get_task_contents_from_str(s):
    if not(type(s) is str):
        return

    return s[s.find(":")+1 : len(s)]

if __name__ == '__main__':
    main()