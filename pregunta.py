"""
Limpieza de datos usando Pandas
-----------------------------------------------------------------------------------------

Realice la limpieza del dataframe. Los tests evaluan si la limpieza fue realizada
correctamente. Tenga en cuenta datos faltantes y duplicados.

"""

import re
from datetime import datetime

import pandas as pd


def clean_data():

    df = pd.read_csv("solicitudes_credito.csv", sep=";", index_col=0)
    df = df.copy()

    df.dropna(inplace=True)  # eliminar filas vacias

    df["sexo"] = df["sexo"].str.lower()

    df["tipo_de_emprendimiento"] = df["tipo_de_emprendimiento"].str.lower()

    df["idea_negocio"] = [
        str.lower(idea.replace("_", " ").replace("-", " "))
        for idea in df["idea_negocio"]
    ]

    df.barrio = [
        str.lower(barrio).replace("_", " ").replace("-", " ") for barrio in df.barrio
    ]

    df["barrio"] = [
        str.lower(barrio).replace("_", " ").replace("-", " ") for barrio in df["barrio"]
    ]

    # df["barrio"] = [
    #     str.lower(fila).replace("antonio nari¿o", "antonio nariño")
    #     for fila in df["barrio"]
    # ]  # .replace("bel¿n", "belen")

    df["comuna_ciudadano"] = df["comuna_ciudadano"].astype(int)

    df["estrato"] = df["estrato"].astype(int)

    df["línea_credito"] = [
        fila.replace("-", " ").replace("_", " ").replace(". ", ".")
        for fila in df["línea_credito"]
    ]
    df["línea_credito"] = df["línea_credito"].str.lower().str.strip()  ##

    df["fecha_de_beneficio"] = [
        (
            datetime.strptime(date, "%d/%m/%Y")
            if bool(re.search(r"\d{1,2}/\d{2}/\d{4}", date))
            else datetime.strptime(date, "%Y/%m/%d")
        )
        for date in df["fecha_de_beneficio"]
    ]

    df["monto_del_credito"] = [
        int(monto.replace("$ ", "").replace(".00", "").replace(",", ""))
        for monto in df["monto_del_credito"]
    ]
    df["monto_del_credito"] = df["monto_del_credito"].astype(int)  ##
    df.drop_duplicates(inplace=True)

    return df


# print(clean_data())
# """ [990, 483, 423, 383, 376, 372, 361, 348, 328, 308, 270, 255, 255, 247, 234, 232, 231, 202, 174, 170, 169, 124, 117, 115, 114, 90, 89, 89, 86, 85, 78, 72, 70, 67, 65, 59, 55, 52, 50, 49, 48, 48, 48, 47, 45, 44, 43, 43, 43, 40, 38, 37, 36, 36, 34, 34, 33, 33, 32, 30, 27, 27, 27, 26, 26, 25, 25, 24, 24, 24, 24, 23, 21, 21, 21, 20, 20, 20, 20, 17, 17, 17, 16, 14, 14, 14, 14, 13, 13, 12, 11, 11, 11, 11, 10, 10, 10, 9, 9, 9, 9, 8, 8, 8, 8, 8, 8, 7, 7, 7, 7, 7, 7, 7, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 5, 5, 5, 5, 5, 5, 4, 4, 4, 4, 4, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]"""

# """ [990, 483, 423, 383, 376, 372, 361, 348, 328, 308, 270, 255, 255, 247, 234, 232, 231, 202, 174, 170, 169, 124, 117, 115, 114, 90, 89, 89, 86, 85, 78, 72, 70, 67, 65, 59, 55, 52, 50, 49, 48, 48, 48, 47, 45, 44, 43, 43, 43, 40, 38, 37, 36, 36, 34, 34, 33, 33, 32, 30, 27, 27, 27, 26, 26, 25, 25, 24, 24, 24, 24, 23, 21, 21, 21, 20, 20, 20, 20, 17, 17, 17, 16, 14, 14, 14, 14, 13, 13, 12, 11, 11, 11, 11, 10, 10, 10, 9, 9, 9, 9, 8, 8, 8, 8, 8, 8, 7, 7, 7, 7, 7, 7, 7, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 5, 5, 5, 5, 5, 5, 4, 4, 4, 4, 4, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]"
