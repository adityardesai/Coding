Ref: http://tutorials.jenkov.com/java-concurrency/thread-signaling.html

Java has a builtin wait mechanism that enable threads to become inactive while waiting for signals. 
The class java.lang.Object defines three methods, wait(), notify(), and notifyAll(), to facilitate this.