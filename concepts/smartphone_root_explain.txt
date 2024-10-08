On a smartphone with Android operating system normally, the user does not have access and 
permissions to internal files and perform complex operations or operations that use maximum
resources from the smartphone.

This is to protect the user aginst attacks and malicious programs, and so that the user does
not carry out risky operations and compromise the security and integrity of the smartphone.
Because the smartphone is designed for be accessible, safe, stable, so for this the 
android smartphone sets limits for the users.

Then, when you own all access to the smartphone or access to the user root, you must be accept
the risk and problems they can occur, because of your actions and operations.

Ways to get root access:

Root by modified Kernel: when the operating system kernel allows the user to access and
perform superuser operations (internal operations) on the system and smartphone.

Root via Bootloader: The bootloader is the program responsible for initializing the hardware, operating system and other programs responsible for the basic functioning of the system and smartphone. And when the user unlocks the bootloader, he can load files and programs into the bootloader, thus modifying the smartphone and giving it the power to run programs on the smartphone. In RAM, the bootloader loads the boot.img file, the boot.img has the kernel and the Ram disk (initramfs, is a temporary file system) 
that has other files, binaries and initialization scripts necessary to load the operating system. The 
initramfs is mainly responsible for loading modules/drivers for the kernel to load and mount the root 
partitions of the system properly (with their files and directories *"/data", "/dev", "/etc") etc...
according to the file system of the partitions. initramfs is a file system temporarily loaded into RAM, 
initialized and used by the kernel to mount the root partitions according to the partition's file system and
boot the operating system.

The initramfs has an "init" file, the "init" file is responsible for detecting hardware and storage devices,
mounting the operating system's root partition, setting the user's boot environment, and starting user 
interface services, among others.

At boot time, the bootloader loads the boot.img, then the boot.img loads the kernel and passes control to it,
and the kernel loads the Ram disk (initramfs). Magisk starts, intercepts this entire initialization and 
modifies the boot.img file in the Ram disk (initramfs) part of the "init" file by loading its own code into
it, giving the user a root management structure and elevated privileges over the smartphone.

Magisk inserts scripts and commands into the “init” file that ensure that the “magiskd” service is initialized,
which is responsible for managing user root requests. Magisk then sits in the background while the operating
system is running, managing and responding to root access requests and performing administrative operations.

This way, the user gains root access before the services are initialized.
Thus, Magisk provides root access without modifying the kernel and other important system programs.
