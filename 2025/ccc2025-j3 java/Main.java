
import java.util.ArrayList;
import java.util.Scanner;
import java.util.regex.Matcher;
import java.util.regex.Pattern;

public class Main {
    public static void main(String[] args) {
        try (Scanner scan = new Scanner(System.in)) {
            ArrayList<String> newCodes = new ArrayList<>();

            Pattern patA = Pattern.compile("\\p{Upper}+"); // All uppercase letter groups
            Pattern patB = Pattern.compile("-?\\d+"); // All possible integer groups

            int N = Integer.parseInt(scan.nextLine());
            for (int i = 0; i < N; i++) {
                String oldCode = scan.nextLine();
                String newCode = "";
                int fin = 0;

                Matcher matchA = patA.matcher(oldCode);
                Matcher matchB = patB.matcher(oldCode);

                while (matchA.find()) {
                    newCode += matchA.group();
                }
                while (matchB.find()) {
                    fin += Integer.parseInt(matchB.group());
                }

                newCodes.add(newCode + String.valueOf(fin));
            }

            for (String nc : newCodes) {
                System.out.println(nc);
            }
        }
    }
}
