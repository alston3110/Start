<!DOCTYPE html>
<html>
<head>

</head>
<body>
1. 使用方法<br>
<br>
   usage: mk_update_sd [-h] [-l] [-n PROJECT] [-p PLATFORM] [-e {u-boot,setting}]<br>
<br>
   optional arguments:<br>
     -h, --help            show this help message and exit<br>
     -l, --list            list all support platform<br>
     -n PROJECT, --project PROJECT<br>
                           set the project name<br>
     -p PLATFORM, --platform PLATFORM<br>
                           set the platform<br>
     -e {u-boot,setting}, --edit {u-boot,setting}<br>
                           edit the setting or u-boot data<br>
<br>
2. 新增 platform<br>
   a) 在 platform 目錄下創建新的資料夾，資料夾的命名規則如下：<br>
<br>
      [PCBA Name]-emmc-[eMMC Version]-[DDR Label(Vendor)]-[DDR Size]<br>
<br>
      ex.<br>
          a6plus-emmc-5-micro-1g<br>
   b) 可從相近的 platform 拷貝資料，並針對自己的 platform 修改相關內容<br>
      ex.<br>
          b.1) 資料夾內容：<br>
<br>
          [info]<br>
              option.json<br>
          [system]<br>
              autorun.sh<br>
              check_code<br>
              efm32cmd<br>
              recovery.dtb<br>
              u-boot.imx<br>
              uImage-recovery<br>
              uramdisk-recovery.img<br>
          setting.dat<br>
          u-boot.dat<br>
<br>
          b.2) 將新的 platform 的相關資料取代，取代檔案列表如下：<br>
          [system]<br>
              recovery.dtb<br>
              uImage-recovery<br>
              u-boot.imx<br>
          b.3) 如果取代檔名一致或無新增燒錄檔案，則不需修改 [info]->option.json<br>
   c) 修改 u-boot 參數或 setting 資料(燒錄在外卡的，並不是要燒錄至emmc的參數)<br>
      ex.<br>
          ./mk_update_sd -e u-boot<br>
          ./mk_update_sd -e setting<br>
   d) 修改 option.json 下複製檔案的列表，如無須調整則不用修改<br>
<br>
3. 更改 .mk_update_sd.rc 檔案<br>
   a) 檔案內容，請更改 platform 和 zipfilename 的內容<br>
   ex.<br>
       a.1) 原內容<br>
           [Options]<br>
           platform=a6plus-emmc-5-micro-1g<br>
           zipfilename=rtx-a6plus-unknow<br>
       a.2) 更正後<br>
           [Options]<br>
           platform=a6-emmc-5-micro-1g<br>
           zipfilename=rtx-a6-ubuntu<br>
<br>
4. 準備燒錄內卡資料，將所有資料拷貝至 files/flash 目錄下<br>
<br>
5. 修改或新增 files 目錄下的 autorun.sh<br>
<br>
6. 執行 mk_update_sd 後會執行下列動作<br>
   a) 檢查 out 目錄是否存在，不存在則建立<br>
   b) 計算外卡所需的最小容量<br>
   c) 建立虛擬磁碟至 sys 目錄下 (sys/update.bin)<br>
   d) 依 platform/xxxxxx/info/option.json 下所設定的 unit 和 mbr 資訊，對虛擬磁碟做 partition 規劃<br>
   e) 格式化虛擬磁碟的 p1 為 fat32<br>
   f) 掛載虛擬磁碟的 p1 partition 至 out 目錄<br>
   g) 拷貝 platform/xxxxxx/info/option.json 下所設定的 cp-files 資訊(複製檔案列表)至 out 目錄下<br>
   h) 拷貝 files 下所有檔案至 out 目錄下(如果 out 下已有相同檔案則覆寫)<br>
   i) dd 虛擬磁碟 p0 相關資料,依 platform/xxxxxx/info/option.json 下所設定的 p0 資訊<br>
   j) 卸載所有虛擬裝置<br>
   k) 製作 update.bin 的 md5sum 至 sys/file.lst<br>
   k) 壓縮打包 sys 下所有內容，並將壓縮檔命名為 .mk_update_sd.rc 下所設定的 zipfilename 資訊 + 日期<br>
</body> 
</html>
