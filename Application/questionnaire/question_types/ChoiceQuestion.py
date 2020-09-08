from Application.questionnaire.question_types.Question import Question


class ChoiceQuestion(Question):

    def __init__(self, question, choices):
        self.choices=choices
        super().__init__(question)


