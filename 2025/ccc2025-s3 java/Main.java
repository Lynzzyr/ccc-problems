// SUBTASK 1 ONLY: Q = 0 ALWAYS
// Partly translated by ChatGPT from Python3

import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        
        // Globals
        int N = 0, M = 0, Q = 0;
        HashMap<Integer, List<Integer>> pens = new HashMap<>();
        
        // Inputs
        String[] r1 = scanner.nextLine().split(" ");
        N = Integer.parseInt(r1[0]);
        M = Integer.parseInt(r1[1]);
        Q = Integer.parseInt(r1[2]);
        
        for (int i = 0; i < N; i++) {
            String[] rl = scanner.nextLine().split(" ");
            int key = Integer.parseInt(rl[0]);
            int value = Integer.parseInt(rl[1]);
            
            pens.putIfAbsent(key, new ArrayList<>());
            pens.get(key).add(value);
            Collections.sort(pens.get(key));
        }
        
        // Process
        List<Integer> rep = new ArrayList<>(); // color, prettiness to replace with
        List<Integer> cols = new ArrayList<>(pens.keySet());
        
        for (int c : cols) {
            List<Integer> cos = new ArrayList<>(cols);
            cos.remove(Integer.valueOf(c));
            int ph = pens.get(c).get(pens.get(c).size() - 1); // highest prettiness
            
            for (int co : cos) {
                List<Integer> ls = pens.get(co);
                for (int i = 0; i < ls.size() - 1; i++) { // skip last value as it will never be avail
                    if (ls.get(i) > ph && !rep.contains(ls.get(i))) {
                        rep.clear();
                        rep.add(c);
                        rep.add(co);
                        rep.add(ls.get(i));
                        break;
                    }
                }
            }
        }
        
        // Print(rep)
        if (!rep.isEmpty()) {
            List<Integer> tl2 = pens.get(rep.get(1));
            tl2.remove(Integer.valueOf(rep.get(2)));
            pens.put(rep.get(1), tl2);
            
            List<Integer> tl3 = pens.get(rep.get(0));
            tl3.add(rep.get(2));
            pens.put(rep.get(0), tl3);
        }
        
        // Output
        int tp = 0;
        for (int c : pens.keySet()) {
            tp += pens.get(c).get(pens.get(c).size() - 1);
        }
        System.out.println(tp);
    }
}
