#!/bin/bash
lsblk
echo "please enter drive letter (sdX)"
read drivenum
echo "are you sure you want to wipe $drivenum? y/n"
read check
if [ "${check}" == "n" ];
then
	echo "answer no"
	 exit
elif [ "${check}" == "y" ];
then
	date=$(date)
	whoami=$(whoami)
	echo "Name: $whoami Date: $date Drive: $drivenum" >> /var/log/zer0fill/drivelog.txt
	sudo dd if=/dev/zero if=/dev/$drivenum bs=1M > /dev/null
else
	echo "error"
	exit
fi
exit
