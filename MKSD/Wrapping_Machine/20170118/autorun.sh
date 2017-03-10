#! /bin/sh

MYPATH=`pwd`
DEVNODE="/dev/mmcblk0"

print() {
	echo $1 > /dev/ttymxc3
#	echo $1 > /dev/tty1
}

run_end() {
	print "update Fail!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!"
	exit 0
}

umount_sd()
{
	mounted=$(mount | grep $DEVNODE | awk '{print $1}' | wc -l)
    if [ $mounted -gt 0 ]; then
		todo=$(mount | grep $DEVNODE | awk '{print $1}')
        for i in $todo
			do
                echo $i
				umount $i
                sleep 1
			done
	fi
}

do_change_uid_gid() {
	chown $1:$2 $3
	uid=`stat -c '%u' $3`
	gid=`stat -c '%g' $3`
	if [ "$uid" != "$1" ] ; then
	    print "change uid $1 fail. get the uid is $uid"
	fi
	if [ "$gid" != "$2" ] ; then
	    print "change gid $2 fail. get the uid is $gid"
	fi
}

run() {

touch /tmp/restart
print "disable mcu watchdog"
/data/wdgdis

mount /dev/mmcblk0p1 /mnt

print "update system start........."

print "judge /mnt/etc/udev/rules.d/92-nvnfc.rules"

# BSP 1.2
#file/folder                                 uid gid mode
#-------------------------------------------+---+---+----
#/usr/bin/dotlockfile                        0     8 2755
#/usr/bin/mail-lock                          0     8 2755 
#/usr/bin/mail-touchlock                     0     8 2755 
#/usr/bin/mail-unlock                        0     8 2755
#/usr/lib/dbus-1.0/dbus-daemon-launch-helper 0   105 4754
#/var/log/btmp                               0    43 0660
#/var/log/lastlog                            0    43 0664
#/var/log/wtmp                               0    43 0664
#/var/mail                                   0     8 2755

# BSP 1.3
#file/folder                                 uid gid mode
#-------------------------------------------+---+---+----
#/usr/bin/dotlockfile                        0     8 2755
#/usr/bin/mail-lock                          0     8 2755 
#/usr/bin/mail-touchlock                     0     8 2755 
#/usr/bin/mail-unlock                        0     8 2755
#/usr/lib/dbus-1.0/dbus-daemon-launch-helper 0   105 4754
#/var/log/btmp                               0    43 0660
#/var/log/btmp.1                             0    43 0660
#/var/log/lastlog                            0    43 0664
#/var/log/wtmp                               0    43 0664
#/var/log/wtmp.1                             0    43 0664
#/var/mail                                   0     8 2755


if [ -f /mnt/etc/udev/rules.d/92-nvnfc.rules ] ; then
	print "It's BSP_1.3 System "
	do_change_uid_gid 0 8 /mnt/usr/bin/dotlockfile
	do_change_uid_gid 0 8 /mnt/usr/bin/mail-lock
	do_change_uid_gid 0 8 /mnt/usr/bin/mail-touchlock
	do_change_uid_gid 0 8 /mnt/usr/bin/mail-unlock
	do_change_uid_gid 0 105 /mnt/usr/lib/dbus-1.0/dbus-daemon-launch-helper
	do_change_uid_gid 0 43 /mnt/var/log/btmp
	do_change_uid_gid 0 43 /mnt/var/log/btmp.1
	do_change_uid_gid 0 43 /mnt/var/log/lastlog
	do_change_uid_gid 0 43 /mnt/var/log/wtmp
	do_change_uid_gid 0 43 /mnt/var/log/wtmp.1
	do_change_uid_gid 0 8 /mnt/var/mail
else
	print "It's BSP_1.2 System "
	do_change_uid_gid 0 8 /mnt/usr/bin/dotlockfile
	do_change_uid_gid 0 8 /mnt/usr/bin/mail-lock
	do_change_uid_gid 0 8 /mnt/usr/bin/mail-touchlock
	do_change_uid_gid 0 8 /mnt/usr/bin/mail-unlock
	do_change_uid_gid 0 105 /mnt/usr/lib/dbus-1.0/dbus-daemon-launch-helper
	do_change_uid_gid 0 43 /mnt/var/log/btmp
	do_change_uid_gid 0 43 /mnt/var/log/lastlog
	do_change_uid_gid 0 43 /mnt/var/log/wtmp
	do_change_uid_gid 0 8 /mnt/var/mail
fi

sync

chmod 2755 /mnt/usr/bin/dotlockfile
chmod 2755 /mnt/usr/bin/mail-lock
chmod 2755 /mnt/usr/bin/mail-touchlock
chmod 2755 /mnt/usr/bin/mail-unlock
chmod 4754 /mnt/usr/lib/dbus-1.0/dbus-daemon-launch-helper
chmod 2755 /mnt/var/mail

sync
#mv /data/check_code /data/check_code-finish
} > /dev/ttymxc3

run

print "update system finished......(For $version)"


