package Baekjoon.java;
/* 
import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.io.IOException;
import java.util.StringTokenizer;
*/

import java.util.*;
import java.io.*;

/* more fast than java.util.scanner and System.out.println */

public class Main {
    public void solution() throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        
        StringTokenizer st = new 
        StringTokenizer(br.readLine(), " ");


        /* 
        String[] st = br.readLine().split(" ");
        int a = Integer.parseInt(st[0]);
        int b = Integer.parseInt(st[1]);
        int c = Integer.parseInt(st[2]);
        */
        
        int a = Integer.parseInt(st.nextToken());
        int b = Integer.parseInt(st.nextToken());
        int c = Integer.parseInt(st.nextToken());
        

        bw.write((a+b+c)+"\n");

        br.close();
        bw.close();
    }
    public static void main(String[] args) {
        try {
            new Main().solution();
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}