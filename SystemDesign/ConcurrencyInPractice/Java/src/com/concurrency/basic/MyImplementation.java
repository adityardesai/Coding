package com.concurrency.basic;

public class MyImplementation implements Runnable {

    @Override
    public void run() {
        System.out.println("Inside Runnable");
    }
}
