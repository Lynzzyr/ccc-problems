import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        try (Scanner scan = new Scanner(System.in)) {
            String flips = scan.nextLine();
            int h = 0;
            int v = 0;

            for (char c : flips.toCharArray()) {
                h = c == 'H' ? h + 1 : h;
                v = c == 'V' ? v + 1 : v;
            }

            h %= 2;
            v %= 2;

            if (h == 1) {
                System.out.println(v == 1 ? "4 3\n2 1" : "3 4\n1 2");
            } else if (v == 1) {
                System.out.println(h == 1 ? "4 3\n2 1" : "2 1\n4 3");
            } else {
                System.out.println("1 2\n3 4");
            }
        }
    }
}