import llm_sdk
import json
import numpy
from src.services.json_loader import JSONLoader


model = llm_sdk.Small_LLM_Model()

def pick_token_from_logits(logits):
    return int(numpy.argmax(logits))


loader = JSONLoader()
functions_definitions = loader.read_function_definitions()
function_definition_dict = {
    function_definition.name: function_definition
    for function_definition in functions_definitions
}

data = loader.read_function_calling_tests()

prompts = [item['prompt'] for item in data]

prompt = "What is the sum of 2 and 3?"
#for prompt in prompts:
#    input_ids = model.encode(prompt).tolist()[0]
#    generated = input_ids.copy()
#    logits = model.get_logits_from_input_ids(generated)
#    most_probable_next_token = pick_token_from_logits(logits)
#    next_token_decoded = model.decode(most_probable_next_token)
#    print(prompt+next_token_decoded)
#    break
input_id = model.encode(prompt).tolist()[0]
generated_token_ids_list = input_id.copy()
for i in range(0, 10):
    logits = model.get_logits_from_input_ids(generated_token_ids_list)
    most_probable_token = pick_token_from_logits(logits)
    generated_token_ids_list.append(most_probable_token)
    

print(f"=== Token Ids List ===\n{generated_token_ids_list}")
for token in generated_token_ids_list:
    print(f"=== Decoded Token Id ===\n{model.decode(token)}")
print(f"=== Decoded Generated ===\n{model.decode(generated_token_ids_list)}")
print(f"=== Prompt ===\n{prompt}")
