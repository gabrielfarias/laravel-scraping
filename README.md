# Projeto de Automação Financeira

Este é um projeto Laravel para automação financeira, que realiza a captura de dados financeiros da internet, os armazena em um banco de dados PostgreSQL e os exibe em páginas web utilizando o framework Laravel e estilização Bootstrap.

## Configuração do Ambiente

1. **Instalação do Laravel**: 
   - Para iniciar, é necessário ter o Laravel instalado. Se ainda não o tiver, você pode seguir as instruções de instalação na [documentação oficial do Laravel](https://laravel.com/docs).

2. **Configuração do Banco de Dados**:
   - Certifique-se de ter o PostgreSQL instalado e configurado na sua máquina.
   - No arquivo `.env`, configure as informações do banco de dados, como nome do banco, usuário e senha.

## Passo a Passo

### 1. Criação do Banco de Dados e Tabelas

- [x] Criação do banco de dados PostgreSQL `dados_financeiros`.
- [x] Criação da tabela `indicadores_financeiros` com colunas `nome`, `valor`, `data` e `created_at`.
- [x] Criação da tabela `bolsa` com colunas `nome`, `valor`, `variacao`, `data` e `created_at`.
- [x] Criação da tabela `moedas` com colunas `nome`, `valor`, `variacao`, `data` e `created_at`.

### 2. Implementação da Captura de Dados

- [ ] Implementação de Jobs em Python para capturar dados financeiros da internet.
- [ ] Integração dos Jobs Python ao Laravel para armazenar os dados no banco de dados PostgreSQL.

## Licença

Este projeto está licenciado sob a licença [MIT](https://opensource.org/licenses/MIT).
