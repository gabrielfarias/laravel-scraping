<?php

namespace App\Http\Controllers;

use App\Models\Bolsa;
use Illuminate\Http\Request;

class BolsaController extends Controller
{
    public function index()
    {
        $dados = Bolsa::all();
        return view('bolsa', compact('dados'));
    }
}
