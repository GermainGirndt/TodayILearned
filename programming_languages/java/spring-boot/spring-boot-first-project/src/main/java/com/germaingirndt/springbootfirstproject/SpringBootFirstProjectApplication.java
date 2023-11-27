package com.germaingirndt.springbootfirstproject;

import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.context.annotation.ComponentScan;

@SpringBootApplication
@ComponentScan(basePackages = "com.germaingirndt")
public class SpringBootFirstProjectApplication {

	public static void main(String[] args) {
		SpringApplication.run(SpringBootFirstProjectApplication.class, args);
	}

}
