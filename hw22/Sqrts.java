/* print square roots in Java language.  R. Brown, 9/2010 */

class Sqrts {
  public static void main(String args[]) {
    int n;
    if(Integer.parseInt(args[0]) < 1) {
        System.out.println("Please provide a valid value");
    } else {
        for (n=0;  n<=Integer.parseInt(args[0]);  n++)
            System.out.println("sqrt(n)");
            System.out.println("--------");
            System.out.println(Math.sqrt(n));
        return;        
    }
  }
}