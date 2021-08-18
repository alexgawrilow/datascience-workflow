import pandas as pd
from sklearn.base import BaseEstimator, TransformerMixin

"""
This file contains a collection of scikit-learn transformers whose `transform` or
`fit_transform` method returns a pandas DataFrame in contrast to a numpy array.
Returning a DataFrame allows to further proceed in a pipeline that uses the column
information which is lost when a numpy array is returned.
"""


class BaseFitTransformer:
    """
    Base class that has a fit method that returns self
    """

    def fit(self, X, y=None, **fit_params):
        return self


class DropColumns(BaseEstimator, TransformerMixin, BaseFitTransformer):
    """
    DataFrame transformer that provides dropping of columns.
    """

    def __init__(self, columns):
        self.columns = columns

    def transform(self, X, **transform_params):
        """
        Drops columns of a DataFrame
        """
        return X.drop(self.columns, axis=1)


class ApplyFunction(BaseEstimator, TransformerMixin, BaseFitTransformer):
    """
    DataFrame transformer that applies a function to its columns.
    """

    def __init__(self, columns, func):
        self.columns = columns
        self.func = func

    def transform(self, X, **transform_params):
        """
        Applies function to the columns of a DataFrame
        """
        return pd.DataFrame(X).apply(
            lambda x: self.func(x) if x.name in self.columns else x
        )
