#!/bin/bash
lsblk
echo "please enter drive letter (sdX)"
read drivenum
date=$(date)
whoami=$(whoami)
echo "Name: $whoami Date: $date Drive: $drivenum" >> /var/log/zer0fill/drivelog.txt
sudo dd if=/dev/zero if=/dev/$drivenum bs=1M > /dev/null
