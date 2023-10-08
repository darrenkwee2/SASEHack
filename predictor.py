import tensorflow as tf
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split

data = pd.read_csv('MOCK_DATA.csv')
X = data[['social_energy', 'physical_energy', 'creative_energy', 'nervous_energy', 'cognitive_energy']].values
y = data['activity'].values

y = y - 1
y_one_hot = tf.keras.utils.to_categorical(y, num_classes=30)

X_train, X_test, y_train, y_test = train_test_split(X, y_one_hot, test_size=0.2, random_state=42)

# Define the softmax regression model
model = tf.keras.Sequential([
    tf.keras.layers.Dense(30, activation='softmax', input_shape=(5,))
])

# Compile the model
model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])

# Train the model
model.fit(X_train, y_train, epochs=50, batch_size=32, validation_data=(X_test, y_test))

# Make predictions
predictions = model.predict(X_test)

# Convert predictions to labels (1-6)
predicted_labels = np.argmax(predictions, axis=1) + 1

# Print predicted labels
# print(predicted_labels)

# Answer responses are 1, 2, 3, -3, 3 --> -3 is lowest energy, 0 is normal, 3 is highest energy
social_energy = int(input("How much social energy do you have? "))
physical_energy = int(input("How much physical energy do you have? "))
creative_energy = int(input("How much creative energy do you have? "))
nervous_energy = int(input("How much nervous energy do you have? "))
cognitive_energy = int(input("How much cognitive energy do you have? "))

print(f"Activity recommendation: ", np.argmax(model.predict([[social_energy, physical_energy, creative_energy, nervous_energy, cognitive_energy]]), axis=1) + 1)






