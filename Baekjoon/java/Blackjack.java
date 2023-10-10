package Baekjoon.java;
import java.io.*;
import java.util.*;

public class Blackjack {
    public void solution() throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        StringTokenizer st = new StringTokenizer(br.readLine(), " ");

        int a = Integer.parseInt(st.nextToken());
        int b = Integer.parseInt(st.nextToken());

        st = new StringTokenizer(br.readLine(), " ");

        int[] list = new int[a];

        for (int i = 0; i < a; i++) {
            list[i] = Integer.parseInt(st.nextToken());
        }

        int tmp = 0;
        int max_value = 0;
        for(int i = 0; i < a-2; i++) {
            for(int j = i+1; j < a-1; j++) {
                for(int k = j+1; k < a; k++) {
                    tmp = list[i] + list[j] + list[k];
                    if(tmp <= b) {
                        max_value = Math.max(max_value, tmp);
                    }
                }
            }
        }

        bw.write(max_value + "\n");

        br.close();
        bw.close();
    }


    public static void main(String[] args) {
        try {
            new Blackjack().solution();
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}