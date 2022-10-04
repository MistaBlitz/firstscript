#!/bin/bash
lsblk
echo "please enter drive letter (sdX)"
read drivenum
echo "are you sure you want to wipe $drivenum? y/n"
read check
# checking if user input is correct
if [ "${check}" == "n" ];
then
	echo "user responded no"
	 exit
# checking if user input is correct
elif [ "${check}" == "y" ];
then
	# setting date variable to todays date
	date=$(date)
	# setting whoami variable to user running script
	whoami=$(whoami)
	# writing information to log file
	#echo "Name: $whoami Date: $date Drive: $drivenum" >> /var/log/zer0fill/drivelog.txt
	# run command to zero fill drive selected
	sudo dd if=/dev/zero if=/dev/$drivenum bs=1M > /dev/null
# if user doesn't respond with y or n script ends
else
	echo "user input did not match y or n"
	exit
fi
exit
