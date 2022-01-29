package Programmers.Level2;

import java.util.*;

public class 기능개발 {
    public static void main(String[] args) {
        int[] answer = {};
        List<Integer> tempAns = new ArrayList<>();
        int[] progresses = { 95, 90, 99, 99, 80, 99 };
        int[] speeds = { 1, 1, 1, 1, 1, 1 };

        Queue<Integer> q = new LinkedList<>();
        for (int progress : progresses)
            q.add(progress);

        int outQueue = 0;
        while (!q.isEmpty()) {
            int cnt = 0;
            int size = q.size();
            if (q.peek() >= 100) {
                boolean cont = false;
                for (int i = 0; i < size; i++) {
                    int confirm = q.poll();
                    if (confirm >= 100 && !cont) {
                        cnt++;
                        outQueue++;
                    } else {
                        cont = true;
                        q.offer(confirm);
                    }
                }
                tempAns.add(cnt);
            } else {
                for (int i = 0; i < size; i++)
                    q.offer(q.poll() + speeds[outQueue + i]);
            }
        }

        answer = new int[tempAns.size()];
        for (int i = 0; i < tempAns.size(); i++)
            answer[i] = tempAns.get(i);

    }
}