// 1. map the filesystem 
// 2. determine the total size of each directory (sum of each file's size)
// 3. Find all of the directories with a total size of at most 100000
// 4. Find the sum of the total sizes of those directories

#include <iostream>
#include <fstream>
#include <vector>
#include <string>
using namespace std;

class dir {
    public:
        dir() : directories(), files(0) {};
        
        vector<dir> directories; // directoriespush_bac.k(element_value)
        int files; 
};

ifstream file("input.txt"); //suffisant ?
