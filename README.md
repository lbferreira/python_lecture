# Hints for developing a sound Python project

This material was created for a short Python lecture offered in the Geospatial Computing for Environmental Research (GCER) Lab at the Mississippi State University on November 2023. The goal of this lecture is to provide some hints for developing a sound Python project. The material is divided in two parts: a brief presentation and a code example. The [presentation](Hints%20for%20developing%20a%20Python%20project.pdf) offers some hints for developing a sound Python project. The code example is a practical example that shows how to apply some of the hints showed in the presentation. The code is provided in the [demo folder](demo/). A complete description of the coding task is provided below.

## Presentation
- A brief presentation offering some hints for developing a sound Python project is provided [here](Hints%20for%20developing%20a%20Python%20project.pdf).
## Code example
- A practical coding example is provided in the [demo folder](demo/).
- The ideia for the code example is providing an initial code and an improved version of it.
- The goal of the code is to read a geotiff file, compute vegetation indices, stack them, plot them, and export the result as a geotiff file.
- The initial code is in a jupyter notebook [(my_analysis.ipynb)](demo/my_analysis.ipynb) and it works fine. However, the idea is to improve it, making it more readable, reusable, and reliable.
- The improved version of the code is split in three files:
  - [my_analysis_refactored.ipynb](demo/my_analysis_refactored.ipynb): a jupyter notebook with the main code, which relies on the modules described below.
  - [raster_dataset.py](demo/raster_dataset.py): a python module with a class called `RasterDataset`.
  - [vegetation_indices.py](demo/vegetation_indices.py): a python module with some functions to compute vegetation indices and apply them to a RasterDataset object.

### Code improvement explanation
The improvements done in the code have the ideas described below.
- Creation of a module (raster_dataset.py) with a class to represent a raster dataset:
    - To make the use a raster data more easy, a class called `RasterDataset` was created. This class represents a raster dataset, containing its data (numpy array) and related metadata (crs, transform, nodata value, and band names).
    - To make it more easy to use, the class has a method (from_geotiff) that allows the user to create a RasterDataset object from a geotiff file. To make it possible to have a method inside a class that can create an object of the same class, the method was defined as a static method. It means that the method can be called without an object of the class. For example, to create a RasterDataset object from a geotiff file, the user can do:
    `dataset = RasterDataset.from_geotiff('my_geotiff.tif')`. The variable `dataset` is a RasterDataset object created from the geotiff file.
    - The class also has a method (to_geotiff) that allows the user to quickly export the data as a geotiff file.
    - Finally, the class has a method (get_band_data) that returns the data of a specific band from its name. For example, to get the data of a band called 'B04', we can do: `band_data = dataset.get_band_data('B04')`. In this case, `dataset` is a RasterDataset object and `band_data` is a numpy array with the data of the band 'B04'.
- Creation of a module (vegetation_indices.py) with functions to compute and apply vegetation indices to a RasterDataset object:
    - To make the code more readable and reusable, the functions to compute vegetation indices were moved to a separate module (vegetation_indices.py).
    - Now the functions can handle a RasterDataset object as input and return a numpy array as output.
    - Finally, we created a function (apply_vi_fns) to receive a list of vegetation indices functions and apply them to a RasterDataset object. The output of this function is also a RasterDataset object.
- Improvement of the jupyter notebook with the main code(my_analysis_refactore.ipynb).
    - This notebook is an improved version of the initial code (my_analysis.ipynb) that relies on the modules that we created.
    - Now, in this notebook, we can focus on our task and we don't need to worry about the details of how to read a geotiff file, how to compute vegetation indices, and how to export the result as a geotiff file.
- Additional comments:
    - The code was also improved by adding docstrings and type hints.

### Final remarks
- The improved code is now more readable, reusable, and reliable. It's also more modular. Thus, it's easier to maintain and extend our code an to reuse it in other projects.
- To do the improvements, we used some good practices of software development. For example, we reduced copling and increase cohesion when we created a class to represent a raster dataset and a module with functions to compute and apply vegetation indices. We also reduced code duplication.
- The ideia explored when we created a function to apply a list of vegetation indices functions to a RasterDataset object (apply_vi_fns) is inspired by a design pattern called Strategy Pattern. This pattern allows us to define different algorithms and make them interchangeable. In our case, the algorithms are the vegetation indices functions. Thus, we can add/change vegetation indices functions without changing the code that applies them to a RasterDataset object. Although the Strategy Pattern was originally defined using classes, we can also adapt it to use functions. For a more in depth explanation of the Strategy Pattern, please see: https://youtu.be/WQ8bNdxREHU
- For more information about good practices of software development, I strongly recommend the YouTube channel [ArjanCodes](https://www.youtube.com/@ArjanCodes). As a first video, I recommend the video [Cohesion and Coupling: Write BETTER PYTHON CODE Part 1](https://youtu.be/eiDyK_ofPPM).
- The ideia of this code example was to show some good practices of software development. However, it's important to mention that there are other good practices that we didn't explore here. For example, we didn't handle exceptions, which is an important practice in software development.
- One of the limitations of our improved code is that the vegetation indices functions need to know the name of the bands they require. For example, the NDVI function needs to know that it requires the bands 'B04' and 'B08'. To solve it, one of the possible approaches is creating a configuration file (a .env file for example) with the name of each type of band. In this way, we can map the band type (e.g., red and nir) to its actual name in the dataset (e.g., B04 and B08). Another approach is converting the vegetation indices functions to classes. Thus, we can pass the name of the required bands as arguments to the class constructor.
- FINAL HINT: if you are starting with Python, all these concepts may seem confusing for you. However, don't worry. You don't need to know all these concepts to start coding in Python but it's good to know that they exist. As you gain more experience with Python, you can start to understand them better and use them in your projects. Keep coding and have fun!