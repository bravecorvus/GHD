// importing Scanner class from the Java library to be able to get user inputs
import java.util.Scanner;

// Very peculiar that even the main function has to go in a class
public class Facts {
  // defining the factorial function before the start of the main function
  // It is a recursive function that multiplies the original argument times argument-1 * argument-1-1 ... until the it passes argument 1 to the factorial function
  static double factorial(int arg) {
      if (arg > 1) {
        return arg*factorial(arg-1);
      } else {
        // once the argument hits 1, return a hardcoded int one since no need for further recursion
        return 1;
      }
    }  
  public static void main(String[] args) {
    // have to creat a new objected of scanner since Java doesn't support functions that are outside class definitions
    Scanner reader = new Scanner(System.in);
    // instantiate int n to any number but 0 since my loop logic will run infinitely until the user enters a 0
    int n = 1;
    while(true) {
      if(n != 0) {
        System.out.println("Enter a number you want the factorial of: (0 to exit)");
        n = reader.nextInt();
        Facts testobject = new Facts();
        System.out.println("n --------------- factorial(n)");
        System.out.println(n + "\t\t   " + testobject.factorial(n));
      } else {
        // If user enters "0", the program will exit
        break;
      }
    }
  }
  
}