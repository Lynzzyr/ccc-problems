
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        try (Scanner scan = new Scanner(System.in)) {
            int D = Integer.parseInt(scan.nextLine());

            int E = Integer.parseInt(scan.nextLine());
            for (int i = 0; i < E; i++) {
                String event = scan.nextLine();
                int Q = Integer.parseInt(scan.nextLine());

                D = event.equals("+") ? D + Q : D - Q;
            }

            System.out.println(D);
        }
    }
}
