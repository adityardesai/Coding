package com.concurrency.basic;

/*
* Reference from : http://tutorials.jenkov.com/java-concurrency/creating-and-starting-threads.html
* */

public class Main {

    public static void main(String[] args) {

        System.out.println("Extending a Thread Class");

        MyThread myThread1 = new MyThread("th1");
        myThread1.start(); // Not run()!

        // Preferred way
        System.out.println("Implementing the Runnable Interface");

        Thread myThread2 = new Thread(new MyImplementation());
        myThread2.start(); // Not run()!

        // Calling Multiple Threads
        //multiplThreads();

        // Stopping threads
        keepRunningDoStop();

    }

    private static void multiplThreads(){
        System.out.println(Thread.currentThread().getName());
        for(int i=0; i<10; i++){
            new Thread("" + i){
                public void run(){
                    System.out.println("Thread: " + getName() + " running");
                }
            }.start();
        }
    }

    private static void keepRunningDoStop(){

        MyRunnable myRunnable = new MyRunnable();
        Thread thread = new Thread(myRunnable);
        thread.start();

        try {
            Thread.sleep(10L * 1000L);
        } catch (InterruptedException e) {
            e.printStackTrace();
        }
        myRunnable.doStop();
    }
}
