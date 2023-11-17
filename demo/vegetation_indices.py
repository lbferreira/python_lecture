from typing import Callable, List

import numpy as np
from raster_dataset import RasterDataset


def calculate_ndvi(raster: RasterDataset) -> np.ndarray:
    """Compute the Normalized Difference Vegetation Index (NDVI) based on the red and near-infrared bands."""
    nir_band = raster.get_band_data("B08")
    red_band = raster.get_band_data("B04")
    return (nir_band - red_band) / (nir_band + red_band)


def calculate_evi(raster: RasterDataset) -> np.ndarray:
    """Compute the Enhanced Vegetation Index (EVI) based on the blue, red and near-infrared bands."""
    nir_band = raster.get_band_data("B08")
    red_band = raster.get_band_data("B04")
    blue_band = raster.get_band_data("B02")
    return 2.5 * (nir_band - red_band) / (nir_band + 6 * red_band - 7.5 * blue_band + 1)


def apply_vi_fns(
    raster: RasterDataset, fns: List[Callable[[RasterDataset], np.ndarray]], out_band_names: List[str]
) -> RasterDataset:
    """Apply a list of vegetation index functions to a raster.

    Args:
        raster (RasterDataset): input raster.
        fns (List[Callable[[RasterDataset], np.ndarray]]): a list of functions that calculate vegetation indices.
        out_band_names (List[str]): names of the output bands.

    Returns:
        RasterDataset: a new RasterDataset object with the vegetation indices.
    """
    results = []
    for fn in fns:
        vi_result = fn(raster)
        results.append(vi_result)
    stacked_results = np.stack(results, axis=0)

    # Create a new RasterDataset object with the vegetation indices
    out_raster = RasterDataset(
        data=stacked_results,
        crs=raster.crs,
        transform=raster.transform,
        band_names=out_band_names,
        nodata=raster.nodata
    )
    return out_raster
