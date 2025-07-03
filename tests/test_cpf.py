import pytest
import /../app
#import sys
#import os
#sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

def test_valid_cpf():
    assert is_valid_cpf("52998224725") == True  # CPF válido

def test_invalid_cpf():
    assert is_valid_cpf("12345678901") == False  # CPF inválido

def test_cpf_with_incorrect_length():
    assert is_valid_cpf("529982247") == False   # Tamanho incorreto

def test_cpf_with_non_digits():
    assert is_valid_cpf("5299A224725") == False  # Caractere não numérico