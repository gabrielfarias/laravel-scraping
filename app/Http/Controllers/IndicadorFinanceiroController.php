<?php

namespace App\Http\Controllers;

use App\Models\IndicadorFinanceiro;
use Illuminate\Http\Request;

class IndicadorFinanceiroController extends Controller
{
    public function index()
    {
        $dados = IndicadorFinanceiro::all();
        return view('indicadores-financeiros', compact('dados'));
    }
}
