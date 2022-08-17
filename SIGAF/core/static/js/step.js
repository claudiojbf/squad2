"use strict"

// Selecionando botões no HTML
var botaoProximo1 = document.querySelector("#step-1-button");
var botaoAnterior1 = document.querySelector("#step-2-button-prev");

// Selecionando Input de Senha
var inputSenha = document.querySelector("#senha");
var inputConfirmaSenha = document.querySelector("#confirma-senha");

// Selecionando Bullets
var bullet1 = document.querySelector("#bullet-1");
var bullet2 = document.querySelector("#bullet-2");

// Botão Proximo Step-1
botaoProximo1.addEventListener('click', () => {
    document.querySelector("#step-1").style.display = "none";
    document.querySelector("#step-2").style.display = "flex";
    bullet1.style.backgroundColor = "#b1b1b1";
    bullet2.style.backgroundColor = "#003D9B";
})

//  Botão Anterior Step-2
botaoAnterior1.addEventListener('click', () => {
    document.querySelector("#step-2").style.display = "none";
    document.querySelector("#step-1").style.display = "flex";
    bullet1.style.backgroundColor = "#003D9B";
    bullet2.style.backgroundColor = "#b1b1b1";
})

// // Botão Proximo Step-2 / verificação de senha
// botaoProximo2.addEventListener('click', () => {
//     if(inputSenha.value == inputConfirmaSenha.value){
//         document.querySelector("#step-2").style.display = "none";
//         document.querySelector("#step-3").style.display = "flex";
//         bullet1.style.backgroundColor = "#b1b1b1";
//         bullet2.style.backgroundColor = "#b1b1b1";
//         bullet3.style.backgroundColor = "#003D9B";
//     }else{
//         alert('Confirmação de senha incorreta');
//     }
// })

// // Botão Anterior Step-3
// botaoAnterior2.addEventListener('click', () => {
//     document.querySelector("#step-3").style.display = "none";
//     document.querySelector("#step-2").style.display = "flex";
//     bullet2.style.backgroundColor = "#003D9B";
//     bullet1.style.backgroundColor = "#b1b1b1";
// }) 


