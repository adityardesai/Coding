package com.concurrency.sync;

//Reference: http://tutorials.jenkov.com/java-concurrency/synchronized.html

/*
*
* Synchronized blocks in Java have several limitations. For instance,
* a synchronized block in Java only allows a single thread to enter at a time.
* However, what if two threads just wanted to read a shared value, and not update it?
* That might be safe to allow. As alternative to a synchronized block you
* could guard the code with a Read / Write Lock which as more advanced locking semantics
* than a synchronized block. Java actually comes with a built in ReadWriteLock class you can use.

* What if you want to allow N threads to enter a synchronized block,
* and not just one? You could use a Semaphore to achieve that behaviour.
* Java actually comes with a built-in Java Semaphore class you can use.
*
* There is a small performance overhead associated with entering and exiting a synchronized block in Java.
* As Java have evolved this performance overhead has gone down, but there is still a small price to pay
*
*
*
* The synchronized keyword can be used to mark four different types of blocks:
        Instance methods
        Static methods
        Code blocks inside instance methods
        Code blocks inside static methods
* */
public class Counter {

    private int count = 0;
    static private int staticCount=0;
    private String log;

    /*
    * only one thread can execute inside either of of the two synchronized methods.
    * One thread in total per instance:
    * */
    public synchronized void add(int value){
        this.count += value;
    }
    public synchronized void subtract(int value){
        this.count -= value;
    }


    /*
    * Only one thread can execute inside any of the two addStatic() and subtractStatic()
    * methods at any given time. If Thread A is executing addStatic()
    * then Thread B cannot execute neither addStatic() nor subtractStatic()
    * until Thread A has exited addStatic().
    * */
    public static synchronized void addStatic(int value){
        staticCount += value;
    }

    public static synchronized void subtractStatic(int value){
        staticCount -= value;
    }


    public synchronized void log1(String msg1, String msg2){
        //log.(msg1);
        //log.writeln(msg2);
    }


    public void log2(String msg1, String msg2){
        /*

        Synchronized block construct takes an object in parentheses. In the example "this" is used,
        which is the instance the add method is called on.
        The object taken in the parentheses by the synchronized construct
        is called a monitor object.

        Only a single thread can execute inside either of the two
        synchronized blocks in this example.
        * */
        synchronized(this){
            //log.writeln(msg1);
            //log.writeln(msg2);
        }
    }

}