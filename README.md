# fomo
### *Fear Of Missing mnemOnics*

**fomo** is a lightweight Python tool designed to collect **JWST Calibrated Engineering Data** (also called *mnemonics*).  
***The Goal??*** These engineering telemetry could help correct and improve JWST light curves by providing useful spacecraft and instrument context.

**JWST Engineering Database:**  
https://mast.stsci.edu/portal/Mashup/Clients/jwstedb/jwstedb.html

---

## Features

- Fetches JWST *mnemOnics* from the STScI Engineering Database using spelunker
- Useful for time-series analysis and systematics correction  

---

## Installation

Follow the steps below to install **fomo** in a clean environment.

### 1. Clone the repository

```bash
git clone https://github.com/sebastian-zieba/fomo.git

conda create -n fomo python==3.11.0

conda activate fomo

cd Desktop/Projects/Open_Source/fomo/fomo

pip install -e .

the last step might take a while... 
