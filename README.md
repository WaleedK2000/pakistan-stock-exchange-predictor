# Pakistan Stock Exchange Predictor

This repository contains a linear classifier model that predicts the closing price of Pakistan Stock Exchange based on given Open, High, Low, and Volume values.

## Dataset

The dataset used in this model was obtained from Kaggle: https://www.kaggle.com/datasets/mirfanazam/pakistan-stock-exchange-complete. It contains historical data of Pakistan Stock Exchange from January 2012 to December 2018.

## Usage

To use this model, you need to provide Open, High, Low, and Volume values as input. The model will then predict the closing price based on these values.

## Dependencies

This project requires the following dependencies:
- Python 3.7+
- Scikit-learn
- Pandas
- Numpy

## Installation

1. Clone this repository to your local machine:

```
git clone https://github.com/username/pakistan-stock-exchange-predictor.git
```

2. Install the required dependencies:

```
pip install -r requirements.txt
```


## Docker

To run the application in a Docker container, you can use the included Dockerfile. To build the Docker image, navigate to the project directory and run the following command:

```
docker build -t pakistan-stock-exchange-predictor .
```


This will build a Docker image with the tag "pakistan-stock-exchange-predictor". To run the container, use the following command:

```
docker run -p 5000:5000 pakistan-stock-exchange-predictor
```


This will start the container and map port 5000 of the container to port 5000 of the host machine. You can then access the application at http://localhost:5000/.

## License

This project is licensed under the MIT License. See the LICENSE file for details.
