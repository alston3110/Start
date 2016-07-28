# Copyright (C) 2013-2015 Freescale Semiconductor
# Released under the MIT license (see COPYING.MIT for the terms)

SUMMARY = "Linux Kernel provided and supported by Freescale"
DESCRIPTION = "Linux Kernel provided and supported by Freescale with focus on \
i.MX Family Reference Boards. It includes support for many IPs such as GPU, VPU and IPU."

require recipes-kernel/linux/linux-imx.inc
require recipes-kernel/linux/linux-dtb.inc

DEPENDS += "lzop-native bc-native"

SRC_URI = "file://linux-imx-3.14.28.tar.gz"
S = "${WORKDIR}/linux-imx-3.14.28"
DEFAULT_PREFERENCE = "1"
SCMVERSION = "n"

addtask copy_defconfig after do_unpack before do_configure
do_copy_defconfig () {
    # copy latest imx_v7_defconfig to use
    if [ -f ${WORKDIR}/defconfig ] ; then
        cp -f ${WORKDIR}/defconfig ${B}/.config
    else
        cp -f ${S}/arch/arm/configs/imx_v7_defconfig ${B}/.config
        cp -f ${S}/arch/arm/configs/imx_v7_defconfig ${B}/../defconfig
    fi
    
    ln -s ${S}/include/dt-bindings ${S}/arch/arm/boot/dts/include/dt-bindings
}

COMPATIBLE_MACHINE = "(mx6)"
