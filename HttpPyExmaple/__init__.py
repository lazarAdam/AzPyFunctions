from . import front_ctl as fc
import shared
import os


# counter = 0


def main(req, context):

    # global counter

    # counter += 1

    # print("COUNTER AT:",counter)

    # accessing an application setting in local.setting.jso under "values"
    print(os.environ["myCustomSet"])

    fcInstance = fc.FrontController()

    print(shared.CONST_X)

    return fcInstance.requestHandler(req, context)
