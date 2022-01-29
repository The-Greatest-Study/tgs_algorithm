package Programmers.Level1;

import java.util.ArrayList;

public class 소수만들기 {
    public static void main(String[] args) {
        int[] nums = { 1, 2, 7, 6, 4 };
        int answer = 0;

        int L = nums.length;
        ArrayList<Integer> list = new ArrayList<>();

        for (int i = 0; i < L; i++) {
            if (i + 2 == L)
                break;
            for (int j = i + 1; j < L; j++) {
                for (int h = j + 1; h < L; h++) {
                    list.add(nums[i] + nums[j] + nums[h]);
                }
            }
        }

        for (Integer numSum : list) {
            int count = 2;
            answer++;
            while (count < numSum) {
                if (numSum % count == 0) {
                    answer--;
                    break;
                }
                count++;
            }
        }

        System.out.println(answer);
    }
}
