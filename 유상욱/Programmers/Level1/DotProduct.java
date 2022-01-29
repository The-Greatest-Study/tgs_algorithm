package Programmers.Level1;

public class DotProduct {
    public static void main(String[] args) {
        int[] a = { 1, 2, 3, 4 };
        int[] b = { -3, -1, 0, 2 };

        int answer = 0;
        int idx = 0;
        for (int num : a)
            answer += num * b[idx++];

        System.out.println(answer);
    }
}