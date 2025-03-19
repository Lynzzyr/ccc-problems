
import java.util.Scanner;


public class Main {
    public static void main(String[] args) {
        try (Scanner scan = new Scanner(System.in)) {
            int N = Integer.parseInt(scan.nextLine());
            int C = Integer.parseInt(scan.nextLine());
            int P = Integer.parseInt(scan.nextLine());

            if (N > C * P) {
                System.out.println("no");
            } else {
                System.out.println("yes");
            }
        }
    }
}