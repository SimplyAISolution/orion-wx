"""NEXRAD ingest placeholder.
TODO:
  - Stream from AWS Open Data 'noaa-nexrad-level2'
  - Backfill for event ranges
  - Write to Zarr/Parquet with STAC metadata
"""
from typing import Iterable

def ingest_nexrad(stations: Iterable[str], date: str) -> None:
    # Implement S3 listing & download, then convert to COG/Zarr as needed.
    pass
