@extends('layouts.app')

@section('content')
    <!-- Conteúdo da sua página aqui -->
    <h1>Indicadores Bolsa</h1>
    <table class="table">
        <thead>
            <tr>
                <th>Nome</th>
                <th>Valor</th>
                <th>Variação</th>
                <th>Data</th>
            </tr>
        </thead>
        <tbody>
            @foreach ($dados as $dado)
                <tr>
                    <td>{{ $dado->nome }}</td>
                    <td>{{ $dado->valor }}</td>
                    <td>{{ $dado->variacao }}</td>
                    <td>{{ \Carbon\Carbon::createFromFormat('Y-m-d H:i:s', $dado->created_at)->format('d/m/Y H:i') }}</td>
                </tr>
            @endforeach
        </tbody>
    </table>
@endsection
