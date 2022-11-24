from features.move_rover.move_handler import MoveHandler
from features.move_rover.move_response import MoveResponse


class MoveRequest:
    def __init__(self, inp=None):
        self.__handler = MoveHandler()
        self.__response = MoveResponse()
        self.__validate(inp)

    def __validate(self, inp):
        if inp is None or len(inp) < 2:
            self.__response.build_failed_response("Invalid input")
        else:
            result = self.__handler.process_request(inp[1])

            if result["code"] == 200:
                self.__response.build_success_response(result["data"])
            else:
                self.__response.build_failed_response(result["data"])

        return
