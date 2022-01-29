package Programmers.Level2;

import java.util.*;

public class 프린터 {
    public static void main(String[] args) {
        int[] priorities = { 1, 1, 9, 1, 1, 1 };
        int[] priorityCnt = new int[10];
        int location = 0;
        int answer = -1;

        List<Integer> list = new ArrayList<>();
        Queue<Pair> que = new LinkedList<>();
        for (int i = 1; i <= priorities.length; i++) {
            que.offer(new Pair(i, priorities[i - 1]));
            priorityCnt[priorities[i - 1]]++;
        }

        while (!que.isEmpty()) {
            Pair p = que.poll();
            int priority = p.b;
            boolean isYes = false;
            if (priority != 9) {
                for (int i = priority + 1; i <= 9; i++) {
                    if (priorityCnt[i] > 0) {
                        isYes = true;
                        break;
                    }
                }
            }
            if (isYes)
                que.offer(p);
            else {
                priorityCnt[priority]--;
                list.add(p.a);
            }
        }
        for (int index = 0; index < list.size(); index++) {
            if (location + 1 == list.get(index)) {
                answer = index + 1;
            }
        }
        System.out.println(answer);
    }

    public static class Pair {
        int a;
        int b;

        Pair(int a, int b) {
            this.a = a;
            this.b = b;
        }
    }

}
