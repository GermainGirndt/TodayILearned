package com.germaingirndt.gestao_vagas.modules.candidate.controller;

import org.springframework.web.bind.annotation.RestController;

import com.germaingirndt.gestao_vagas.modules.candidate.CandidateEntity;

import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestMethod;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;

@RestController
@RequestMapping("/candidate")
public class CandidateController {

    @PostMapping("/")
    public void create(@RequestBody CandidateEntity entity) {
        System.out.println("Candidato: " + entity.getEmail() + " criado com sucesso!");

    }
}
