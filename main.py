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
while True:
  cmd = input("\033[1;30;41m" + os.getcwd() + "\033[0;36;40m" + "~> ")
  cmddata = cmd.split()
  tempdata = ""
  if 'echo' in cmddata:
    cmddata.remove("echo")
    for i in range(len(cmddata)):
      tempdata = tempdata + cmddata[i] + " "
    print(tempdata)
    tempdata = ""