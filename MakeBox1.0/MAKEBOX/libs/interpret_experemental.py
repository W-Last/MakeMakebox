import libs.ama

def pyrun(path):
    libs.ama.set_print("Warning : Do you realy want to use experemtal version?", "YELLOW")
    input("Y/N : ")
    if input == "Y":      
        with open(path, "r") as file:
            exec(file.read())
    else:
        breakpoint()