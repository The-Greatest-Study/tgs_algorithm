package Programmers.Level1;

import java.util.Set;
import java.util.TreeSet;

public class 폰켓몬 {
    public static void main(String[] args) {
        int answer = 0;
        int[] nums = { 3, 3, 3, 2, 2, 2 };
        int selectNum = nums.length / 2;

        Set<Integer> set = new TreeSet<>();
        for (int num : nums)
            set.add(num);

        int maxType = set.size();

        if (selectNum <= maxType)
            answer = selectNum;
        else
            answer = maxType;

        System.out.println(answer);
    }
}
