import pandas as pd
import numpy as np
from sklearn.feature_extraction import DictVectorizer
from xgboost import XGBRegressor
import pickle

def load_data() -> pd.DataFrame:
    """
        Read in the training data into a pandas dataFrame
        Args:
            None

        return:
            df: pandas.DataFrame: A table of the training dataset

    """
    df = pd.read_csv('train.csv')
    return df

def data_preprocessing(df:pd.DataFrame):
    """
    This help to preprocessing the data and carry out features engineering

    Args:
        df: pandas.DataFrame: A table of the training dataset
    
    return:
        X_train: Preprocessed features
        y_train: Preprocessed target variables
        dv: Dictionary vectorizer for one encoding
    """

    train_columns = ['LotArea', 'OverallQual', 'YearBuilt', 'YearRemodAdd', 'MasVnrArea', 'BsmtFinSF1', 'BsmtUnfSF', 'TotalBsmtSF', 
            '1stFlrSF', '2ndFlrSF', 'GrLivArea', 'BsmtFullBath', 'FullBath', 'HalfBath', 'BedroomAbvGr', 'TotRmsAbvGrd', 
            'Fireplaces', 'GarageYrBlt', 'GarageCars', 'GarageArea', 'WoodDeckSF', 'OpenPorchSF', 'MSZoning', 'LotShape', 
            'LandContour', 'LotConfig', 'LandSlope', 'Neighborhood', 'Condition1', 'BldgType', 'HouseStyle', 'RoofStyle', 
            'Exterior1st', 'Exterior2nd', 'MasVnrType', 'ExterQual', 'ExterCond', 'Foundation', 'BsmtQual', 'BsmtCond', 
            'BsmtExposure', 'BsmtFinType1', 'BsmtFinType2', 'HeatingQC', 'Electrical', 'KitchenQual', 'Functional', 
            'GarageType', 'GarageFinish', 'GarageQual', 'PavedDrive', 'SaleType', 'SaleCondition', 'SalePrice']

    df = df[train_columns]

    numerical_columns = df.columns[df.dtypes != 'object']


    df[numerical_columns] = df[numerical_columns].fillna(0)

    df.dropna(inplace=True)

    df['age'] = 2023 - df['YearBuilt']

    y_train = np.log1p(df.SalePrice)

    df.drop('SalePrice', inplace=True, axis=1)

    train_dict = df.to_dict(orient='records')

    dv = DictVectorizer()

    X_train = dv.fit_transform(train_dict)

    return X_train, y_train, dv

def model_training(X_train, y_train): 
    """
    Train the model on the training dataset

    Args:
        X_train: Preprocessed features
        y_train: Preprocessed target variables
    
    Return:
        model: Trained XGB model
    """
    model = XGBRegressor(learning_rate=0.05, max_depth=4, n_estimators=300, nthread=6, seed=42)
    model.fit(X_train, y_train)
    return model

def save_model(model, dv):
    """
        Save the model and other dependances to a bin file

        Args:
            model: Trained XGB model
            dv: Dictionary vectorizer for one encoding
        return:
            None

    """
    pred_columns = ['LotArea', 'OverallQual', 'YearBuilt', 'YearRemodAdd', 'MasVnrArea', 'BsmtFinSF1', 'BsmtUnfSF', 'TotalBsmtSF', 
            '1stFlrSF', '2ndFlrSF', 'GrLivArea', 'BsmtFullBath', 'FullBath', 'HalfBath', 'BedroomAbvGr', 'TotRmsAbvGrd', 
            'Fireplaces', 'GarageYrBlt', 'GarageCars', 'GarageArea', 'WoodDeckSF', 'OpenPorchSF', 'MSZoning', 'LotShape', 
            'LandContour', 'LotConfig', 'LandSlope', 'Neighborhood', 'Condition1', 'BldgType', 'HouseStyle', 'RoofStyle', 
            'Exterior1st', 'Exterior2nd', 'MasVnrType', 'ExterQual', 'ExterCond', 'Foundation', 'BsmtQual', 'BsmtCond', 
            'BsmtExposure', 'BsmtFinType1', 'BsmtFinType2', 'HeatingQC', 'Electrical', 'KitchenQual', 'Functional', 
            'GarageType', 'GarageFinish', 'GarageQual', 'PavedDrive', 'SaleType', 'SaleCondition']

    output_file = 'model_V1.0.bin'
    with open(output_file, 'wb') as f_out:
        pickle.dump((model, dv, pred_columns), f_out)

def main():
    """
    Main function for training the model
    """
    print('----------------------------Training Started----------------------------')
    df = load_data()
    print('Data preprocessing')
    X_train, y_train, dv = data_preprocessing(df)
    model = model_training(X_train, y_train)
    save_model(model, dv)
    print('---------------------------Saved Trained Model----------------------------')

if __name__ == '__main__':
    main()