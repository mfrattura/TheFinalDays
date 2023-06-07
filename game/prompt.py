

class Prompt:
    def __init__(self, id, prompt, response):
        self.id = id
        self.prompt = prompt
        self.response = response

    def __str__(self):
        return self.prompt

    def __repr__(self):
        return f"{self.prompt} : {self.response}"
