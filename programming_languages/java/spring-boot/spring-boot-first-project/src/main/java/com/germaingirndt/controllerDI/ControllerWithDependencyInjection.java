package com.germaingirndt.controllerDI;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

@RestController
@RequestMapping("controllerWithDependencyInjection")
public class ControllerWithDependencyInjection {

    // This annotation tells Spring to inject the dependency
    // The dependency is created by Spring and injected into the controller
    // "Bean" is a Spring term for a class that is managed by Spring
    @Autowired
    private Dependency dependency;

    @GetMapping("/methodWithDependencyInjection")
    public String methodUsingDependecyInjection() {

        System.out.println("ControllerWithDependencyInjection run!");

        return "Runned sucessfully! " + dependency.getProperty();
    }

}
