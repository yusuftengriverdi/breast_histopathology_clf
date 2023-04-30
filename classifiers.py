from tools import read_images, binary_paths
from classifiers.stack import prepare_data
import classifiers.metrics as m

# TODO: Try with MNIST
# You can try to list parameters of classifier here.
params = {"l1_regularization": 0.1}
def eval_classifiers(train_X, train_y, test_X, test_y):
    """Pseudo -code. Do not RUN yet."""
    # Example classifiers: https://scikit-learn.org/stable/auto_examples/classification/plot_classifier_comparison.html 
    clfs = []
    preds = []
    for clf in clfs:
        train_yhat = clf.fit(train_X)
        preds.append(train_yhat)
        # You can apply CV.
        test_yhat = clf.predict(test_y)

    train_performance = m.auc(train_y, train_yhat)
    test_performance = m.auc(test_y, test_yhat)
    return  train_performance, test_performance

if __name__ == "__main__":
    # Use here to test MNIST or other dataset.
    pass