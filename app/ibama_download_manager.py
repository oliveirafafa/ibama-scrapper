import os
from datetime import datetime

import grequests
import pandas as pd
import urllib3

from app.state import STATES
from app.utils import format_export
from settings import Config

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


class IbamaDownloadManager:
    ARRECADACAO_URL = 'https://dadosabertos.ibama.gov.br/dados/SICAFI/{}/Arrecadacao/arrecadacaobenstutelados.json'
    MULTA_URL = 'https://dadosabertos.ibama.gov.br/dados/SICAFI/{}/Quantidade/multasDistribuidasBensTutelados.json'

    @staticmethod
    def __is_same_date(json_, filename, file_path):
        # CASO A DATA DE ATUALIZAÇÃO DO ARQUIVO E DO JSON SEJAM IGUAIS, NÃO IREMOS BAIXAR O ARQUIVO
        try:
            if os.path.isfile(os.path.join(file_path, filename)) is False:
                return False

            last_updated_at = pd.read_excel(os.path.join(file_path, filename)).head(1).to_dict('records')[0]['ULTIMAATUALIZACAORELATORIO']

            if last_updated_at == json_[0]['ultimaAtualizacaoRelatorio']:
                return True

            return False
        except:  # noqa
            return False

    def __perform_download(self, urls, type_: str = None):
        requests = (grequests.get(url, verify=False) for url in urls)
        for idx, (state, r) in enumerate(zip(STATES, grequests.map(requests))):
            if not r.ok:
                raise Exception(f'Erro ao buscar dados para o estado {state}; {r.status_code=}')

            filename = f'{type_}_{state.acronym}.xlsx'
            file_path = os.path.join(Config.DIR_ROOT, 'output', type_)

            json_ = r.json()['data']
            if self.__is_same_date(json_, filename, file_path):
                print(datetime.now(), f'ARQUIVO {filename} ESTÁ ATUALIZADO.')
                continue

            print(datetime.now(), f'EXPORTANDO {type_}: \t {idx + 1} DE {len(STATES)}...')
            df = pd.DataFrame(json_)

            format_export(
                df,
                filename=filename,
                path=file_path
            )

    def get_arrecadacao_data(self):
        urls = [self.ARRECADACAO_URL.format(state.acronym) for state in STATES]
        self.__perform_download(urls, type_='ARRECADACAO')

    def get_multa_data(self):
        urls = [self.MULTA_URL.format(state.acronym) for state in STATES]
        self.__perform_download(urls, type_='MULTA')
