import datetime
import logging

import azure.functions as func


def main(mytimer: func.TimerRequest) -> None:

    timeStamp = datetime.datetime.now()
    timeStr = datetime.datetime.isoformat(timeStamp)

    if mytimer.past_due:
        logging.info('The timer is past due!')

    logging.info('Python timer trigger function ran at %s',timeStr)
