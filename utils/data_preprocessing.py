import pandas as pd
from sklearn.preprocessing import StandardScaler, MinMaxScaler
# Puedes importar más librerías según tus necesidades

def load_data(filepath):
    """
    Carga datos desde un archivo en un DataFrame de pandas.

    Args:
        filepath (str): Ruta del archivo a cargar.

    Returns:
        DataFrame: Datos cargados en un DataFrame.
    """
    # Puedes ajustar esta función para manejar diferentes formatos de archivos como CSV, Excel, etc.
    data = pd.read_csv(filepath)
    return data

def clean_data(data):
    """
    Limpia los datos eliminando o imputando valores faltantes, eliminando duplicados, etc.

    Args:
        data (DataFrame): DataFrame de pandas con los datos a limpiar.

    Returns:
        DataFrame: Datos limpiados.
    """
    # Aquí puedes añadir tu lógica para limpiar los datos
    # Por ejemplo, eliminar filas con valores faltantes, imputar valores, etc.
    cleaned_data = data.dropna()  # Ejemplo básico
    return cleaned_data

def normalize_data(data):
    """
    Normaliza los datos para que tengan una media de 0 y una desviación estándar de 1.

    Args:
        data (DataFrame): DataFrame de pandas con los datos a normalizar.

    Returns:
        DataFrame: Datos normalizados.
    """
    scaler = StandardScaler()
    normalized_data = scaler.fit_transform(data)
    return pd.DataFrame(normalized_data, columns=data.columns)

def preprocess_data(filepath):
    """
    Función general para el preprocesamiento de datos.

    Args:
        filepath (str): Ruta del archivo de datos.

    Returns:
        DataFrame: Datos preprocesados.
    """
    data = load_data(filepath)
    data = clean_data(data)
    data = normalize_data(data)
    return data

# Ejemplo de uso:
# preprocessed_data = preprocess_data('ruta/a/tu/dataset.csv')
