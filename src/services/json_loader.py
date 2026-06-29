from json import load
from ..models.function_definition import FunctionDefinition

class JSONLoader:
    def __init__(self):
        pass

    def read_input(self):
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


if __name__ == "__main__":
    def test_main():
        loader = JSONLoader()
        functions = loader.read_input()

        for function in functions:
            print(f"{function}\n")
            for param, param_type in function.parameter.items():
                print(f"key -> {param}\nvalue -> {param_type['type']}\nresult -> {function.returns['type']}\n")


    test_main()