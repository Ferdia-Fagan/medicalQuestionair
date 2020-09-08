

class ParentQuestion:

    def __init__(self, parent_question, child_questions_answers, is_exact_answer_relation):
        """
        Container of parent question and child questions
        :param parent_question: Question sub class
        :param child_questions_answers: if is_exact_answer_relation:
                                            dict {key: answer value , value: question subclass}
                                        else:
                                            List[[comparison, value, question subclass],...]
        :param is_exact_answer_relation: boolean.
        """
        self.parent_question=parent_question
        self.child_questions_answers=child_questions_answers
