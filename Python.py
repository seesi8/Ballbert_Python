from Hal.Classes import Response
from Hal.Decorators import reg
from Hal.Skill import Skill


class Python(Skill):
    @reg(name="Run Python Code")
    def run(self, code):
        """
        Runs Python code. Returns the result. Uses python eval to run code and get result.

        :param string code: The code you want to run.
        :return: The Result.
        :rtype: Response
        """

        try:
            res = eval(code)
            return Response(succeeded=False, data=res)
        except Exception as e:
            return Response(succeeded=False, data=f"error: {e}")
