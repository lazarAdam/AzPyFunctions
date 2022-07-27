
import logging
import azure.functions as func
import json


class FrontController:

    '''
    A static var similar to a global var when not using OOP
    Azure Functions runtime often reuses the same process for multiple executions
    so static or global vars live through the lifetime of the python interpreter execution
    '''
    runCounter = 0

    def __init__(self) -> None:

        self.respBody = "Empty Body"

    def requestHandler(self, req: func.HttpRequest, context: func.Context) -> func.HttpResponse:

        FrontController.runCounter += 1

        print(context.invocation_id)
        print("COUNTER AT:", FrontController.runCounter)

        firstName = None
        lastName = None

        firstName = req.params.get("fName")

        lastName = req.params.get("lName")

        if (not firstName) or (not lastName):

            try:
                self.respBody = req.get_json()

                self.respBody["gift"] = "\N{grinning face}"

            except Exception as e:

                logging.info(f"Error occurred: {e}")
        else:

            self.respBody = {
                "fName": firstName,
                "lName": lastName,
                "gift": "\N{grinning face}"
            }

        resp = func.HttpResponse(
            json.dumps(self.respBody, indent=2),
            status_code=200,
            headers={"Content-Type": "application/json"}
        )

        logging.info("HTTP request was processed")

        return resp
