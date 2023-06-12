# Think with Google Automation

Setting up and running the application

## Getting Started

You should be using python 3.x. Check your version with:
```
python --version
```

You will also need:
- pip
- xcode
- virtualenv

Install xcode command line tools
```
xcode-select --install
```

Install virtualenv
```
python3 -m venv /path/to/new/virtual/env
```

Create a virtual environment with python 3 in your root directory
```
virtualenv env -python=python3
```

Activate your virtual environment from your project root directory
```
source env/bin/activate
```

Install all necesary dependencies from requirements file
```
pip install -r requirements.txt
```

Download Chrome Driver for Selenium. Get it here: http://chromedriver.chromium.org/downloads

Download Geckodriver for Selenium. Get it here: https://github.com/mozilla/geckodriver/releases

## Running the tests

Run all the features from your local root (Chrome browser):
```
aloe
```

Run a specific feature
```
aloe features/feature_name.feature
```

Run a specific scenario from a feature.
```
aloe features/feature_name.feature --n 3
```

To run test in diferent browsers specify the BROWSER variable (Firefox: 'ff', Safari: 'safari')
```
BROWSER='ff' aloe
```
