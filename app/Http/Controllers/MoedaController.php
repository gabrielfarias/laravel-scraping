<?php

namespace App\Http\Controllers;

use App\Models\Moeda;
use Illuminate\Http\Request;

class MoedaController extends Controller
{
    public function index()
    {
        $dados = Moeda::all();
        return view('moedas', compact('dados'));
    }
}
