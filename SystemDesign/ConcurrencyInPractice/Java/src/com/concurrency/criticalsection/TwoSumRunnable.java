package com.concurrency.criticalsection;

public class TwoSumRunnable implements Runnable {
    private int sum1, val1;

    TwoSumRunnable(int val1){
        this.sum1=0;
        this.val1=val1;
    }

    // This is CS
    public void add(){
        synchronized(this){
            this.sum1 += this.val1;
        }
    }

    @Override
    public void run() {
        add();
    }

    public void printSum(){
        System.out.println("Sum is " + this.sum1);
    }
}
