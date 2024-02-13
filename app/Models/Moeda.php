<?php

namespace App\Models;

use Illuminate\Database\Eloquent\Factories\HasFactory;
use Illuminate\Database\Eloquent\Model;

class Moeda extends Model
{
    protected $table = 'moedas';

    use HasFactory;
    protected $fillable = ['nome', 'valor', 'variacao', 'created_at'];
}
