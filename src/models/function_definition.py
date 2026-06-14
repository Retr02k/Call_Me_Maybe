
class FunctionDefinition:
    def __init__(
            self,
            name,
            description,
            parameter,
            returns
            ):
        self.name = name
        self.description = description
        self.parameter = parameter
        self.returns = returns
    
    def __str__(self):
        return (f"Function name -> {self.name}\n"
                f"Function Description -> {self.description}\n"
                f"Function Parameters -> {self.parameter}\n"
                f"Function Returns -> {self.returns}")