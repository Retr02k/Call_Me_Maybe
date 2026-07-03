from json import load
from ..models.function_definition import FunctionDefinition

class JSONLoader:
    def __init__(self):
        pass

    def read_function_definitions(self):
        try:
            with open("data/input/functions_definition.json", 'r') as file:
                settings_read = load(file)
                
                return [
                    FunctionDefinition(
                        name=setting.get('name'),
                        description=setting.get('description'),
                        parameter=setting.get('parameters'),
                        returns=setting.get('returns')
                    )
                    for setting in settings_read
                ]
        except Exception as error_message:
            print(error_message)

    def read_function_calling_tests(self):
        try:
            with open("data/input/function_calling_tests.json", 'r') as file:
                data = load(file)
                return data
        except Exception as error_message:
            print(error_message)
