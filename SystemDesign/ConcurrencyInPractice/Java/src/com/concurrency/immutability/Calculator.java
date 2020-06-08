package com.concurrency.immutability;

public class Calculator {

    private ImmutableValue currentValue = null;

    public ImmutableValue getValue(){
        return currentValue;
    }

    /*
    * This set's the value for Immutable.
    * Meaning, even though the ImmutableValue class is thread safe,
    * It's usage in this Calculator Class is not thread safe.
    *
    * To make this Calculator Class thread safe,
    * add `synchronized` to setValue, getValue and add
    * */
    public void setValue(ImmutableValue newValue){
        this.currentValue = newValue;
    }

    public void add(int newValue){
        this.currentValue = this.currentValue.add(newValue);
    }
}
