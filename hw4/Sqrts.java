/* print square roots in Java language.  R. Brown, 9/2010 */

public class Sqrts {
  public static void main(String[] args) {
    System.out.println("n --------------- sqrt(n)");
    System.out.println("--------");
    int n;
    for (n=0;  n<=5;  n++)
      System.out.println(n + "\t\t   " + Math.sqrt(n));
    return;

  }
}