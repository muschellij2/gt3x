# Read Raw GT3X file
An implementation of extract raw acceleration data from .gt3x files.

This package was extracted and expanded upon from the work of Shaheen Syed and his repositories https://github.com/shaheen-syed/CNN-Non-Wear-Time-Algorithm and https://github.com/shaheen-syed/ActiGraph-ActiWave-Analysis.  They are instrumental in this module creation.

The script gt3x_functions.py contains code to extract raw acceleration data from .gt3x files. Each .gt3x file is basically a zip file containing a log.bin and a info.txt file. The log.bin is a binary file which contains the actual acceleration values. The info.txt file contains the meta-data in text form. When the script is executed, it will create a numpy file that contains the raw data and a time vector.

### Usage

The `gt3x` module needs to be first installed.  The most up-to-date one is:

```bash
pip install git+https://github.com/muschellij2/gt3x.git#egg=gt3x
````

But can also be installed via `pip` from [PyPi](https://pypi.org/project/gt3x/):

```bash
pip install gt3x
```

```bash
import gt3x
actigraph_acc, actigraph_time, meta_data = gt3x.read_gt3x('AI9_NEO1F16120039_2017-06-27.gt3x')
```

## Installation

```bash
pip3 install -r requirements.txt
```

