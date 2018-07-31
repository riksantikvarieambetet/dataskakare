# Dataskakare

Python package with not so common data wrangling functions and API wrappers.

Dataskakare currently contains the following:

 - A cache enabled Google Vision wrapper.
 - A set of generators for the Europeana Search API.
 - A set of string transformations related to museum collections.

## Installing

```
pip install dataskakare
```

## Usage Examples

```python
from dataskakare import Europeana
from dataskakare import GoogleVision
from dataskalare.data_transformation import *

search = Europeana('europeana api key')

for item in search.provider_subject_generator('Stiftelsen Nordiska museet', 'Dräkt : Byxor'):
    print(item)

vision = GoogleVision('path to google service account file', cache=False) # true by default

vision.get_colors('url to image')
vision.get_labels('url to image')
vision.is_black_and_white('url to image')
```
