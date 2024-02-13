@extends('layouts.app')

@section('content')
<div class="container">
    <div class="row justify-content-center">
        <div class="col-md-10">
            <div class="card">
                <div class="card-header">Projeto Laravel Scraping Financeiro</div>

                <div class="card-body">
                    <h1>Bem-vindo ao Projeto Laravel Scraping Financeiro</h1>

                    <p>Este é um projeto Laravel para automação financeira, que realiza a captura de dados financeiros da internet, os armazena em um banco de dados PostgreSQL e os exibe em páginas web utilizando o framework Laravel e estilização Bootstrap.</p>

                    <h2>Funcionalidades</h2>
                    <ul>
                        <li>Coleta automática de dados financeiros de fontes online com Python.</li>
                        <li>Exibição dos dados financeiros em uma interface web Laravel Blade.</li>
                        <li>Agendamento de coleta de dados para execução periódica Laravel Jobs.</li>
                    </ul>
                </div>
            </div>
        </div>
    </div>
</div>

@endsection
