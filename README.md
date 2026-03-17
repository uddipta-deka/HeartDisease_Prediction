# Heart Disease Prediction

This machine learning project that trains and compares multiple classification models to predict the presence of heart disease.
The goal of this project is to evaluate different algorithms and identify the model that performs best based on common classification metrics.

## Models Implemented

* Logistic Regression
* K-Nearest Neighbors (KNN)
* Naive Bayes
* Decision Tree
* Support Vector Machine (SVM)

## Evaluation Metrics

Models were evaluated using:

* Accuracy
* F1 Score

## Results

| Model               | Accuracy | F1 Score |
| ------------------- | -------- | -------- |
| Logistic Regression | 0.8696   | 0.8857   |
| KNN                 | 0.8533   | 0.8720   |
| Naive Bayes         | 0.8533   | 0.8683   |
| Decision Tree       | 0.7717   | 0.7941   |
| SVM                 | 0.8478   | 0.8667   |

Based on these results, **Logistic Regression** performed the best among the tested models with an accuracy of approximately **87%**.

## Project Workflow

1. Data preprocessing
2. Feature scaling
3. Model training
4. Model evaluation
5. Model comparison

## Technologies Used

* Python
* pandas
* numpy
* scikit-learn
* matplotlib
* seaborn
* StreamLit


## Future Improvements

* Hyperparameter tuning
* Cross-validation
* Additional feature engineering
* Testing ensemble models
