print("Starting")
import time

time.sleep(0.45)

print("  -Object:ama ")
try:
    import libs.ama
except(ImportError):
    print("Error Cannot find library")
print("next")

print("  -Object:ftc ")
try:
    import libs.ftc
except(ImportError):
    print("Error Cannot find library")
print("next")

print("  -Object:ftb ")
try:
    import libs.ftb
except(ImportError):
    print("Error Cannot find library")
print("next")

print("  -Object:suremi ")
try:
    import libs.suremi
except(ImportError):
    print("Error Cannot find library")
print("next")

print("  -Object:interpret ")
try:
    import libs.interpret_experemental
except(ImportError):
    print("Error Cannot find library")
print("next")


time.sleep(0.45)

libs.ama.set_print("""
___  ___  ___   _   __ ________  ___      _         ______           
|  \/  | / _ \ | | / /|  ___|  \/  |     | |        | ___ \          
| .  . |/ /_\ \| |/ / | |__ | .  . | __ _| | _____  | |_/ / _____  __
| |\/| ||  _  ||    \ |  __|| |\/| |/ _` | |/ / _ \ | ___ \/ _ \ \/ /
| |  | || | | || |\  \| |___| |  | | (_| |   <  __/ | |_/ / (_) >  <_________
\_|  |_/\_| |_/\_| \_/\____/\_|  |_/\__,_|_|\_\___| \____/ \___/_/\__________| v1.0
[ with MakeMake License ]                                                                     
                                                                     """, "YELLOW")

while True:
    inp = input("  >")

    match inp:
        case _ if inp.startswith("mkdir(") and inp.endswith(")"):
            path_and_name = inp[6:-1]
            if "," in path_and_name:
                path, name = map(str.strip, path_and_name.split(",", 1))
                libs.suremi.mkd(name, path)
                libs.ama.set_print("Done", "BLUE")
            else:
                libs.ama.set_print("Error : Use mkdir(path, name)", "RED")

        case _ if inp.startswith("mkfil(") and inp.endswith(")"):
            path_and_name = inp[6:-1]
            if "," in path_and_name:
                path, name = map(str.strip, path_and_name.split(",", 1))
                libs.suremi.mkf(name, path)
            else:
                libs.ama.set_print("Error : Use mkfil(path, name)", "RED")

        case _ if inp.startswith("cd(") and inp.endswith(")"):
            path = inp[3:-1].strip()
            libs.suremi.cd(path)

        case _ if inp.startswith("ls(") and inp.endswith(")"):
            path = inp[3:-1].strip()
            print(libs.suremi.ls())
        
        case _ if inp.startswith("rm(") and inp.endswith(")"):
            path = inp[3:-1].strip()
            print(libs.suremi.rm(path))

        case _ if inp.startswith("echo(") and inp.endswith(")"):
            str = inp[5:-1].strip()
            print(libs.ama.set_print(str, "BLUE"))

        case _ if inp.startswith("prt(") and inp.endswith(")"):
            str = inp[4:-1].strip()
            print(libs.ama.set_print(str, "NONE"))

        case _ if inp.startswith("err(") and inp.endswith(")"):
            str = inp[4:-1].strip()
            print(libs.ama.set_print(str, "RED"))

        case _ if inp.startswith("acp(") and inp.endswith(")"):
            str = inp[4:-1].strip()
            print(libs.ama.set_print(str, "GREEN"))

        case _ if inp.startswith("pyrun(") and inp.endswith(")"):
            path = inp[6:-1].strip()
            print(libs.interpret_experemental.pyrun(path))

        case _ if inp.startswith("shutdown()"):
            break

        case _:
            libs.ama.set_print("Error : Unknown command", "RED")