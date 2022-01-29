package Programmers.Level2;

public class 문자열압축 {
    public static void main(String[] args) {
        String s = "xababcdcdababcdcd";
        int maxLength = s.length();
        int minAnswer = Integer.MAX_VALUE;
        int tempAnswer = -1;
        if (maxLength == 1)
            System.out.println(1);
        else {
            for (int i = 1; i <= maxLength / 2; i++) {
                tempAnswer = 0;
                String comp1 = s.substring(0, i);
                int count = 1;
                System.out.println("Step" + i + ":::");
                for (int j = i; j < maxLength; j += i) {
                    String comp2 = "";
                    if (j + i > maxLength) {
                        comp2 = s.substring(j, s.length());
                    } else {
                        comp2 = s.substring(j, j + i);
                    }
                    System.out.println(comp1 + " and " + comp2);
                    boolean check = false;
                    if (comp1.equals(comp2)) {
                        count++;
                        check = true;
                        if (j + i != maxLength)
                            continue;
                    }

                    if (count == 1) {
                        tempAnswer += i;
                        System.out.println("+" + i);
                    } else {
                        int numLength = 1;
                        while ((count / 10) != 0) {
                            count /= 10;
                            numLength++;
                        }
                        tempAnswer += (numLength + i);
                        System.out.println("+" + numLength + "+" + i);
                    }
                    if (!check) {
                        if (j + i == maxLength) {
                            tempAnswer += i;
                        } else if (j + i > maxLength) {
                            tempAnswer += (maxLength - j);
                        }
                    }
                    comp1 = comp2;
                    count = 1;
                }
                System.out.println(tempAnswer);
                if (minAnswer > tempAnswer)
                    minAnswer = tempAnswer;
            }
            System.out.println(minAnswer);
        }
    }
}