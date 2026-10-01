import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int n = Integer.parseInt(br.readLine());

        int[][] times = new int[n][3];
        for (int i = 0; i < n; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            int a = Integer.parseInt(st.nextToken());
            int b = Integer.parseInt(st.nextToken());
            times[i][0] = a;
            times[i][1] = b;
            times[i][2] = i;
        }

        Arrays.sort(times, (x, y) -> Integer.compare(x[0], y[0]));
        int[] allocation = new int[n];
        PriorityQueue<int[]> heap = new PriorityQueue<>(
            (x, y) -> Integer.compare(x[0], y[0])
        );

        int numRoom = 0;
        for (int[] customer : times) {
            int arrival = customer[0];
            int departure = customer[1];
            int index = customer[2];
            int room;
            if (!heap.isEmpty() && heap.peek()[0] < arrival) {
                int[] available = heap.poll();
                room = available[1];
            } else {
                numRoom++;
                room = numRoom;
            }

            heap.offer(new int[]{departure, room});
            allocation[index] = room;
        }

        StringBuilder output = new StringBuilder();
        output.append(numRoom).append('\n');
        for (int i = 0; i < n; i++) {
            output.append(allocation[i]);
            if (i < n - 1) {
                output.append(' ');
            }
        }

        output.append('\n');
        System.out.print(output);
    }
}