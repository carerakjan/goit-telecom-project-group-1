from web.utils.scale_data import scale,prepare_data
from web.utils.load_model import get_model, get_model_name
import numpy as np

def sigmoid(x):
    return 1 / (1 + np.exp(-x))

def get_predict(data):
    model = get_model(get_model_name())
    model_name = get_model_name()
    
    # Словник з відповідними методами для кожної моделі
    method_map = {
        "decision_tree.pkl": lambda: model.predict_proba(scale(prepare_data(data)))[:, 1],
        "logistic_regression_model.pkl": lambda: model.predict_proba(scale(prepare_data(data)))[:, 1],
        "svm_model_linear.pkl": lambda: sigmoid(model.decision_function(scale(prepare_data(data)))),
        "neural_model_MLP.pkl": lambda: model.predict_proba(scale(prepare_data(data)))[:, 1],
        "svm_model_sigmoid.pkl": lambda: sigmoid(model.decision_function(scale(prepare_data(data)))),
        "svm_model_poly.pkl": lambda: sigmoid(model.decision_function(scale(prepare_data(data)))),
        "svm_model_rbf.pkl": lambda: sigmoid(model.decision_function(scale(prepare_data(data)))),
    }
    
    if model_name not in method_map:
        raise ValueError(f"Непідтримувана модель: {model_name}")
    
    return method_map[model_name]()