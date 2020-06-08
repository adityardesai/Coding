package com.concurrency.immutability;

public class MainImmutableValue {

    public static void main(String[] args) {
        ImmutableValue immutableValue = new ImmutableValue(10);
        System.out.println(immutableValue.getValue());

        ImmutableValue result = immutableValue.add(20);
        System.out.println(result.getValue());
    }
}
