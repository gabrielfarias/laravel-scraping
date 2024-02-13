<?php

namespace App\Models;

use Illuminate\Database\Eloquent\Factories\HasFactory;
use Illuminate\Database\Eloquent\Model;

class IndicadorFinanceiro extends Model
{
    protected $table = 'indicadores_financeiros';

    use HasFactory;
    protected $fillable = ['nome', 'variacao', 'created_at'];
}
