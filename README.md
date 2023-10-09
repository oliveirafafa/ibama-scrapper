# Ibama Scrapper
**NOTE**: Tested with Python 3.10 version; may or may not work with other versions.

Package to download IBAMA environmental data for fines in Excel format
from the Brazilian Institute for the Environment and Renewable Natural Resources (IBAMA).


[![ibm_logo](http://upload.wikimedia.org/wikipedia/commons/thumb/8/81/Logo_IBAMA.svg/150px-Logo_IBAMA.svg.png)](https://www.ibama.gov.br)

# Data Sample

### **Check the final data by clicking [here](https://docs.google.com/spreadsheets/d/1sL8idZR0e20nhzjV9ne_s_t7f4wJpKM4LGkJtWZPXWs/edit?usp=sharing).**

# Installation and Usage

Clone this repo:

```bash
git clone https://github.com/oliveirafafa/ibama_scrapper.git
```

Install dependencies:

```bash
pip install -r requirements.txt
```
Then, run `main.py` file.

It will collect data from the endpoints referenced in `app/ibama_download_manager.py`; 
the files will be exported in the folder `output\ARRECADACAO` and `output\MULTA`.

## Contributing

I don't see a way to turn this project into something bigger, however, if you would like to contribute:

[![Donate](https://www.buymeacoffee.com/assets/img/custom_images/orange_img.png)](https://www.buymeacoffee.com/oliveiras)

Para meus amigos brasileiros, eu não vejo uma maneira de transformar este projeto em algo maior, porém, caso você queira contribuir:

[![Donate](https://img.shields.io/badge/Donate-PayPal-green.svg)](https://www.paypal.com/donate/?business=ZKZV2PRVUS7BA&no_recurring=0&currency_code=BRL)

Any help and suggestions will be apreciated.

