package com.germaingirndt.controllerDI;

import org.springframework.stereotype.Component;

@Component
public class Dependency {

    String property;

    public Dependency() {
        System.out.println("Dependency created!");

        this.property = "This is a property of the dependency!";
    }

    public String getProperty() {
        return property;
    }

}
