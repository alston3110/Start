#! /bin/sh

DIR=$0
CURDIR=${DIR%/*}
MP_TOOLS=${CURDIR}/mp-tools

chmod 777 -R ${MP_TOOLS}/tools

write_xinitrc_config(){
	echo "echo 0 > /sys/class/graphics/fb4/blank" 
	echo "echo 0 > /sys/class/graphics/fb2/blank"
	echo "echo 0 > /sys/class/graphics/fb0/blank"
	echo "cd ${MP_TOOLS}"
	echo "./mp-tools.py"
} > ${MP_TOOLS}/.xinitrc

write_xinitrc_config
cp ${MP_TOOLS}/.xinitrc /root/

startx &

