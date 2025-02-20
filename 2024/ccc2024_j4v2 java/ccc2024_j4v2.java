import java.util.Scanner;

class ccc2024_j4v2 {
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);

        // inputs
        char[] pressed = in.nextLine().toCharArray();
        char[] displayed = in.nextLine().toCharArray();
        in.close();

        // stupidly long logic
        if (pressed.length == displayed.length) { for (int i = 0; i < pressed.length; i++) { if (pressed[i] != displayed[i]) { System.out.println(pressed[i] + " " + displayed[i] + "\n "); return; } } }
        
    }
}