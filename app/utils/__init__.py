import os
from pathlib import Path

import pandas as pd


def format_export(df: pd.DataFrame, filename: str, path: str):
    """
    Formata o arquivo xlsx de uma forma mais "bonita" em relação ao padrão da biblioteca pandas

    Parameters
    ----------
        :param df:
        :param filename:
        :param path:
    """
    Path(path).mkdir(parents=True, exist_ok=True)

    file_path = os.path.join(path, filename)

    writer = pd.ExcelWriter(file_path, engine='xlsxwriter')

    # Padroniza o conteúdo do excel em MAIÚSCULO
    df.columns = [str(col).strip().upper() for col in df.columns]
    df = df.map(lambda x: x.upper() if isinstance(x, str) else x)

    df.to_excel(writer, index=False)
    worksheet = writer.sheets['Sheet1']
    workbook = writer.book  # noqa

    content_format = workbook.add_format({'font_size': 8,
                                          'valign': 'center',
                                          'align': 'center', })

    header_format = workbook.add_format({'valign': 'center',
                                         'font_size': 8,
                                         'font_color': '9BBB59',
                                         'bold': True})
    worksheet.set_default_row(12)

    [worksheet.write(0, col_num, value, header_format) for col_num, value in enumerate(df.columns.values)]

    for idx, col in enumerate(df):
        series = df[col]
        max_len = max((
            series.astype(str).map(len).max(),
            len(str(series.name))
        )) + 1
        worksheet.set_column(idx, idx, max_len, content_format)
    writer._save()
