# ~/.profile: executed by Bourne-compatible login shells.

if [ "$BASH" ]; then
  if [ -f ~/.bashrc ]; then
    . ~/.bashrc
  fi
fi

if [ -f /tmp/update.lock ]; then
    rm /tmp/update.lock
fi

if [ -x /root/update.sh ]; then
  /root/update.sh
  rm /root/update.sh
fi

if [ -x /mnt/sda1/update.sh ]; then
  /mnt/sda1/update.sh
  touch /tmp/update.lock
fi

if [ ! -f /tmp/update.lock ]; then
    if [ -x /mnt/sdb1/update.sh ]; then
      /mnt/sdb1/update.sh
      touch /tmp/update.lock
    fi
fi

mesg n
