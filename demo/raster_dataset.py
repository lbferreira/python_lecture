from __future__ import annotations

from typing import Any, List

import numpy as np
import rasterio
from affine import Affine


class RasterDataset:
    def __init__(
        self,
        data: np.ndarray,
        crs: Any,
        transform: Affine,
        band_names: List[str],
        nodata: Any,
    ) -> None:
        """Stores raster data and related metadata.

        Args:
            data (np.ndarray): raster data
            crs (Any): Coordinate Reference System.
            transform (Affine): Affine transformation matrix.
            band_names (List[str]): band names.
            nodata (Any): nodata value.
        """
        self.data = data
        self.crs = crs
        self.transform = transform
        self.band_names = band_names
        self.nodata = nodata

    @staticmethod
    def from_geotiff(file: str) -> RasterDataset:
        """Reads a GeoTIFF file and returns a RasterDataset object."""
        with rasterio.open(file) as src:
            data = src.read()
            band_names = src.descriptions
            crs = src.crs
            transform = src.transform
            nodata = src.nodata
        return RasterDataset(data, crs, transform, band_names, nodata)

    def get_band_data(self, band_name: str) -> np.ndarray:
        """Returns the data for the specified band."""
        # Here we could implement some logic to check if the requested band
        # is available. If not, we could raise an exception.
        return self.data[self._get_band_index(band_name)]

    def _get_band_index(self, band_name: str) -> int:
        """Returns the index of the specified band."""
        return self.band_names.index(band_name)

    def to_geotiff(self, file: str) -> None:
        """Writes the raster data to a GeoTIFF file."""
        with rasterio.open(
            file,
            "w",
            driver="GTiff",
            height=self.data.shape[1],
            width=self.data.shape[2],
            count=self.data.shape[0],
            dtype=self.data.dtype,
            crs=self.crs,
            transform=self.transform,
            nodata=self.nodata,
        ) as dst:
            dst.write(self.data)
            dst.descriptions = tuple(self.band_names)
