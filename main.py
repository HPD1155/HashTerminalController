import platform as pt
import psutil as psu
import os


os.system("cls")
os.system('clear')

print("\033[0;32;40mArchitecture: " + "\033[1;36;40m" + pt.machine())
print("\033[0;32;40mOS: " + "\033[1;36;40m" + pt.platform())
print("\033[0;32;40mOS Version: " + "\033[1;36;40m" + pt.version())
print('\033[0;32;40mOS type: ' + "\033[1;36;40m" + pt.system())
print("\033[0;32;40mRam: " + "\033[1;36;40m" + str(psu.virtual_memory().total / (1024.0 ** 3))+" GB")
print("\033[0;32;40mCPU: " + "\033[1;36;40m" + str(psu.cpu_count(logical=False)))
print("\033[0;32;40mCPU Logical: " + "\033[1;36;40m" + str(psu.cpu_count(logical=True)))
print("\033[0;35;40m")
print("############             ############")
print("  ##########             ##########  ")
print("   #########             #########   ")
print("    ########             ########    ")
print("     #######             #######     ")
print("     ###########################     ")
print("     ###########################     ")
print("     ###########################     ")
print("     #######             #######     ")
print("    ########             ########    ")
print("   #########             #########   ")
print("  ##########             ##########  ")
print("############             ############")

# Constant Data structures
commands = ['echo', 'cd', 'DIR', 'mke']


while True:
  print("")
  cmd = input("\033[1;30;41m" + os.getcwd() + "\033[0;36;40m" + "~> ")
  cmddata = cmd.split()
  tempdata = ""
  if cmddata[0] not in commands:
    print("\033[1;31;40m[Terminal Reader]: Command does not exist or was misspelled {Error Code: CMD01}")

  # random
  if 'echo' in cmddata:
    cmddata.remove("echo")
    for i in range(len(cmddata)):
      tempdata = tempdata + cmddata[i] + " "
    print(tempdata)
    tempdata = ""

  # Directory
  
  if 'cd' in cmddata:
    if(len(cmddata) == 1):
      print("\033[0;32;40m" + os.getcwd())
    else:
      if cmddata[1] == "<":
        os.chdir(os.getcwd()[0:len(os.getcwd()) - len(os.path.basename(os.getcwd()))])
      else:
        try:
          try:
            os.chdir(cmddata[1])
          except:
            os.chdir(os.getcwd() + cmddata[1])
        except:
          print("\033[1;31;40m[Terminal Reader]: Couldn't fetch your directory or perms have been denied! {Error Code: DIR01}")
  if 'DIR' in cmddata:
    if len(cmddata) == 1:
      for li in range(len(os.listdir(os.getcwd()))):
        print(os.listdir(os.getcwd())[li])
    elif(len(cmddata) == 2):
      for li in range(len(os.listdir(cmddata[1]))):
        print(os.listdir(cmddata[1])[li])
    else:
      print("\033[1;31;40m[Terminal Reader]: You need to give exact directory! {Error Code: DIR02}")
  if 'mke' in cmddata:
    try: 
      path = ""
      if len(cmddata) == 2:
        path = os.path.join(os.getcwd(), cmddata[1])
        os.mkdir(path, 0o666)
      else:
        print("\033[1;31;40m[Terminal Reader]: Invalid Arguments! {Error Code: DIR03}")
    except:
       print("\033[1;31;40m[Terminal Reader]: Failed to use name or create file {Error Code: DIR04}")
    