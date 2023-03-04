# Car_Price_Predictor
The purpose of this app is to predict the price of a selected car based on the previous data available on that car by using **Machine Learning** algorithms. The app is available both in web application format and stable executable format. The data is cleaned, processed and then we performed EDA to explore the decisive pattern, All the models are tested on the data and **Random Forest** turns out to be the accurate one for this purpose

![Alt](/assets/image.png "image")

## Sources
1. To train the data, we need a dataset which will contain all the necessary, so we obtain the dataset from [Vehicle dataset](https://www.kaggle.com/datasets/nehalbirla/vehicle-dataset-from-cardekho)
2. The interface is designed on [PyGUI](https://dearpygui.readthedocs.io/en/latest/#:~:text=Dear%20PyGui%20is%20an%20easy,to%20create%20a%20functional%20layout.)

## Working Screenshots
![Alt](/assets/CarPricePredictor-1.png "Screenshot-1")
![Alt](/assets/CarPricePredictor-2.png "Screenshot-2")
![Alt](/assets/CarPricePredictor-3.png "Screenshot-2")

## Installation
1. Clone the Repo
2. Create a [Virtual Environment](https://packaging.python.org/en/latest/guides/installing-using-pip-and-virtual-environments/) through python, ``python -m venv carPredictor``
3. Activate the Virtual Enviroment ``./carPredictor/Scripts/activate``
4. Install the Requirements, In our case ``pip -m install -r requirements.txt``
5. ``python ./app.py``