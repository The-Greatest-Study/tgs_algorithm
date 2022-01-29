package Programmers.Level2;

public class CrossBridgeTruck {
    public static void main(String[] args) {
        int bridge_length = 100;
        int weight = 100;
        int[] truck_weights = { 10, 10, 10, 10, 10, 10, 10, 10, 10, 10 };

        int truckNum = truck_weights.length;
        int[] bridge = new int[bridge_length];

        int time = 0;
        int truckIdx = 0;
        int weightSum = 0;
        while (truckIdx != truckNum || weightSum != 0) {
            int truck = 0;
            if (truckIdx < truckNum)
                truck = truck_weights[truckIdx];
            else {
                if (weightSum == 0)
                    break;
            }
            // 트럭이 진입해도 될 지 확인
            boolean isCanGo = false;
            if (bridge[0] > 0)
                weightSum -= bridge[0];

            if (weightSum + truck <= weight) {
                weightSum += truck;
                isCanGo = true;
                truckIdx++;
            }
            // 다리 한칸씩 건너기
            for (int i = 1; i < bridge_length; i++) {
                bridge[i - 1] = bridge[i];
                bridge[i] = 0;
                if (isCanGo && i == bridge_length - 1)
                    bridge[i] = truck;
            }
            time++;
        }
        System.out.println(time);
    }
}