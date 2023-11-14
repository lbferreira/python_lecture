import numpy as np


def calculate_ndvi(red_band: np.ndarray, nir_band: np.ndarray) -> np.ndarray:
    """Compute the Normalized Difference Vegetation Index (NDVI) based on the red and near-infrared bands."""
    return (nir_band - red_band) / (nir_band + red_band)

def calculate_evi(
    blue_band: np.ndarray, red_band: np.ndarray, nir_band: np.ndarray
) -> np.ndarray:
    """Compute the Enhanced Vegetation Index (EVI) based on the blue, red and near-infrared bands."""
    return 2.5 * (nir_band - red_band) / (nir_band + 6 * red_band - 7.5 * blue_band + 1)
