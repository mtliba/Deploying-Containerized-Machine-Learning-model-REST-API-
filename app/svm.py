import numpy as np
from sklearn.externals import joblib
from sklearn import svm, datasets
from sklearn.cross_validation import train_test_split, cross_val_score 
from sklearn.svm import SVC

def run_models():
    iris = datasets.load_iris()

    print ("Iris data set Description : ", iris['DESCR']) 
    #Features
    X = iris.data
    #Target variable              
    y = iris.target             

    #split the data into train and test sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=10)


    # we create an instance of SVM and fit out data. We do not scale our
    # data since we want to plot the support vectors
    C = 1.0  # SVM regularization parameter
    models = (svm.SVC(kernel='linear', C=C),
            svm.LinearSVC(C=C, max_iter=10000),
            svm.SVC(kernel='rbf', gamma=0.7, C=C),
            svm.SVC(kernel='poly', degree=3, gamma='auto', C=C))
    models = (clf.fit(X_train, y_train) for clf in models)

    # title for the plots
    titles = ('SVC',
            'LinearSVC',
            'SVC-RBF',
            'SVC-Pd3')

    for clf, title in zip(models, titles):
        y_pred = clf.predict(X_test)
        #print(y_pred)
        print(title +' :'+ clf.score(X_test,y_test.ravel()))
        # save model
        joblib.dump(clf, './'+title+'.pkl', compress=True)
        
if __name__ == "__main__":
     run_models()