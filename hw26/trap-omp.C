#include <iostream>
#include <cmath>
#include <cstdlib>
using namespace std;

/* Demo program for OpenMP: computes trapezoidal approximation to an integral*/


const double pi = 3.141592653589793238462643383079;


int main(int argc, char** argv) {
  /* Variables */
  double a = 0.0, b = pi;  /* limits of integration */;
  int n = 1048576; /* number of subdivisions = 2^20 */
  double h = (b - a) / n; /* width of subdivision */
  double integral; /* accumulates answer */
  int threadct = 1;  /* number of threads to use */
  
  /* parse command-line arg for number of threads */
  if (argc > 1)
    threadct = atoi(argv[1]);

  double f(double x);
    
#ifdef _OPENMP
  cout << "OMP defined, threadct = " << threadct << endl;
#else
  cout << "OMP not defined" << endl;
#endif

  integral = (f(a) + f(b))/2.0;
  int i;
  #pragma omp parallel for num_threads(threadct) \
  shared(a, n, h, integral) private(i)
  for(i = 1; i < n; i++) {
    integral += f(a+i*h);
  }
  
  integral = integral * h;
  cout << "With n = " << n << " trapezoids, our estimate of the integral" <<
    " from " << a << " to " << b << " is " << integral << endl;
  


  // Added fibbonaci loop
  int z;
  #pragma omp parallel for num_threads(threadct) \
  shared(z) private(i)
    for (z=0;  z<=600;  z++){
      cout << "z is " << z << " and sqrt(z) is " << sqrt(z) << endl;
    }

    // prints out fibonacci triangle

  int t = 0;
  #pragma omp parallel for num_threads(threadct) \
  shared(t) private(i)
int userinput = 2000;
// cout << "How many rows of the fibonacci triangle do you want to print?" << endl;
// cin >> userinput;
int **fibonacci = new int*[userinput];
int x = 1;
  for(int i = 0; i<userinput+1; i++) {
    fibonacci[i]= new int[x];
    ++x;
  }

fibonacci[0][0] = 1;
fibonacci[1][0] = 1;
fibonacci[1][1] = 1;
int length = 3;
for(int i = 2; i <= userinput; ++i) {
  for(t = 0; t < length; ++t) {
    if (t == 0) {
      fibonacci[i][t] = 1;
    } else if (t == length-1) {
      fibonacci[i][t] = 1;
    } else {
      fibonacci[i][t] = fibonacci[i-1][t-1] + fibonacci[i-1][t];
    }
  }
++length;
}
int spacing = userinput;
int num_elements_in_current_row = 1;
for (int i = 0; i < userinput+1; ++i) {
  for (int n = 0; n < spacing; ++n) {
    cout << " ";
  }
  spacing -= 1;
  for (int n = 0; n < num_elements_in_current_row; ++n) {
    cout << fibonacci[i][n] << " ";
  }
  num_elements_in_current_row += 1;
  cout << endl;
}
    return 0;
}


  
   
double f(double x) {
  return sin(x);
}
