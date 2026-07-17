import llm_sdk
import json
import numpy
from src.services.json_loader import JSONLoader
import torch

model = llm_sdk.Small_LLM_Model()

def pick_token_from_logits(logits):
    return int(numpy.argmax(logits))


loader = JSONLoader()
functions_definitions = loader.read_function_definitions()
function_definition_dict = {
    function_definition.name: function_definition
    for function_definition in functions_definitions
}


lista_dos_gabrieis = [
        "{",
        "}",
        "\"",
        ":",
        ",",
        "[",
        "]",
        "true",
        "false",
        "null",
        "123",
        "3.14",
        "fn_add_numbers",
        "parameters",
        '"name"',
        '"parameters"',

        ]

#for gabriel in lista_dos_gabrieis:
#    print(f"=== {gabriel} ===\n{model.encode(gabriel)}\n")

#ids = model.encode("fn_add_numbers")[0]

#for token in ids:
#    print(token.item())
#    print(model.decode(torch.tensor([token.item()], device="cuda")))

functions_names_list = [
        "fn_add_numbers",
        "fn_greet",
        "fn_reverse_string",
        "fn_get_square_root",
        "fn_substitute_string_with_regex"
        ]

func_add = model.encode("fn_add_numbers")[0]
#for token in func_add:
#    print(token.item())
#    print(model.decode(torch.tensor([token.item()], device="cuda")))

func_greet = model.encode("fn_greet")[0]
for token in func_greet:
    print(token.item())
    print(model.decode(torch.tensor([token.item()], device="cuda")))

func_rev = model.encode("fn_reverse_string")[0]
#for token in func_rev:
#    print(token.item())
#    print(model.decode(torch.tensor([token.item()], device="cuda")))

func_sqrt = model.encode("fn_get_square_root")[0]
#for token in func_sqrt:
#    print(token.item())
#    print(model.decode(torch.tensor([token.item()], device="cuda")))

func_sub = model.encode("fn_subtitute_string_with_regex")[0]
#for token in func_sub:
#    print(token.item())
#    print(model.decode(torch.tensor([token.item()], device="cuda")))


#data = loader.read_function_calling_tests()
#prompts = [item['prompt'] for item in data]

#for prompt in prompts:
#    input_ids = model.encode(prompt).tolist()[0]
#    generated = input_ids.copy()
#    logits = model.get_logits_from_input_ids(generated)
#    most_probable_next_token = pick_token_from_logits(logits)
#    next_token_decoded = model.decode(most_probable_next_token)
#    print(prompt+next_token_decoded)
#    break



