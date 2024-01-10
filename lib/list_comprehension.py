#!/usr/bin/env python3

def return_evens(num_list):
    even_numbers_list = [n for n in num_list if n % 2 == 0] 
    if len(even_numbers_list) == 0:
        return []
    else:
        return even_numbers_list

def make_exclamation(sentence_list):
    exclamation_string = [sentence + "!" for sentence in sentence_list]
    return(exclamation_string)