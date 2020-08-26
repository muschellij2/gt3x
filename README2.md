# Read Raw GT3X file
An implementation of extract raw acceleration data from .gt3x files.

The script gt3x_functions.py contains code to extract raw acceleration data from .gt3x files. Each .gt3x file is basically a zip file containing a log.bin and a info.txt file. The log.bin is a binary file which contains the actual acceleration values. The info.txt file contains the meta-data in text form. When the script is executed, it will create a numpy file that contains the raw data and a time vector.

### Usage
```bash
import gt3x
actigraph_acc, actigraph_time, meta_data = gt3x.read_gt3x('AI9_NEO1F16120039_2017-06-27.gt3x')
```

## Installation

```bash
pip3 install -r requirements.txt
```

