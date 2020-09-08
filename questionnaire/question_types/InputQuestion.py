from questionnaire.question_types.Question import Question


class InputQuestion(Question):

    def __init__(self,question,input_type):
        self.input_type=input_type
        super().__init__(question)


