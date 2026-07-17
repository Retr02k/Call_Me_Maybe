from pydantic import (BaseModel,
                      ValidationError,
                      Field)


class FunctionDefinition:
    def __init__(
            self,
            name,
            description,
            parameter,
            returns
            ):
        self.name: str = name
        self.description: str = description
        self.parameter: dict[str, dict[str, str]] = parameter
        self.returns: dict[str, str] = returns
    
    def __str__(self):
        return (f"{self.name}\n"
                f"{self.description}\n"
                f"{self.parameter}\n"
                f"{self.returns}")
    
