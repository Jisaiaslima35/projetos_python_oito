"use strict"

const ps = require('prompt-sync')
const prompt = ps()


class AgendaTelefonica {
    constructor() {
      this.opcao = '';
    }
  
    exibirMenu() {
      console.log('########################');
      console.log('## Projeto Agenda JavaScript');
      console.log('Menu:');
      console.log('[1] Cadastrar');
      console.log('[2] Lista de contatos');
      console.log('[3] E-mail do usuário');
    }
  
    iniciar() {
      while (this.opcao !== '1' && this.opcao !== '2' && this.opcao !== '3') {
        this.exibirMenu();
        this.opcao = prompt('Escolha uma opção: ');
  
        if (this.opcao === '1') {
          this.cadastrar();
        } else if (this.opcao === '2') {
          this.listarContatos();
        } else if (this.opcao === '3') {
          this.exibirEmailUsuario();
        } else {
          console.log('Opção inválida. Tente novamente.');
        }
      }
    }
  
    cadastrar() {
      console.log('Você escolheu a opção de cadastro');
    }
  
    listarContatos() {
      console.log('Você escolheu a opção de listar contatos');
    }
  
    exibirEmailUsuario() {
      console.log('Você escolheu a opção de exibir e-mail do usuário');
    }
  }
  
  const agenda = new AgendaTelefonica();
  agenda.iniciar();
  