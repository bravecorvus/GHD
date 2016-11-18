/* print square roots in C++ language.  R. Brown, 9/2010 */

#include <iostream>
#include <cmath>
#include <cstdlib>
using namespace std;

int main(int argc, char **argv)
{
    int max = 0;
    if (argc > 0) {
        for (int i = 0;  i < argc;  i++) {
            if (max < atoi(argv[i])) {
                max = stoi(argv[i]);
            }
        }        
    } else {
        max = 1;
    }

    cout << "sqrt(n)" << endl << "--------" << endl;
    for (int n=0;  n<=max;  n++)
        cout << sqrt(n) << endl;
    return 0;
}

