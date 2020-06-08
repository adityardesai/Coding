package com.concurrency.criticalsection;

public class TwoSumsMain {



    public static void main(String[] args) {

        TwoSumRunnable run1 = new TwoSumRunnable(10);
        TwoSumRunnable run2 = new TwoSumRunnable(1000);

        Thread th1 = new Thread(run1);
        Thread th2 = new Thread(run2);

        th1.start();
        th2.start();

        run1.printSum();
        run2.printSum();
    }
}
