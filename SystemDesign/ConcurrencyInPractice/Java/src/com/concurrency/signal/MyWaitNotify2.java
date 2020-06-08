package com.concurrency.signal;

/*
* To avoid losing signals they should be stored inside the signal class.
* In the MyWaitNotify example the notify signal should be stored in a member
* variable inside the MyWaitNotify instance. Here is a modified version of MyWaitNotify that does this:
*
* */

public class MyWaitNotify2 {
    final MonitorObject myMonitorObject = new MonitorObject();
    boolean wasSignalled = false;

    public void doWait(){
        synchronized(myMonitorObject){
            if(!wasSignalled){
                try{
                    myMonitorObject.wait();
                } catch(InterruptedException e){
                    e.printStackTrace();}
            }
            //clear signal and continue running.
            wasSignalled = false;
        }
    }

    public void doNotify(){
        synchronized(myMonitorObject){
            wasSignalled = true;
            myMonitorObject.notify();
        }
    }
}
