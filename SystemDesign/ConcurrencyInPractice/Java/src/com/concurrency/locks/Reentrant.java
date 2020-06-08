package com.concurrency.locks;
/*
*
* if a Java thread enters a synchronized block of code, and thereby take the lock on
* the monitor object the block is synchronized on, the thread can enter other Java
* code blocks synchronized on the same monitor object.
*   public class Reentrant{
         public synchronized outer(){
                inner();
        }
        public synchronized inner(){
            //do something
        }
}
*
* A thread calling outer() will first lock the Lock instance. Then it will call inner().
* Inside the inner() method the thread will again try to lock the Lock instance.
* This will fail (meaning the thread will be blocked), since the Lock instance was locked
* already in the outer() method. So we need to make Lock capable to handle this situation.
* Hence Lock2 implementation.
*
*
* */
public class Reentrant {

    Lock lock = new Lock();

    public synchronized void outer() throws InterruptedException {
        lock.lock();
        inner();
        lock.unlock();
    }
    public synchronized void inner() throws InterruptedException {

        lock.lock();
        //do something
        lock.unlock();
    }
}
