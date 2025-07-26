import sys, time, os, random

if len(sys.argv) == 1:
    print("no file given. goodbye")
    quit()
    

print("""
                                                                    
                            @@@@@@/                                    
                    .@@@@@@@@@@@@@@@                                
                /@@@@@@@@@@@@@@@@@@@@@@@.                           
            &@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@/                       
        .@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%                   
    /@@@@@@@@@@@@@@@@@@@@@&&%%%&@@@@@@@@@@@@@@@@@@@@@@.              
@@@@@@@@@@@@@@@@@@&                  .@@@@@@@@@@@@@@@@@@&           
@@@@@@@@@@@@@@@@,                         #@@@@@@@@@@@@@@@@          
@@@@@@@@@@@@@@                               @@@@@@@@@@@@@@          
@@@@@@@@@@@@.             *%@@@#,             &@@@@@@@@@@@@          
@@@@@@@@@@@           #@@@@@@@@@@@@@,     %@@@@@@@@@@@@@@@@          
@@@@@@@@@@          /@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@          
@@@@@@@@@&         *@@@@@@@@@@@@@@@@@@@@@@@@@  @@@@@@  @@@@          
@@@@@@@@@&         #@@@@@@@@@@@@@@@@@@@@@@&      @%      &@          
@@@@@@@@@@         .@@@@@@@@@@@@@@@@@@@@@@@@%  @@@@@@  @@@@          
@@@@@@@@@@.          @@@@@@@@@@@@@@@@#%@@@@@@@@@@@@@@@@@@@@          
@@@@@@@@@@@            &@@@@@@@@@@@,      /@@@@@@@@@@@@@@@@          
@@@@@@@@@@@@/                                 &@@@@@@@@@@@@          
@@@@@@@@@@@@@@,                             (@@@@@@@@@@@@@@          
@@@@@@@@@@@@@@@@&                         @@@@@@@@@@@@@@@@@          
&@@@@@@@@@@@@@@@@@@#                 %@@@@@@@@@@@@@@@@@@*           
    @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@/               
        (@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@,                   
            ,@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@&                        
                    &@@@@@@@@@@@@@@@@@@@@@(                            
                        (@@@@@@@@@@@@@.                                
                            .@@@@@                                     
                                                                    """)



filepath = sys.argv[1]

if len(sys.argv) == 3:
    namē = sys.argv[2]
else:
    name = str(random.randint(0, 100000000000)) + '.exe'



print("compilation start")

compInit = time.time()

return_code = os.system("g++ " + filepath + " -o " + name)

if return_code != 0:
    print("FAILED: g++ compilation failed, see above")
    quit()

compEnd = time.time()

timeTaken = compEnd - compInit

print("compilation success;", timeTaken, "seconds")

print("execution start")

exeInit = time.time()
os.system(".\\" + name)
exeEnd = time.time()
timeTaken2 = exeEnd - exeInit

print("execution complete; ", timeTaken2, "seconds")
print("deletion start")

os.system("del " + name)
print("deletion success. goodbye")