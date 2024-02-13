<?php

use App\Http\Controllers\BolsaController;
use App\Http\Controllers\IndicadorFinanceiroController;
use App\Http\Controllers\MoedaController;
use Illuminate\Support\Facades\Route;

/*
|--------------------------------------------------------------------------
| Web Routes
|--------------------------------------------------------------------------
|
| Here is where you can register web routes for your application. These
| routes are loaded by the RouteServiceProvider within a group which
| contains the "web" middleware group. Now create something great!
|
*/

Route::get('/', function () {
    return view('home');
});

Route::get('/bolsa', [BolsaController::class, 'index']);
Route::get('/indicadores-financeiros', [IndicadorFinanceiroController::class, 'index']);
Route::get('/moedas', [MoedaController::class, 'index']);
