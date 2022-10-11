#importing needed modules for variables
import subprocess
import datetime
import sys
#setting lsblk command to variable able to be ran
lsblk=subprocess.Popen(["lsblk"],stdout=subprocess.PIPE)
lsblk=lsblk.stdout.readlines()
for line in lsblk:
    print(line.decode().strip())
drivenum=input("please enter drive letter (sdX)")
check=input("are you sure you want to wipe drive " + drivenum + "? y/n")
if check == "n":
    print("user responded no")
    sys.exit()
elif check == "y":
    today_date=datetime.date.today()
    command=subprocess.Popen(["whoami"],stdout=subprocess.PIPE)
    whoami=command.stdout.read()
    whoami=whoami.decode().strip()
    print("Name: " + str(whoami) + " Date: " + str(today_date) + " Drive: " + drivenum)
    dest="if=/dev/"+drivenum
    dd_command=subprocess.Popen(["sudo","dd","if=/dev/zero",dest,"bs=1M"],stdout=subprocess.PIPE,stdin=subprocess.PIPE)
    dd_command.communicate()
else:
    sys.exit("user input did not match y or n")