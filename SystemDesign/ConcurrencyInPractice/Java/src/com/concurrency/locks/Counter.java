package com.concurrency.locks;

public class Counter {

    private Lock lock = new Lock();
    private int count = 0;

    public int increment() throws InterruptedException {

        lock.lock();
        //Enter Critical Section
        int newCount = ++count;
        //Exit Critical Section
        lock.unlock();
        return newCount;
    }
}
