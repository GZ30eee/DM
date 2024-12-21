# Data Mining Projects

This repository contains a collection of data mining projects demonstrating various techniques such as association rule mining, clustering, sentiment analysis, and more. Below is a list of the projects included in this repository:

---

### **Projects Overview**

#### **Apriori Algorithm**
- `main.py`

An implementation of the Apriori algorithm for mining frequent itemsets and generating association rules.

#### **Association Rule Generator**
- `ap.py`

A tool that generates association rules based on the results from the Apriori algorithm.

#### **Binning Methods**
- `bin.py`

A project demonstrating various binning techniques to discretize continuous data into discrete bins.

#### **Clustering Visualization**
- `clu.py`

A project that visualizes the clustering of data using K-Means and other clustering algorithms.

#### **Movie Recommendation System**
- `movie.py`

A recommendation system for movies based on collaborative filtering or content-based methods.

#### **Sentiment Analysis**
- `sen.py`
- `cleaned_data.csv`
- `tweets.csv`

A project to perform sentiment analysis on tweets and other textual data using the TextBlob library.

#### **Stock Price Estimation**
- `f.py`

A tool to estimate and predict stock prices using historical data and the Yahoo Finance API.

---

## **Getting Started**

### **Step 1: Clone the Repository**

Clone this repository to your local machine by running the following command:

```bash
git clone https://github.com/GZ30eee/DM.git
cd DM
```

---

### **Step 2: Install Required Libraries**

These projects require several external libraries. To install them, run the following command:

```bash
pip install -r requirements.txt
```

Alternatively, you can manually install the required libraries by running:

```bash
pip install tkinter pandas mlxtend yfinance matplotlib textblob numpy scikit-learn requests beautifulsoup4
```

---

## **Running the Projects**

Each project can be executed independently. You can run the scripts in the following way:

```bash
python main.py
python ap.py
python bin.py
python clu.py
python movie.py
python sen.py
python f.py
```

For projects involving datasets like `cleaned_data.csv` or `tweets.csv`, ensure the data files are in the same directory or adjust the file paths in the code accordingly.

---

## **Contributing**

Feel free to fork this repository, make your changes, and submit a pull request. Contributions are welcome!

---

## **License**

This repository is open-source and available under the MIT License.

---
