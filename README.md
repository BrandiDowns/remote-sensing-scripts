# remote-sensing-scripts
A collection of unrelated scripts useful for remote sensing.

* <b>read_nlcd.ipynb</b> shows how to plot a National Landcover Database (NLCD) GeoTIFF in <b>Python</b> and adjust the colormap to match the NLCD legend. This assumes you have an NLCD tif file reprojected (if needed) and ready.
  * NLCD data can be downloaded here: https://www.usgs.gov/centers/eros/science/national-land-cover-database

* <b>get_modis_ndvi_gee</b> is a short demonstration of how to do these things in <b>Google Earth Engine</b> (gee): 
  * download MODIS Normalized Difference Vegetation Index (NDVI) data over a multi-year time period
  * select a specific image from an image collection using the image index
  * MODIS NDVI data on GEE: https://developers.google.com/earth-engine/datasets/catalog/MODIS_006_MOD13A2
