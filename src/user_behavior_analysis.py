from sklearn.ensemble import IsolationForest
from sklearn.preprocessing import StandardScaler
import numpy as np
import pandas as pd

def preprocess_data(data):
    """
    Preprocesa los datos normalizándolos.
    Args:
        data (DataFrame): Datos de entrada en formato DataFrame de pandas.

    Returns:
        DataFrame: Datos normalizados.
    """
    scaler = StandardScaler()
    scaled_data = scaler.fit_transform(data)
    return pd.DataFrame(scaled_data, columns=data.columns)

def analyze_user_behavior(data):
    """
    Analiza el comportamiento del usuario utilizando el algoritmo Isolation Forest.
    Este método identifica las anomalías en los patrones de comportamiento.

    Args:
        data (DataFrame): Datos de comportamiento del usuario.

    Returns:
        ndarray: Las predicciones del modelo, donde -1 indica una anomalía y 1 lo normal.
    """
    # Validación de la entrada
    if not isinstance(data, pd.DataFrame):
        raise ValueError("La entrada debe ser un DataFrame de pandas")

    # Preprocesamiento de datos
    try:
        preprocessed_data = preprocess_data(data)
    except Exception as e:
        raise Exception(f"Error en el preprocesamiento de datos: {e}")

    # Configuración del modelo Isolation Forest
    model = IsolationForest(n_estimators=100, max_samples='auto', contamination=float(0.1), max_features=1.0)
    
    # Entrenamiento y predicciones
    try:
        predictions = model.fit_predict(preprocessed_data)
    except Exception as e:
        raise Exception(f"Error en el entrenamiento del modelo: {e}")

    return predictions

# Ejemplo de uso
# Suponiendo que 'user_data' es un DataFrame de Pandas con tus datos
# user_data = pd.read_csv('tu_archivo_de_datos.csv')
# try:
#     behavior_analysis = analyze_user_behavior(user_data)
#     print(behavior_analysis)
# except Exception as error:
#     print(f"Error: {error}")


# Explicación del Código
# Preprocesamiento de Datos: Los datos se normalizan antes de alimentarlos al modelo. Esto es crucial para muchos algoritmos de machine learning.
# Manejo de Excepciones: Se añaden bloques de try-except para manejar posibles errores durante el preprocesamiento y el entrenamiento del modelo.
# Validación de Entradas: Se verifica que la entrada sea un DataFrame de pandas, lo cual es una buena práctica para asegurar que la función reciba el tipo de datos esperado.
# Parámetros del Modelo: Se configura el modelo IsolationForest con parámetros específicos. Puedes ajustar estos parámetros según las necesidades de tu dataset.
# Documentación: Se añaden docstrings para explicar el propósito y uso de cada función y sus argumentos, lo cual es una práctica esencial en el desarrollo de software profesional.