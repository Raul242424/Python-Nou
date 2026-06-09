import tensorflow as tf
import matplotlib.pyplot as plt
import numpy as np

mnist = tf.keras.datasets.mnist
(x_train, y_train), (x_test, y_test) = mnist.load_data()

x_train = x_train / 255.0
x_test = x_test / 255.0

print("Forma datelor de antrenament:", x_train.shape)

model = tf.keras.models.Sequential([
    tf.keras.layers.Flatten(input_shape=(28, 28)),
    tf.keras.layers.Dense(128, activation='relu'),
    tf.keras.layers.Dense(10, activation='softmax')
])

model.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])

print("\n--- Începe antrenarea modelului ---")

model.fit(x_train, y_train, epochs=5)

print("\n--- Evaluarea pe setul de test ---")
test_loss, test_acc = model.evaluate(x_test, y_test, verbose=2)
print(f"Acuratețea pe setul de test: {test_acc * 100:.2f}%")

predictii = model.predict(x_test)


index_imagine = 0
clasa_prezisa = np.argmax(predictii[index_imagine])
clasa_reala = y_test[index_imagine]

plt.imshow(x_test[index_imagine], cmap='gray')
plt.title(f"Predicție model: {clasa_prezisa} | Valoare reală: {clasa_reala}")
plt.axis('off')
plt.show()