package com.germaingirndt.controller;

import java.util.Map;

import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.RestController;

@RestController // This annotation tells Spring that this class is a controller
@RequestMapping("/firstController") // This annotation tells Spring that this class will handle requests to the
// /first path
public class FirstController {

    @GetMapping("/firstMethod")
    public String helloWorld() {
        return "Hello World!";
    }

    // This method will handle GET requests to the /firstController/firstMethod path
    // Accessible at http://localhost:8080/firstController/firstMethod
    @GetMapping("/firstMethod/{id}")
    public String firstMethod(@PathVariable String id) {
        return "My first Spring REST API method! It has parameter id = " + id;
    }

    @GetMapping("/secondMethod")
    public String methodWithQueryParams(@RequestParam String id) {
        return "My second Spring REST API method! It has query parameter id = " + id;
    }

    @GetMapping("/thirdMethod")
    public String methodWithAllQueryParams(@RequestParam Map<String, String> allParams) {
        return "My second Spring REST API method! It has following query params = " + allParams.entrySet().toString();
    }

    @PostMapping("/forthMethod")
    public String methodWithBodyParams(@RequestBody Map<String, String> body) {
        return "This is the body: " + body.entrySet().toString();
    }

    @PostMapping("fifthMethod")
    public String methodWithRecordAsBodyParams(@RequestBody UserRecord userRecord) {
        return "The username is: " + userRecord.username;
    }

    record UserRecord(String username) {

    }

    @GetMapping("/sixthMethod/{id}")
    public ResponseEntity<Object> methodWithResponseEntity(@PathVariable Long id) {

        if (id == 1) {
            return ResponseEntity.ok(new UserRecord("Someone"));
        }
        return ResponseEntity.status(400).body("Error message");
    }

}
