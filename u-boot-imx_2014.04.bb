# Copyright (C) 2013, 2014 Freescale Semiconductor

DESCRIPTION = "Bootloader for i.MX platforms"
require recipes-bsp/u-boot/u-boot.inc

PROVIDES += "u-boot"

LICENSE = "GPLv2+"
LIC_FILES_CHKSUM = "file://Licenses/gpl-2.0.txt;md5=b234ee4d69f5fce4486a80fdaf4a4263"

SRC_URI = "file://u-boot-imx.tar.gz"
SRCREV = "RTX_V2015.04"

S = "${WORKDIR}/u-boot-imx"

PACKAGE_ARCH = "${MACHINE_ARCH}"
COMPATIBLE_MACHINE = "(mx6)"
