#necessary libraries:
import pickle
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, confusion_matrix
import numpy as np

#Load the hand landmark data from the pickle file:
data_dict = pickle.load(open('./data.pickle', 'rb'))
data = np.asarray(data_dict['data'])
#data = np.asarray(data_dict['data'], dtype=object)

labels = np.asarray(data_dict['labels'])

#Split the data into training and testing sets:
x_train, x_test, y_train, y_test = train_test_split(data, labels, test_size=0.2, shuffle=True, stratify=labels)

#Initialize and train the Random Forest classifier:
model = RandomForestClassifier()
model.fit(x_train, y_train)

#Make predictions using the trained model:
y_predict = model.predict(x_test)

# Print confusion matrix
conf_matrix = confusion_matrix(y_test, y_predict)
print('Confusion Matrix:')
print(conf_matrix)

#Calculate the accuracy of the model:
score = accuracy_score(y_predict, y_test)
precision = precision_score(y_test, y_predict, average='weighted')
recall = recall_score(y_test, y_predict, average='weighted')
f1 = f1_score(y_test, y_predict, average='weighted')
print('{}% of samples were classified correctly !'.format(score * 100))
print('Precision:', precision)
print('Recall:', recall)
print('F1-score:', f1)

#Save the trained model to a file:
f = open('model.p', 'wb')
pickle.dump({'model': model}, f)
f.close()
