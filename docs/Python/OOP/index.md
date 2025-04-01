# Object Orientated Programming and Packaging

So you've gotten your code to the stage where you'd like to provide a stable, usable, code for other to use and to build upon.
This is a fantastic stage to reach!
Whether your code is going to be completely open source (visible to everyone in the world) or only usable to a number of collaborators, there are some key things we should keep in mind when making our code available for others to use.

In this workshop we'll walk taking out code from a simple Python script, to a versitile, well-documented, Python package. We'll be focusing on the following topics:

* Classes and Inheritance
* Documentation
* Packaging
* Testing


## Starting Point

Let's start with some pre-existing code that we've written and would like to package up.

```python title="analaysis_script.py" linenums="1" hl_lines="1-2 6-12 15-19 23-26 28-31 34-38 42-45 49-52 56"
import numpy as np
import matplotlib.pyplot as plt


# load in the data from a csv file
data = np.loadtxt("data.csv", delimiter=",", comments="#")

# Get the properties of the data
data_mean = np.zeros(data.shape[1])
data_std = np.zeros(data.shape[1])
data_min = np.zeros(data.shape[1])
data_max = np.zeros(data.shape[1])

# Set the properties of the data in a loop
for i in range(data.shape[1]):
    data_mean[i] = data[:,i].mean()
    data_std[i] = data[:,i].std()
    data_min[i] = data[:,i].min()
    data_max[i] = data[:,i].max()



# Perform a min/max normalization of some columns
columns = [0,1,2]
for col in columns:
    data[:,col] = (data[:,col] - data_min[col]) / (data_max[col] - data_min[col])

# Perform a standard normalization of some other columns
columns = [3,4,5]
for col in columns:
    data[:,col] = (data[:,col] - data_mean[col]) / data_std[col]

# Recalculate the properties of the data
for i in range(data.shape[1]):
    data_mean[i] = data[:,i].mean()
    data_std[i] = data[:,i].std()
    data_min[i] = data[:,i].min()
    data_max[i] = data[:,i].max()


# Print out a summary of the datasets
for i in range(data.shape[1]):
    print(f"Column {i} has a mean value of {data_mean[i]:0.2f} and a standard deviation of {data_std[i]:0.2f}")
    print(f"The minimum value is {data_min[i]:0.2f} and the maximum value is {data_max[i]:0.2f}")
    print("\n")


# Plot the data in a histogram
for i in range(data.shape[1]):
    fig = plt.figure()
    plt.hist(data[:,i], bins = 20, alpha = 0.5, label = f"Column {i}")
    fig.show()


# Dump updated data to a file
np.savetxt("normalized_data.csv", data, delimiter=",")

input("Press Enter to continue...")
```

Let's break this down a little:

* On lines 1-2 we're importing the required libraries, namely `numpy` and `matplotlib`. 
* On lines 6-12 we're loading in data and assigning empty arrays for properties of our data.
* On lines 15-19 we're assigning to the property arrays.
* On lines 23-26 and 28-31 we're normalizing with either a min/max normalization or a standard normalization.
* On lines 34-38 we're resetting the property arrays.
* On lines 42-45 we're printing out a summary of the data column.
* On lines 49-52 we're plotting the data to a histogram.
* On line 56 we're dumping the modified data to a new CSV file.

Keeping in mind that we want our code to be versatile, easy to use and well documented, let's consider the following takeaways:

* The user needs to have `numpy` and `matplotlib` to run this code. These should be considered <i>requirements</i> or <i>dependencies</i>.
* When we load in data, we perform a number of operations and save some derived data. The user shouldn't need to worry about whether these arrays are getting properly set.
* We want to normalize the data using two similar ideas but different implementations. The user should expect similar interface when using either method to normalize the data.
* When the data is modified, we need to update the derived data. The user again shouldn't need to worry about correctly setting them. This would introduce a potential source of error.
* The derived data is used when printing summaries. We need to make sure these are up-to-date.
* When dumping to a CSV file, there is no check to see if we're overwriting data. This could lead to an unintentional loss of data.
* There is a lot of repeated code. Repeated code is highly susceptible to errors as one needs to make sure the same change is made in multiple places.

With these points in mind, let's start writing a Python package to make this workflow more user friendly.

# Python Package Layout

Let's start off by created a new directory called `my_package`. 
Within `my_package` we'll create an empty file called `__init__.py` (here `__file__.py` is pronounced "dunder file", hence `__init__.py` is "dunder init", calling it "init" is also understandable). 
This `__init__.py` is a special file in Python with a few functions. Firstly `__init__.py` tells Python that files in this directory can be `import`-ed into python. 
Once Python sees `__init__.py` it knows that any `.py` file within this directory can be `import`-ed. 
Secondly, `__init__.py` will act as an entry point to the package (or sub-package, more on this later). 
Within `__init__.py` we can specify what is `import`-ed by default using `from my_package import *`. 
We can do things like specify alias for functions within `__init__.py`.
Let's say we have the following:
```python title="__init__.py" linenums="1" hl_lines="2"
...
def my_super_complicated_long_function_name():
    ...


short_name = my_super_complicated_long_function_name

```
On line 2 we define a cumbersome function name that will be awkward to keep typing out.
However, on line 6 we assign `short_name` to be `my_super_complicated_long_function_name`. 
We can then import this function as `from my_package import short_name`.
We'll come back to this in more detail later, for now let's just stick with an empty `my_package/__init__.py`

Now let's just copy the `analysis_script.py` into `my_package` and wrap the main body of the script into a simple function, which takes the input filename as an argument:
```python title="my_package/analaysis_script.py" linenums="1" hl_lines="4"
import numpy as np
import matplotlib.pyplot as plt

def run_analysis(input_data):
    # load in the data from a csv file
    data = np.loadtxt(input_data, delimiter=",", comments="#")

    # Get the properties of the data
    data_mean = np.zeros(data.shape[1])
    data_std = np.zeros(data.shape[1])
    data_min = np.zeros(data.shape[1])
    data_max = np.zeros(data.shape[1])

    # Set the properties of the data in a loop
    for i in range(data.shape[1]):
        data_mean[i] = data[:,i].mean()
        data_std[i] = data[:,i].std()
        data_min[i] = data[:,i].min()
        data_max[i] = data[:,i].max()



    # Perform a min/max normalization of some columns
    columns = [0,1,2]
    for col in columns:
        data[:,col] = (data[:,col] - data_min[col]) / (data_max[col] - data_min[col])

    # Perform a standard normalization of some other columns
    columns = [3,4,5]
    for col in columns:
        data[:,col] = (data[:,col] - data_mean[col]) / data_std[col]

    # Recalculate the properties of the data
    for i in range(data.shape[1]):
        data_mean[i] = data[:,i].mean()
        data_std[i] = data[:,i].std()
        data_min[i] = data[:,i].min()
        data_max[i] = data[:,i].max()


    # Print out a summary of the datasets
    for i in range(data.shape[1]):
        print(f"Column {i} has a mean value of {data_mean[i]:0.2f} and a standard deviation of {data_std[i]:0.2f}")
        print(f"The minimum value is {data_min[i]:0.2f} and the maximum value is {data_max[i]:0.2f}")
        print("\n")


    # Plot the data in a histogram
    for i in range(data.shape[1]):
        fig = plt.figure()
        plt.hist(data[:,i], bins = 20, alpha = 0.5, label = f"Column {i}")
        fig.show()


    # Dump updated data to a file
    np.savetxt("normalized_data.csv", data, delimiter=",")

```


Let's also add a test data file to the base directory, this can be downloaded from here <b> TO DO</b>.

Our folder layout should look like this:
```
.
├── data.csv
└── my_package
    ├── analysis_script.py
    └── __init__.py

```

From here we can try and run the code (I'm using iPython):
```
In [1]: from my_package.analysis_script import run_analysis
In [2]: run_analysis("./data.csv")
```

Which worked! However, this is only local to this directory. If we change to a different location and try to rerun the above:
```
In [1]: from my_package.analysis_script import run_analysis
---------------------------------------------------------------------------
ModuleNotFoundError                       Traceback (most recent call last)
Cell In[1], line 1
----> 1 from my_package.analysis_script import run_analysis

ModuleNotFoundError: No module named 'my_package'
``` 

We want to package to be installed so that we can run the code from anywhere on our system. 
Let's look at how to do that next.


## Environment-wide install using pip and pyproject.toml

There are a few different methods we can choose when creating a package and installing it:

* Append the PYTHONPATH: Using this method we simply modify the location where Python searches when running `import`. This isn't a good choice, it requires user messing around with environmental variables. Not all users will be comfterble doing this. 
* Install using `setup.py`. This method will compile the Python code to byte code and place it into the correct location for Python to find when running `import`. Using this method, any user who has `pip` installed can install our package using `pip install .`. This isn't a bad option, it is also fairly widely used, however Python standards and package maintainers tend to move away from this method.
* Install using a `pyproject.toml` file. This is very similar to the `setup.py` method, except we'll be defining things like package name, file locations, additional data file, project metadata, all within the `pyproject.toml` file. 

`pyproject.toml` is the preferred method for a number of reasons. 
Firstly, it is tool agnostic, allowing us to use the installation tools that we are most fimilre with.
We can also include the requirements/dependencies within the `pyproject.toml` file.
A `toml` file is human-readable file format which uses modern syntax.
`pyproject.toml` integrates with other tools such as `commitizen`.
`pyproject.toml` conforms to python standards ([PEP 517](https://peps.python.org/pep-0517/)/[518](https://peps.python.org/pep-0518/))!


Let's start with a simple `pyproject.toml` file:
```toml title="pyproject.toml" linenums="1"
[build-system]
requires = ["setuptools >= 61.0", "setuptools-scm>=8.0"]
build-backend = "setuptools.build_meta"

[project]
dynamic = ["version"]
name = "my_package"
requires-python = ">= 3.8"
dependencies = [
    "numpy",
    "matplotlib",
]
authors = [
  {name = "Stephan O'Brien", email = "stephan.obrien@mcgill.ca"},
]
maintainers = [
  {name = "Stephan O'Brien", email = "stephan.obrien@mcgill.ca"}
]
description = "A python package for doing cool stuff"
readme = "README.md"
license = {file = "LICENSE"}

[tool.setuptools]
packages=[
  "my_package", 
]


[project.urls]
Homepage = "https://github.com/steob92/my_package/"
Documentation = "https://github.com/steob92/my_package/"
Repository = "https://github.com/steob92/my_package.git"
Issues = "https://github.com/steob92/my_package/issues"
Changelog = "https://github.com/steob92/my_package/blob/main/CHANGELOG.md"
```

There's a lot going on in this file. Let's take it apart:
```toml
[build-system]
requires = ["setuptools >= 61.0", "setuptools-scm>=8.0"]
build-backend = "setuptools.build_meta"
```

Here we are specifying the `build-system`, essentially what we're using to build the package. 
In this case we're using `setuptools`, hence adding it as a requirement with the `requires` variable.

```
[project]
dynamic = ["version"]
name = "my_package"
requires-python = ">= 3.8"
dependencies = [
    "numpy",
    "matplotlib",
]
authors = [
  {name = "Stephan O'Brien", email = "stephan.obrien@mcgill.ca"},
]
maintainers = [
  {name = "Stephan O'Brien", email = "stephan.obrien@mcgill.ca"}
]
description = "A python package for doing cool stuff"
readme = "README.md"
license = {file = "LICENSE"}
```

Here we're specifying some metadata about our package, including the name, version, who the authors/maintainers are and a short description. 
Here we can also specify a README and license file. 
The README acts as an introduction page about our package. 
Note here we're also specifying the required python version `requires-python = ">= 3.8"`. 
This syntax means that we need a python version which is greater than or equal to 3.8 to run the code.
We can also specify dependencies using the `dependencies` keyword. 
When we start building the package, pip will search for these dependencies within our environment and install them if they don't exist.

```
[tool.setuptools]
packages=[
  "my_package", 
]
```
Here we're specifying the packages (and sub-packages) that are to be installed as part of our package. We'll look at this is some more details later.
```
[project.urls]
Homepage = "https://github.com/steob92/my_package/"
Documentation = "https://github.com/steob92/my_package/"
Repository = "https://github.com/steob92/my_package.git"
Issues = "https://github.com/steob92/my_package/issues"
Changelog = "https://github.com/steob92/my_package/blob/main/CHANGELOG.md"
```

Here we're specifying some URLs that users can consult. For example the "Issues" URL will link to the github issues page of this repository.


With this package in place, we can simply install this package into our environment using `pip install .`:
```
Processing /raid/RAID1/Tutorials/python_packaging_working
  Installing build dependencies ... done
  Getting requirements to build wheel ... done
  Preparing metadata (pyproject.toml) ... done
Requirement already satisfied: numpy in /home/obriens/mambaforge/envs/dev/lib/python3.11/site-packages (from my_package==0.0.0) (1.26.4)
Requirement already satisfied: matplotlib in /home/obriens/mambaforge/envs/dev/lib/python3.11/site-packages (from my_package==0.0.0) (3.8.0)
Requirement already satisfied: contourpy>=1.0.1 in /home/obriens/mambaforge/envs/dev/lib/python3.11/site-packages (from matplotlib->my_package==0.0.0) (1.2.0)
Requirement already satisfied: cycler>=0.10 in /home/obriens/mambaforge/envs/dev/lib/python3.11/site-packages (from matplotlib->my_package==0.0.0) (0.11.0)
Requirement already satisfied: fonttools>=4.22.0 in /home/obriens/mambaforge/envs/dev/lib/python3.11/site-packages (from matplotlib->my_package==0.0.0) (4.25.0)
Requirement already satisfied: kiwisolver>=1.0.1 in /home/obriens/mambaforge/envs/dev/lib/python3.11/site-packages (from matplotlib->my_package==0.0.0) (1.4.4)
Requirement already satisfied: packaging>=20.0 in /home/obriens/mambaforge/envs/dev/lib/python3.11/site-packages (from matplotlib->my_package==0.0.0) (23.1)
Requirement already satisfied: pillow>=6.2.0 in /home/obriens/mambaforge/envs/dev/lib/python3.11/site-packages (from matplotlib->my_package==0.0.0) (10.2.0)
Requirement already satisfied: pyparsing>=2.3.1 in /home/obriens/mambaforge/envs/dev/lib/python3.11/site-packages (from matplotlib->my_package==0.0.0) (3.0.9)
Requirement already satisfied: python-dateutil>=2.7 in /home/obriens/mambaforge/envs/dev/lib/python3.11/site-packages (from matplotlib->my_package==0.0.0) (2.8.2)
Requirement already satisfied: six>=1.5 in /home/obriens/mambaforge/envs/dev/lib/python3.11/site-packages (from python-dateutil>=2.7->matplotlib->my_package==0.0.0) (1.16.0)
Building wheels for collected packages: my_package
  Building wheel for my_package (pyproject.toml) ... done
  Created wheel for my_package: filename=my_package-0.0.0-py3-none-any.whl size=2183 sha256=dd2ca561171519e9b5755e595d8ae619d67e3ec7593c00e8e29096d29e6b943d
  Stored in directory: /tmp/pip-ephem-wheel-cache-om8ak4ov/wheels/11/62/fc/593354b5442752b3bf9fa9c9fc8fe5e054389e3b47a6fb69bf
Successfully built my_package
Installing collected packages: my_package
Successfully installed my_package-0.0.0
```

This will now work from any directory as long as we're using the same Python environment!


## Converting our script into a versatile package using Object Orientated Programming

As was previously mentioned, `my_package/analysis_script.py` isn't very versatile. 
We ideally want something that other users can build upon. 
To do this we'll convert some data types into classes that we can then build upon. 
Let's start by making a base data class that we'll build upon. 
Create a subdirectory called `my_package/data`, within this directory let's create a `base.py` file:
```python title="my_package/data/base.py" linenums="1" hl_lines="1 3 5-10 16-19 22-24 26-33 47-56 59-60"
from numpy import ndarray, savetxt

class Base:

    _data = None
    data_mean = 0
    data_std = 0
    data_min = 0
    data_max = 0
    normalize_methods = ['minmax', 'standard']


    def __init__(self):
        pass

    def __str__(self):
        desc_string = self.describe()
        print (desc_string)
        return self.__class__.__name__    
    

    @property
    def data(self):
        return self._data

    @data.setter
    def data(self, value):
        self._data = value
        self.data_mean = self.data.mean()
        self.data_std = self.data.std()
        self.data_min = self.data.min()
        self.data_max = self.data.max()
        self.data_shape = self.data.shape
    


    def describe(self):
        data_string = f'Data has a mean value of {self.data_mean:0.2f}.\n'
        data_string += f'Data has a minimum value of {self.data_min:0.2f} and a maximum value of {self.data_max:0.2f}'
        return data_string
    

    def get_properties(self):
        return self.data_mean, self.data_std, self.data_min, self.data_max
    

    def normalize(self, method = 'minmax'):

        if method.lower() == 'minmax':
            self.data = (self.data  - self.data_min) / (self.data_max - self.data_min)

        elif method.lower() == 'standard':
            self.data = (self.data - self.data_mean) / self.data_std 

        else:
            raise RuntimeError (f'Method {method} not implemented. Please use one of {self.normalize_methods}')


    def to_file(self, filename):
        savetxt(filename, self.data, delimiter=",")

```

Some comments:

* On line 1 we're only `import`-ing what we need to use from `numpy`
* On line 3 we define the name of the class as `Base`
* On lines 5-10 we define some class member and data that we'll be using
* On lines 16-19 we're defining the `__str__` method which we define the behaviour when we run something like "print (my_base_class)".
* On lines 22-24 we're defining a property called data using the `@property` decorator. This acts as a "getter", instead of accessing the real data `_data` the user accesses a copy of the data called `data`.
* On lines 26-33 we're defining the "setter" of `data` using the `@data.setter` decorator. This defines the behaviour when we're assigning values to `data`. When the user calls `my_base_class.data = some_data`, they're actually calling this function. This allows for `_data` to be updated and the data properties to be automatically determined whenever `data` is modified.
* On lines 47-56 we've defined a `normalize` function which allows the user to normalize the data using either a min/max or standard normalization based on a keyword. This defaults to a min/max normalization. Since we've set the property `data`, when we assign with `self.data = ...` the setter function is called, `self._data` is updated the data properties (min, max, mean, std) are also recalculated.
* On lines 59-60 we're created a member function to dump the data to a CSV file.

!!! info "Aside on data classes"
    Python now has a special class type called "Data Classes". 
    Using data classes allows one to create data-based classes like the one above.
    For the sake of illustration, we won't be using data classes in this tutorial.
    See [here](https://docs.python.org/3/library/dataclasses.html) for more details.


We now want to make this package visible anyone using this package. Firstly we need to add a `__init__.py` file to this folder:
``` linenums="1" hl_lines="6"
├── data.csv
├── my_package
│   ├── analysis_script.py
│   ├── data
│   │   ├── base.py
│   │   └── __init__.py
│   └── __init__.py
├── normalized_data.csv
└── pyproject.toml
```

Secondly, we need to add this location to the `pyproject.toml` file:
```toml linenums="1" hl_lines="26"
[build-system]
requires = ["setuptools >= 61.0", "setuptools-scm>=8.0"]
build-backend = "setuptools.build_meta"

[project]
dynamic = ["version"]
name = "my_package"
requires-python = ">= 3.8"
dependencies = [
    "numpy",
    "matplotlib",
]
authors = [
  {name = "Stephan O'Brien", email = "stephan.obrien@mcgill.ca"},
]
maintainers = [
  {name = "Stephan O'Brien", email = "stephan.obrien@mcgill.ca"}
]
description = "A python package for doing cool stuff"
readme = "README.md"
license = {file = "LICENSE"}

[tool.setuptools]
packages=[
  "my_package", 
  "my_package.data", 
]


[project.urls]
Homepage = "https://github.com/steob92/my_package/"
Documentation = "https://github.com/steob92/my_package/"
Repository = "https://github.com/steob92/my_package.git"
Issues = "https://github.com/steob92/my_package/issues"
Changelog = "https://github.com/steob92/my_package/blob/main/CHANGELOG.md"
```

If we now rerun `pip install .`, we can now import our base class:
```python linenums="1" hl_lines="2"
In [1]: import numpy as np
In [2]: from my_package.data.base import Base
In [3]: my_data = Base()
In [4]: my_data.data = np.random.random((10,10))
In [5]: my_data.data_min
Out[5]: 0.010934507239608426
In [6]: my_data.data_max
Out[6]: 0.9917396588604535
```

It is often very useful to have a method or class of randomly generated data for testing pipelines.
Let's build on top of the `Base` class by creating a class that will generate random data.
```python title="my_package/data/random.py" linenums="1" hl_lines="1 4 17"
from .base import Base
from numpy.random import random, normal

class RandomData(Base):

    # Define the implemented methods
    implemented_methods = ['uniform', 'normal']

    def __init__(
            self, 
            shape, 
            rnd = 'uniform',
            mean = 0,
            width = 1 ):

        # Call the parent's constructor
        super().__init__()  

        # Uniform Random Numbers
        if rnd.lower() == 'uniform':
            self.data = random(shape)
        # Normal Random Numbers
        elif rnd.lower() == 'normal':
            self.data = normal(loc = mean, scale = width, size = shape)
        else:
            raise RuntimeError(f'Random method "{rnd}" is not implemented. Please use one of the implemented methods {self.implemented_methods} ')
```

* Notice on line 1 we're importing using `from .base import Base`. Here the `.base` is specifying that we're looking for a file called `base.py` within the same directory (`.`). If we wanted to search in the parent directory (one directory above) we'd use `from ..base import Base`. This is similar to the `.` and `..` path when working with `bash`.
* On line 4 we define the `RandomData` class, specifying that it inherits from the `Base` class. This means that `RandomData` will have all the same functionality as `Base`, meaning the `self.data` setter will also work for `RandomData`.
* On line 17 we're calling the parent class's constructor using `super().__init__()`. When ever we want to explicitly call the parent class's version of a function, we can call `super().function()`.


Since `"my_package.data"` has already been added to the `pyproject.toml` file `my_package/data/random_data.py` will be installed with `pip install .`. We can try run this:
```python linenums="1" hl_lines="26"
In [1]: from my_package.data.random_data import RandomData
In [2]: my_data = RandomData((5,100))
In [3]: my_data.data_max
Out[3]: 0.9959056068848283
In [4]: my_data.data_shape
Out[4]: (5, 100)
```

You'll notice that the import is pretty long and cumbersome to type. 
Let's make this a little easier for the user by playing around with the `__init__.py` files. 
Firstly let's modify `my_package/data/__init__.py`:
```python title="my_package/data/__init__.py" linenums="1" hl_lines="1 4"
from .random_data import RandomData

# Define what is imported with 'from here import *'
__all__ = ["RandomData"]
```
Here we're importing `RandomData` making it easily available from `my_package.data` rather than `my_package.data.random_data`. 
We then create a variable called `__all__` and assign it to a list (`["RandomData"]`). This specifies what is imported when running `from my_package.data import *`.

Next let's modify `my_package/__init__.py`:
```python title="my_package/__init__.py" linenums="1" hl_lines="1 4"
from .data import RandomData

# Define what is imported with 'from here import *'
__all__ = ["RandomData"]
```
Notice that we no longer need to import from `.data.random_data`, we can just import from `.data`. 
We can do this because `RandomData` is already visible within `my_package.data`. 
We now have a few ways to import `RandomData`:

* `from my_package import *`
* `from my_package import RandomData`
* `from my_package.data import *`
* `from my_package.data import RandomData`
* `from my_package.data.random_data import RandomData`

A user no longer needs to know that `RandomData` is nested within `data`. Reinstalling with `pip install .`, we can run the previous example with:
```python linenums="1" hl_lines="1"
In [1]: from my_package import RandomData
In [2]: my_data = RandomData((5,100))
In [3]: my_data.data_max
Out[3]: 0.9959056068848283
In [4]: my_data.data_shape
Out[4]: (5, 100)
```

## Making a CSV Data loader

Now that we have a base class `Base` and a tester class `RandomData`, let's add a CSV reader class within the `my_package/data` directory:
```python title="my_package/data/csv_data.py" linenums="1 12-21 23-25" hl_lines="1"
from .base import Base
import numpy as np


class CSVData:

    def __init__(self, filename):

        self.data = []
        self.read_file(filename)

    def read_file(self, filename):
        data = np.loadtxt(filename, delimiter=',', comments = '#')
        n_data = data.shape[0]
        n_cols = data.shape[1]

        for i in range(n_cols):
            datum = Base()
            datum.data = data[:,i]
            self.data.append(datum)
        self.len = len(self.data)
    
    @classmethod
    def from_file(cls, filename):
        return cls(filename)
```

Here `CSVData` doesn't explicitly inherent from `Base`, but there is an internal data type `self.data` which is a list of `Base`. 

Lines 12-21 defines the `read_file` function which will extract the data from the CSV file and stores each column into a `Base` data type.

On lines 23-25 we're defining a class method using the `@classmethod` decorator. 
A class method allows us to call functions associated to the class which aren't associated with a specific instance. 
In this case the `from_file` method will call `__init__`, passing the `filename`.
This will allow us to generate a new object using `CSVData.from_file(filename)`.

Let's update the `__init__.py` files with the new class:

```python title="my_package/data/__init__.py" linenums="1" hl_lines="1 4"
from .random_data import RandomData
from .csv_data import CSVData

# Define what is imported with 'from here import *'
__all__ = ["RandomData", "CSVData"]
```

Next let's modify `my_package/__init__.py`:
```python title="my_package/__init__.py" linenums="1" hl_lines="1 4"
from .data import RandomData, CSVData

# Define what is imported with 'from here import *'
__all__ = ["RandomData", "CSVData"]
```

## Adding some package data

It might be useful to have some data included within the package. 
This could be some reference data or some test data.
Let's start by adding the CSV file into our package. 
We'll add it to `my_package/package_data/data.csv`. 
For the package data to be visible, we'll need to add a `MANIFEST.in` file
```title="MANIFEST.in"
include my_package/package_data/*.csv
```

Let's then update the `CSVData` class to have a method to import this data:
```python title="my_package/data/csv_data.py" linenums="1" hl_lines="3"
from .base import Base
import numpy as np
import pkg_resources

class CSVData:

    def __init__(self, filename):

        self.data = []
        self.read_file(filename)

    def read_file(self, filename):
        data = np.loadtxt(filename, delimiter=',', comments = '#')
        n_data = data.shape[0]
        n_cols = data.shape[1]

        for i in range(n_cols):
            datum = Base()
            datum.data = data[:,i]
            self.data.append(datum)
        self.len = len(self.data)

    @classmethod
    def from_file(cls, filename):
        return cls(filename)


    @classmethod
    def get_titanic(cls) -> 'CSVData':
        return cls(pkg_resources.resource_filename('my_package','package_data/Titanic.csv'))
```

Here we're using `pkg_resources` to access the location of the package data from the installation location.
Now calling `CSVData.get_titanic_data()` will return a `CSVData` object with the dataset loaded.


# Documenting Our Code

So far we've written code with little-to-no documentation. 
For a small single-use analysis script, this might be ok.
However, as our code increases in complexity and we want to start sharing it with others, we need to better document our code.
Furthermore, we need to remember that undocumented code my become completely unreadable to anyone not in your current mindstate.
This include ourselves. 
A very common problem people have is returning to old code and failing to understand the code without hours of reading and debugging.

In this section we'll look at the following topics:

* Documenting our code with docstrings, providing useful help messages for users.
* Using "type-hinting" to show the data types being used and returned by functions
* Combining the above to easily make documentation pages like [numba.readthedocs.io](https://numba.readthedocs.io/en/stable/)

## Docstrings

Docstrings are a standard method used to describe one's code. 
Docstrings use a format that is well defined and utilised by Python and documenation software.

Here are some links discussing documenting one's code using docstrings:

* [Real Python: Documenting Python Code](https://realpython.com/documenting-python-code/)
* [Example Google Style Python Docstrings](https://sphinxcontrib-napoleon.readthedocs.io/en/latest/example_google.html)
* [THe Hitchhiker's Guide to Python: Documentation](https://docs.python-guide.org/writing/documentation/)


There are many different standards, but they all use a common syntax, that is a long string defined just after a function/class declaration:
```python title="docstring_example.py" linenums="1"
def my_function(a,b):
    """A simple function to add two numbers together

    This function will take in two numbers (a and b) and return their sum (a + b)

    Parameters
    ----------
    a : float
        The first number 

    b : float
        The second number

    Returns
    -------
    float
        The sum of a and b
    """
    
    return a + b

```

Notice that the docstring starts and end with 3 quotation marks `"""`. 
It is place directly after the functions/class declaration.
The first line is a high-level description of the function/class followed by an optional more detailed description.
We then define `Parameters` and `Returns` and list what the parameters/returns are, their type and how they are used.
We can also add things like examples, tests (which can be evaluated with a module like [doctest](https://docs.python.org/3/library/doctest.html)) and any error handling does using `raise exception` (see [here](https://sphinxcontrib-napoleon.readthedocs.io/en/latest/example_google.html) for some examples).
Using a docstring like this, a new developer has a good idea of what the function does and the expected behaviour.
Futhermore the user can also call the `help` function to return the docstring:
```python
help(my_function)
```
```
Help on function my_function in module __main__:

my_function(a, b)
    A simple function to add two numbers together
    
    This function will take in two numbers (a and b) and return their sum (a + b)
    
    Parameters
    ----------
    a : float
        The first number 
    
    b : float
        The second number
    
    Returns
    -------
    float
        The sum of a and b

```
This provides a useful resource for the user without the need to dig through the code to determine the expected behaviour of the function.

Let's start looking at `my_package/data/base.py` and add some docstrings:
```python title="my_package/data/base.py" linenums="1" hl_lines="102-105 115"
from numpy import ndarray

class Base:
    """This is the base class for all the classes in this package.
    
    """

    _data = 0
    data_mean = 0
    data_std = 0
    data_min = 0
    data_max = 0
    
    normalize_methods = ['minmax', 'standard']


    def __init__(self):
        """This is the constructor of the class."""

        pass

    def __str__(self):
        """This is the string representation of the class.
        
        Returns
        -------
        str
            The name of the class
        """

        desc_string = self.describe()
        print (desc_string)
        return self.__class__.__name__    
    

    @property
    def data(self):
        """This is the data property.
        
        Returns
        -------
        ndarray
            A numpy array of the data
        """

        return self._data

    @data.setter
    def data(self, value):
        """This is the setter for the data property.
        
        Parameters
        ----------
        value : ndarray
            A numpy array that will be stored as the data
        """

        self._data = value
        self.data_mean = self.data.mean()
        self.data_std = self.data.std()
        self.data_min = self.data.min()
        self.data_max = self.data.max()
        self.data_shape = self.data.shape
        


    def describe(self):
        """This method prints a summary of the data.
        
        Returns
        -------
        str
            A description of the data
        """

        data_string = f'Data has shape {self.data_shape}, with a mean value of {self.data_mean:0.2f}.\n'
        data_string += f'Data has a minimum value of {self.data_min:0.2f} and a maximum value of {self.data_max:0.2f}'
        return data_string
    

    def get_properties(self):
        """This method returns the mean, standard deviation, minimum and maximum of the data.
        
        Returns
        -------
        (float, float, float)
            A tuple with the mean, standard deviation, minimum and maximum of the data.
            
        """

        return self.data_mean, self.data_std, self.data_min, self.data_max
    

    def normalize(self, method = 'minmax'):
        """This method normalizes the data.
        
        Parameters
        ----------
        method : str
            The method to use for normalization. Can be 'minmax' or 'standard'.
        
        Raises
        ------
        RuntimeError
            If `method` has not yet been implemented
        """

        if method.lower() == 'minmax':
            self.data = (self.data  - self.data_min) / (self.data_max - self.data_min)

        elif method.lower() == 'standard':
            self.data = (self.data - self.data_mean) / self.data_std 

        else:
            raise RuntimeError (f'Method {method} not implemented. Please use one of {self.normalize_methods}')

```

In the above example we've added docstrings to `my_package/data/base.py`.
Notice that the `normalize` function has the potential to raise a `RuntimeError` (line 115).
This potential error steam is documented in the docstring on lines 102-105.

## Type Hinting

Type hinting is an excellent way to inform developers and users of what type the arguments and returns are. 
This is done by labeling arguments and returns with the expected type.
Let's look again at simple function we used to get the sum of two numbers:

```python title="type_hinting_example.py" linenums="1" hl_lines="1"
def my_function(a : float ,b : float) -> float:
    """A simple function to add two numbers together

    This function will take in two numbers (a and b) and return their sum (a + b)

    Parameters
    ----------
    a : float
        The first number 

    b : float
        The second number

    Returns
    -------
    float
        The sum of a and b
    """
    
    return a + b

```

Here on line 1 we modify the function definition to include the data types. 
We specify the type of `a` and `b` using the syntax `var : type`.
In this case we use `a : float, b : float` to indicate that `a` and `b` are expected to be of type `float`.
Additionally we indicate what the return value is using `-> type` after the function definition.
In this case we're returning a float, so `def my_function(a : float ,b : float) -> float:`. 
We can also specify default parameters using the syntax `var : type = default`. For example:
```python title="type_hinting_example.py" linenums="1" hl_lines="1 12"
def my_function(a : float ,b : float = 1.) -> float:
    """A simple function to add two numbers together

    This function will take in two numbers (a and b) and return their sum (a + b)

    Parameters
    ----------
    a : float
        The first number 

    b : float
        The second number, defaults to 1.

    Returns
    -------
    float
        The sum of a and b
    """
    
    return a + b

```

Here `b` is of type `float` and has a default value of `1.0`. 
This means that if the user calls `my_function(3)`, they'll get a return of `4`, whereas if the user calls `my_function(3, 2)` they'll get a return of `5`.

A very useful package to use when implementing type hinting is the `typing` library.
`typing` has a lot of useful imports, for example:

* `List[type1, type2, ..., typen]`, this can be used when we expect a `list` of types `type1,...,typen`.
* `Tuple[type1, type2, ..., typen]`, this can be used when we expect a `tuple` of types `type1,...,typen`.
* `Option[type]`, this can be used for optional values
* `Union[type1, type2]`, this can be used when a varibable can have either `type1` or `type2`.

See [typing cheat sheet](https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html) for more examples.

Let's use `typing` in the `my_function` example:

```python title="type_hinting_example.py" linenums="1" hl_lines="1 2 13"
from typing import Optional
def my_function(a : float ,b : Optional[float] = 1.) -> float:
    """A simple function to add two numbers together

    This function will take in two numbers (a and b) and return their sum (a + b)

    Parameters
    ----------
    a : float
        The first number 

    b : Optional[float]
        The second number, defaults to 1.

    Returns
    -------
    float
        The sum of a and b
    """
    
    return a + b

```

On line 1 we import `Optional` from `typing`.
On line 2 the `my_function` definition is updated to reflect that `b` is an `Optional` parameter of type `float`.
We also update the docstring on line 12 to show that this is an `Optional` parameter.

Now that we have an idea of how type hinting works, let's update the `my_package/data/base.py` file:
```python title="my_package/data/base.py" linenums="1" hl_lines="1 2 8-12 14 21 36 48 80 92"
from numpy import ndarray
from typing import List, Tuple, Optional

class Base:
    """This is the base class for all the classes in this package.
    
    """
    _data : ndarray
    data_mean : float
    data_std : float
    data_min : float
    data_max : float
    
    normalize_methods : List[str] = ['minmax', 'standard']


    def __init__(self):
        """This is the constructor of the class."""
        pass

    def __str__(self) -> str:
        """This is the string representation of the class.

        Returns
        -------
        str
            The name of the class
        """
        
        desc_string = self.describe()
        print (desc_string)
        return self.__class__.__name__    
    

    @property
    def data(self) -> ndarray:
        """This is the data property.

        Returns
        -------
        ndarray
            A numpy array of the data
        """
        
        return self._data

    @data.setter
    def data(self, value) -> None:
        """This is the setter for the data property.

        Parameters
        ----------
        value : ndarray
            A numpy array that will be stored as the data
        """
        
        self._data = value
        self.data_mean = self.data.mean()
        self.data_std = self.data.std()
        self.data_min = self.data.min()
        self.data_max = self.data.max()
        self.data_shape = self.data.shape
        


    def describe(self) -> str:
        """This method prints a summary of the data.

        Returns
        -------
        str
            A description of the data
        """
        
        data_string = f'Data has shape {self.data_shape}, with a mean value of {self.data_mean:0.2f}.\n'
        data_string += f'Data has a minimum value of {self.data_min:0.2f} and a maximum value of {self.data_max:0.2f}'
        return data_string
    

    def get_properties(self) -> Tuple[float, float, float]:
        """This method returns the mean, standard deviation, minimum and maximum of the data.
        
        Returns
        -------
        Tuple[float, float, float]
            A tuple with the mean, standard deviation, minimum and maximum of the data.
            
        """
        return self.data_mean, self.data_std, self.data_min, self.data_max
    

    def normalize(self, method : Optional[str] = 'minmax') -> None:
        """This method normalizes the data.
        
        Parameters
        ----------
        method : Optional[str]
            The method to use for normalization. Can be 'minmax' or 'standard'.
        
        Raises
        ------
        RuntimeError
            If `method` has not yet been implemented
        """

        if method.lower() == 'minmax':
            self.data = (self.data  - self.data_min) / (self.data_max - self.data_min)

        elif method.lower() == 'standard':
            self.data = (self.data - self.data_mean) / self.data_std 

        else:
            raise RuntimeError (f'Method {method} not implemented. Please use one of {self.normalize_methods}')

```

On line 2 we import `List`, `Tuple` and `Optional` from `typing`. 
On lines 8-12 the types of the class data are added, noting that `ndarray` was imported on line 1.
On lines 90, 92 we're utilizing the `typing` imports in the function definition.
Some functions don't have a return (e.g. line 48), in these cases we can use the type `None` to specify that nothing is returned.