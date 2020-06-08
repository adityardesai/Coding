package com.concurrency.basic;

public class MyThread extends Thread {
    MyThread(String name){
        this.setName(name);
    }
    public void run(){
        System.out.println("MyThread running");
        Thread thread = Thread.currentThread();
        System.out.println("Run by " + thread.getName());
    }
}
