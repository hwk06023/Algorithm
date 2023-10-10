package Baekjoon.java;

import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;

public class Hanoitop {
    static StringBuilder output = new StringBuilder();
    public static void hanoitop(int n, int start, int mid, int end) {
        if(n == 1) {
            output.append(start + " " + end + "\n");
            return;
        }
        hanoitop(n-1, start, end, mid);
        output.append(start + " " + end + "\n");
        hanoitop(n-1, mid, start, end);
    }

    public void solution() throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        
        int n = Integer.parseInt(br.readLine());
        br.close();

        bw.write((int)Math.pow(2, n) - 1 + "\n");

        hanoitop(n, 1, 2, 3);
        
        bw.write(output.toString());
        bw.close();
    }

    public static void main(String[] args) {
        try {
            new Hanoitop().solution();
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}
