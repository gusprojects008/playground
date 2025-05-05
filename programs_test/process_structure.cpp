#include <iostream>
#include <unistd.h>
#include <sys/wait.h>
#include <stdlib.h>

// fundamentals concepts about processes, memory management and process creation.
 
// global variable allocated in the .data section of the binary.
int global_var = 100;

// void is used to indicate that a function will only perform operations, without returning a specific value that can be used inthe program. 
void COW_demo() {
     std::cout << "\n=== COW (Copy-on-write) operation demontration ===" << std::endl;

     int stack_var = 200; // Integer allocated in the stack. The stack stores local and function scopes variables.
     int* heap_var = new int(200); // Allocating a new integer value in the Heap virtual memory area.  

     std::cout << "Before fork():\n" << std::endl;
     std::cout << "global_var: " << global_var << ". Virtual memory address: " << &global_var << std::endl;
     std::cout << "stack_var: " << stack_var << ". Virtual memory address: " << &stack_var << std::endl;
     std::cout << "heap_var: " << *heap_var << ". Virtual memory address: " << heap_var << std::endl;

     pid_t pid = fork(); // Create a child process. pid_t is a specific data type defined in <sys/types.h>. This prefix is used to indicate that the variable specifically stores a PID. This way, the value of the variable will follow the pattern that types.h has defined for PIDs. if fork() is executed successsfully, it returns "0" to the child, if it fails, it returns "-1".

     if (pid == 0) {

        //Child process created, COW operations carried out. But the child process does not have a physical memory area, i.e. Its page table is not mapped to a physical address in RAM.

        std::cout << "\nChild process created, PID: " << getpid() << std::endl; // The child process has a PID because the kernel reserves a PCB structure regardless of whether or not the process has a page table.
       
        // Child process modifying variables
        global_var = 200;
        stack_var = 300;
        *heap_var = 300;

        // When the child process tries to modify the variables (which were copied from the pages of the parent process to the pages of the child process. *During fork() operation), and exception-type interruption occurs, because the pages (of variables) of the child process are copies of the pages of the parent process, but with read-only permissions, not write permissions. At the time of fork(), the pages of the parent process are copied to the page table of the child process, but the child is given read-only permission, not write permissions. This and exception called "Page fault", the CPU search the IDT for the ISR or handler responsible for handling the exception-type  interrupt.

       // Tachnicaly, the pages of the child process have their virtual address, but their physical address points to the pages of the process. However, the process only has read and not write permissions on them. So, when it tries to write to them, a "Page fault" exception is triggered, which causes the CPU to trigger the ISR responsible for mapping nd reserving a physical memory address in RAM for the specific pages. It then updates the page table of the child process and calls the operation again, allowing the MMU together with the IMC to resolv the physical addressin RAM and write to the cells elated to them.

        std::cout << "After fork() and COW operations:" << std::endl;
        std::cout << "global_var modified: " << global_var << ". Virtual memory address: " << &global_var << std::endl;
        std::cout << "stack_var modified: " << stack_var << ". Virtual memory address: " << &stack_var << std::endl;
        std::cout << "heap_var modified: " << *heap_var << ". Virtual memory address: " << heap_var << std::endl;
 
        exit(0); // ends child process.
     } else if (pid > 0) {
         // Parent process.
         wait(NULL); // waits for his son to finish.
        
         std::cout << "\nFather process PID: " << getpid() << std::endl;
        std::cout << "global_var origin: " << global_var << ". Virtual memory address: " << &global_var << std::endl;
        std::cout << "stack_var origin: " << stack_var << ". Virtual memory address: " << &stack_var << std::endl;
        std::cout << "heap_var origin: " << *heap_var << ". Virtual memory address: " << heap_var << std::endl;

         delete heap_var; // frees the heap memory, leaving the "heap_var" variable space open for new value.
     } else {
         std::cerr << "\nError in fork()" << std::endl;
         exit(1);
     }

     }


void process_creation_demo() {
     std::cout << "\n=== Process Creation Demo ===" << std::endl;
     
     std::cout << "PID of the parent process: " << getpid() << std::endl;
     
     pid_t pid = fork(); // creates a child process and returns pid from it.

     if (pid == 0) {
        // Child process
        std::cout << "\nChild process create, PID: " << getpid() << std::endl;

        std::cout << std::endl;

        // Replaces the image of the child process with a new program.
        execlp("ls", "ls", "-l", NULL);

        // if execlp fail:
        std::cerr << "\nFail in execlp()" << std::endl;
        exit(1);
     } else if (pid > 0) {
         // Father process
         int status;
         waitpid(pid, &status, 0); // Waits for his son to finish.
         std::cout << "\nChild process ended. Status: " << WEXITSTATUS(status) << std::endl;
     } else {
         std::cerr << "\nFail in fork()" << std::endl;
         exit(1);
     }

     }

int main() {
    std::cout << "==== Demonstration of the process structure ====" << std::endl;

    COW_demo();
    process_creation_demo();
    
    return 0; 
    }
