import logging
import azure.functions as func
from datetime import datetime
# import os
# import requests
# import pandas as pd
# import io
# from azure.storage.blob import BlobServiceClient


app = func.FunctionApp()


@app.timer_trigger(schedule="0 5 * * * *", arg_name="myTimer", run_on_startup=False,
                   use_monitor=False)
def Func_Data_Refinement(myTimer: func.TimerRequest) -> None:
    logging.info('Python timer trigger function started.')

    logging.info(
        'Acessar os dados do Blob Storage e carregar no Data Refinement (Camada Silver).')

    logging.info('Formatar os dados com as regras de negócios.')

    logging.info('Criar todas as tabelas para leituras dos dados.')

    logging.info('Gerar o arquivo de saída.')

    logging.info('Salvar o arquivo de saída no Blob Storage.')

    logging.info('Python timer trigger function executed.')


# if __name__ == '__main__':
#     # For local testing, pass None or a mock TimerRequest
#     Func_Data_Refinement(None)
