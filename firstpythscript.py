# importing needed modules for variables
import subprocess
import datetime
import sys

# setting lsblk command to variable able to be ran
lsblk = subprocess.Popen(["lsblk"], stdout=subprocess.PIPE)
lsblk = lsblk.stdout.readlines()
for line in lsblk:
    print(line.decode().strip())
# setting drivenumb variable and taking input
drivenum = input("please enter drive letter (sdX)")
# checking user input
check = input("are you sure you want to wipe drive " + drivenum + "? y/n")
# if user responds with n, script ends
if check == "n":
    print("user responded no")
    sys.exit()
# if user responds with y, script runs
elif check == "y":
    # setting variables
    today_date = datetime.date.today()
    command = subprocess.Popen(["whoami"], stdout=subprocess.PIPE)
    whoami = command.stdout.read()
    whoami = whoami.decode().strip()
    print("Name: " + str(whoami) + " Date: " + str(today_date) + " Drive: " + drivenum)
    dest = "if=/dev/" + drivenum
    # running zerofill command
    dd_command = subprocess.Popen(
        ["sudo", "dd", "if=/dev/zero", dest, "bs=1M"],
        stdout=subprocess.PIPE,
        stdin=subprocess.PIPE,
    )
    dd_command.communicate()
else:
    # if user doesn't respond with y or n, script ends
    sys.exit("user input did not match y or n")
