package Programmers.Level2;

import java.util.*;

public class 단체사진찍기 {
    static int answer = 0;
    static Map<Integer, Character> members = new HashMap<>();

    public static void main(String[] args) {
        answer = 0;
        String[] data = { "N~F=0", "R~T>2" };
        members.put(0, 'A');
        members.put(1, 'C');
        members.put(2, 'F');
        members.put(3, 'J');
        members.put(4, 'M');
        members.put(5, 'N');
        members.put(6, 'R');
        members.put(7, 'T');
        boolean[] check = new boolean[8];
        makeLine(data, check, 0, "");
        System.out.println(answer);
    }

    public static boolean testChk(String s, String[] d) {
        boolean result = true;
        for (String data : d) {
            char c1 = data.charAt(0);
            char c2 = data.charAt(2);
            char op = data.charAt(3);
            char num = data.charAt(4);

            int idx1 = 0, idx2 = 0;
            for (int i = 0; i < s.length(); i++) {
                if (c1 == members.get(s.charAt(i) - 48))
                    idx1 = i;
                if (c2 == members.get(s.charAt(i) - 48))
                    idx2 = i;
            }

            switch (op) {
                case '=':
                    if ((Math.abs(idx1 - idx2) - 1) != (num - 48)) {
                        result = false;
                    }
                    break;
                case '<':
                    if ((Math.abs(idx1 - idx2) - 1) >= (num - 48)) {
                        result = false;
                    }
                    break;
                case '>':
                    if ((Math.abs(idx1 - idx2) - 1) <= (num - 48)) {
                        result = false;
                    }
                    break;
                default:
                    System.err.println("Error Case");
            }

            if (!result)
                return false;
        }

        return result;
    }

    public static void makeLine(String[] data, boolean[] chk, int depth, String lines) {
        if (depth == 8) {
            if (testChk(lines, data)) {
                answer++;
            }
            return;
        }

        for (int i = 0; i < 8; i++) {
            if (chk[i])
                continue;
            chk[i] = true;
            makeLine(data, chk, depth + 1, lines + i);
            chk[i] = false;
        }

    }

}
