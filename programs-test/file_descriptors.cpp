#include <iostream>
#include <cstring>
#include <fcntl.h>
#include <unistd.h>
#include <cstring>

int main() {
    /* return an integer related to a file descriptor that teh kernel has registered in the process's FD table,
       and which corresponds tothe structure that the kernel has reserved for it in its global table of structures
       corresponding to file descriptors opened and used by the system and processes.

       This makes it possible for the program to peform operations on devices, file or sockets. Communicationg with
       them through syscalls for these file descriptors.
    */

    std::string main_virtual_console = "/dev/tty";
    int fd = open(main_virtual_console.c_str(), O_RDONLY);

    std::cout << "Buffer data from main virtual console " << main_virtual_console << std::endl;

    /*
    int time = 5;
    std::cout << "closing file descriptor " << fd << " from " << main_virtual_console << " in " << time << " seconds " << std::endl;
    */

    // buffer to store read data
    const size_t bufferSize = 100;
    char buffer[bufferSize];

    for (int i=0; i < 10; i++) {
        std::cout << "Type something (limit " << i << "): " << std::flush;
        ssize_t bytesRead = read(fd, buffer, bufferSize);
        std::cout << "Data reads from tty buffer: " << std::string(buffer, bytesRead);
    }

    /*
    std::cout << std::string(buffer, bytesRead) << std::endl;
    std::cout << "closing..." << std::endl;
    sleep(5);
    close(fd);
    std::cout << "close" << std::endl;
    */
    
    return 0;
}
