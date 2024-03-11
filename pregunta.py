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
    df = df.dropna()  # eliminar filas vacias

    df["sexo"] = df["sexo"].str.lower()  # Reemplazar todo por minuscula

    df["tipo_de_emprendimiento"] = df["tipo_de_emprendimiento"].str.lower()

    df["idea_negocio"] = df["idea_negocio"].str.lower()

    df["idea_negocio"] = [
        fila.replace("-", " ").replace("_", " ") for fila in df["idea_negocio"]
    ]

    df["barrio"] = [
        str.lower(barrio).replace("_", " ").replace("-", " ") for barrio in df["barrio"]
    ]

    df["barrio"] = df["barrio"].str.strip()

    df["estrato"] = df["estrato"].astype(int)

    df["comuna_ciudadano"] = df["comuna_ciudadano"].astype(int)

    df["monto_del_credito"] = [
        fila.replace(".00", "").replace("$", "").replace(",", "").replace(".", "")
        for fila in df["monto_del_credito"]
    ]

    df["monto_del_credito"] = df["monto_del_credito"].astype(int)

    df["línea_credito"] = df["línea_credito"].str.lower().str.strip()
    df["línea_credito"] = [
        fila.replace("-", " ").replace("_", " ").replace(". ", ".")
        for fila in df["línea_credito"]
    ]

    df["fecha_de_beneficio"] = [
        (
            datetime.strptime(date, "%d/%m/%Y")
            if bool(re.search(r"\d{1,2}/\d{2}/\d{4}", date))
            else datetime.strptime(date, "%Y/%m/%d")
        )
        for date in df["fecha_de_beneficio"]
    ]

    df.drop_duplicates(inplace=True)

    return df["sexo"].value_counts()
