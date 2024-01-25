# CoinSage

Welcome to CoinSage, your go-to solution for advanced cryptocurrency analytics and predictive insights. 
CoinSageWeb is designed to offer a wide range of services that set it apart from other platforms. 
Here's why CoinSage is the ultimate choice for your cryptocurrency analysis:

1. **Rich Data Sources** <br>
Overcoming dataset scarcity with CoinSage. We leverage platforms like Bitmex,
providing a standardized structure for different currencies, ensuring a robust and reliable dataset for accurate analysis.

2. **Unified Model Evaluation** <br>
No more running different codes for various models. CoinSage uses Hydra to facilitate a unified and equitable comparison
of different models. Understand arguments easily and run codes with different settings effortlessly.

3. **Hydra Configuration**<br>
Enhance your understanding of arguments and fine-tune parameters with Hydra. This hierarchical configuration framework 
simplifies code execution with various settings, providing flexibility and control.

4. **Effective Backtesting**<br>
Assess the real-world effectiveness of your models with CoinSageWeb's backtester. 
Develop successful trading strategies by evaluating your models in diverse scenarios.

5. **Comprehensive Metrics**<br>
CoinSage offers a diverse set of metrics for model evaluation. Analyze multiple metrics to identify areas for 
improvement and refine your models. Explore different metrics in the dedicated metrics section.

6. **Indicator Calculation**<br>
Unlike fetching indicators from various websites, CoinSage calculates them in a way that avoids issues like null rows
and missing information. This approach ensures accuracy and can be applied to other datasets.


# Overview

**Project Structure**

```
├── CoinSageWeb                    -- Main project folder
├── configs                        -- Hydra configuration files
├── live_data      
├── predictor_data_collector       -- Data collector for predictor
|  ├── models                      -- Predictor models
|  | ├── random_forest.py
|  | ├── lstm.py
|  | ├── arima.py
|  | ├── sarimax.py
|  | ├── prophet.py
|  | ├── ...
|  ├── bitmex_dataset.py
|  ├── bitmex_fetcher.py
|  ├── creator.py
|  ├── indicators.py 
|  ├── ...
├── user_management                 -- User management app
|  ├── models.py
|  ├── views.py
|  ├── forms.py
|  ├── urls.py
|  ├── ...
├── templates                       -- HTML templates
├── .gitignore
├── manage.py
├── requirements.txt
├── README.md
```

# Getting Started

**Dependencies**
Before diving in, make sure you have the following dependencies installed:
Python 3.8+<br>
pip >= 20.0.2<br>
Virtualenv

**Virtual Environment**<br>
Create a virtual environment and activate it:
```
pip install --upgrade virtualenv
virtualenv -p python 3.8 <venv_name>
source <venv_name>/bin/activate
pip install --upgrade pip
```

**Requirements**<br>
Install the required packages:
```
pip install -r requirements.txt
```

