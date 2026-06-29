import llm_sdk
import json
import numpy
from src.services.json_loader import JSONLoader

model = llm_sdk.Small_LLM_Model()

def pick_token_from_logits(logits):
    return int(numpy.argmax(logits))


loader = JSONLoader()
functions = loader.read_input()
function_dict = {
    function.name: function
    for function in functions
}

with open("data/input/function_calling_tests.json", 'r') as file:
    data = json.load(file)


# prompt = "What is the sum of 2 and 3?"
# renato = model.encode(prompt).tolist()[0]
# gabriel = model.get_logits_from_input_ids(renato)
# next_token = pick_token_from_logits(gabriel)
# print(next_token)
# next_token_decoded = model.decode(next_token)
# print(next_token_decoded)
# print(prompt + next_token_decoded)


# prompts = [item['prompt'] for item in data]
prompt = (
    "Question: What is the sum of 2 and 3?\n"
    "Answer:"
)
input_ids = model.encode(prompt).tolist()[0]
generated = input_ids.copy()
logits = model.get_logits_from_input_ids(generated)
array = numpy.array(logits)
top = numpy.argsort(logits)[-10:][::-1]
for token_id in top:
    print(
        token_id,
        logits[token_id],
        repr(model.decode(token_id))
    )
print(model._model_name)


# for prompt in prompts:
#     input_ids = model.encode(prompt).tolist()[0]
#     generated = input_ids.copy()
#     logits = model.get_logits_from_input_ids(generated)
#     array = numpy.array(logits)
#     top = numpy.argsort(logits)[-10:][::-1]
#     for token_id in top:
#         print(
#             token_id,
#             logits[token_id],
#             repr(model.decode(token_id))
#         )
#     print(model._model_name)
#     break
    # next_token = pick_token_from_logits(logits)
    # print(f"=== Next Token ID ===\n{next_token}")
    # decoded_next_token = repr(model.decode(next_token))
    # print(f"=== Decoded Token ===\n{decoded_next_token}")
    # break