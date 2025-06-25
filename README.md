# 🏡 House Price Prediction

This project aims to predict house prices using a linear regression model trained on a selected subset of features from the Ames Housing dataset. It uses clean machine learning practices including preprocessing pipelines and evaluation via cross-validation.

---

## 📌 Project Summary

- 🎯 **Goal**: Predict `SalePrice` of houses using features like `GrLivArea`, `BedroomAbvGr`, and `FullBath`.
- 🧠 **Model**: Linear Regression
- ⚙️ **Tools Used**: `scikit-learn`, `pandas`, `numpy`, `PowerTransformer`, `StandardScaler`, `Pipeline`, `ColumnTransformer`

---

## 📁 Dataset

- `train.csv`: Training data with features and target `SalePrice`
- `test.csv`: Testing data used for predictions
- Features used:
  - `GrLivArea` (Above ground living area in square feet)
  - `BedroomAbvGr` (Number of bedrooms above ground)
  - `FullBath` (Number of full bathrooms)

---

## 🔧 Workflow

### ✅ 1. Preprocessing
- Applied `PowerTransformer` (Yeo-Johnson) to normalize skewed data
- Scaled features using `StandardScaler`
- Combined steps using `ColumnTransformer` and `Pipeline`

### ✅ 2. Modeling
- Built a regression pipeline using `LinearRegression`
- Evaluated performance using:
  - **Mean Squared Error (MSE)**
  - **R² Score**

### ✅ 3. Cross-Validation
- Performed 10-fold cross-validation using `cross_val_score`
- Averaged scores for robust model evaluation

### ✅ 4. Output
- Generated predictions on test data
- Preserved original `Id` from input dataset
- Created a final DataFrame with:
  - `Id`
  - `Predicted` sale price
- Exported as `test_output.csv`

---

## 🚀 How to Run

1. Clone the repo:
```bash
git clone https://github.com/yourusername/house-price-prediction.git
cd house-price-prediction
```
2. Install requirements:
```bash
pip install -r requirements.txt
Run the Jupyter notebook:
```
3. Run the jupyter notebook:
```bash
jupyter notebook
```

## 📦 Dataset Source

This project uses data from the **Kaggle House Prices - Advanced Regression Techniques** competition.

📥 [View Dataset on Kaggle](https://www.kaggle.com/c/house-prices-advanced-regression-techniques/data)

---

## 📬 Contact
Created with ❤️ by Swarnabha Ghosh  
Feel free to reach out or contribute!  
Email: [swarnabha983@gmail.com](mailto:swarnabha983@gmail.com)
