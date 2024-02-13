# Projeto Laravel Scraping Financeiro

Este é um projeto Laravel para automação financeira, que realiza a captura de dados financeiros da internet, os armazena em um banco de dados PostgreSQL e os exibe em páginas web utilizando o framework Laravel e estilização Bootstrap.

## Funcionalidades

- Coleta automática de dados financeiros de fontes online com Python.
- Exibição dos dados financeiros em uma interface web Laravel Blade.
- Agendamento de coleta de dados para execução periódica Laravel Jobs.

## Requisitos

- PHP >= 7.4
- Laravel
- Composer
- Python >= 3.9
- PostgreSQL

### Instalação

1. Clone este repositório para o seu ambiente local.
2. Execute `composer install` para instalar as dependências do PHP.
3. Execute `pip install -r requirements.txt` para instalar as dependencias do Python.
4. Configure as credenciais do banco de dados no arquivo `.env`.
5. Execute `php artisan key:generate` para gerar a chave de aplicativo.
6. Execute `php artisan migrate` para criar as tabelas do banco de dados.
7. Execute `php artisan serve` para iniciar o servidor de desenvolvimento.

### Configuração do Banco de Dados PostgreSQL

Certifique-se de que as extensões necessárias para o PostgreSQL estejam habilitadas no PHP. Verifique o arquivo `xampp/php/php.ini` ou `php.ini` do seu ambiente para garantir que as seguintes linhas estejam sem comentários:

```ini
extension=pdo_pgsql
extension=pgsql
```

## Licença

Este projeto está licenciado sob a licença [MIT](https://opensource.org/licenses/MIT).
