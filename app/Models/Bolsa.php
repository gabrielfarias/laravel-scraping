<?php

namespace App\Models;

use Illuminate\Database\Eloquent\Factories\HasFactory;
use Illuminate\Database\Eloquent\Model;

class Bolsa extends Model
{
    protected $table = 'bolsa';

    use HasFactory;
    protected $fillable = ['nome', 'valor', 'variacao', 'created_at'];
}
