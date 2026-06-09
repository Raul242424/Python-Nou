import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report

print("--- 1. Explorarea setului de date ---")
iris = load_iris()
X = iris.data
y = iris.target

print(f"Numarul de exemple si dimensiunea caracteristicilor (shape): {X.shape}")
print(f"Denumirile coloanelor (atributelor): {iris.feature_names}")
print(f"Numele claselor: {iris.target_names}\n")

print("--- 2. Impartirea setului ---")
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

print(f"Forma datelor de antrenament: X_train={X_train.shape}, y_train={y_train.shape}")
print(f"Forma datelor de testare: X_test={X_test.shape}, y_test={y_test.shape}\n")

print("--- 3. Preprocesarea datelor ---")
scaler = StandardScaler()

print("Primele 3 exemple INAINTE de scalare:")
print(X_train[:3])

X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

print("\nPrimele 3 exemple DUPA scalare:")
print(X_train_scaled[:3], "\n")

print("--- 4. Construirea si antrenarea modelului KNN ---")
knn = KNeighborsClassifier(n_neighbors=5)
knn.fit(X_train_scaled, y_train)

y_pred = knn.predict(X_test_scaled)
accuracy = accuracy_score(y_test, y_pred)
print(f"Acuratetea modelului cu k=5 pe setul de testare este: {accuracy * 100:.2f}%\n")

print("--- 5. Explorarea impactului valorii k ---")
k_values = range(1, 16)
accuracies = []

for k in k_values:
    temp_knn = KNeighborsClassifier(n_neighbors=k)
    temp_knn.fit(X_train_scaled, y_train)
    temp_pred = temp_knn.predict(X_test_scaled)
    accuracies.append(accuracy_score(y_test, temp_pred))

plt.figure(figsize=(8, 5))
plt.plot(k_values, accuracies, marker='o', linestyle='dashed', color='b')
plt.title('Acuratetea modelului in functie de valoarea lui k!')
plt.xlabel('Valoarea lui k')
plt.ylabel('Acuratete')
plt.xticks(k_values)
plt.grid(True)
plt.show()

print("--- 6. Evaluarea modelului (pentru k=5) ---")
print("Matricea de confuzie:")
print(confusion_matrix(y_test, y_pred))

print("\nRaportul de clasificare:")
print(classification_report(y_test, y_pred, target_names=iris.target_names))

print("--- 7. Vizualizarea datelor si predictie noua ---")

plt.figure(figsize=(8, 5))
scatter = plt.scatter(X[:, 2], X[:, 3], c=y, cmap='viridis', edgecolor='k')
plt.title('Distributia florilor Iris (Lungime vs Latime Petala)')
plt.xlabel('Lungime Petala (cm)')
plt.ylabel('Latime Petala (cm)')
plt.legend(handles=scatter.legend_elements()[0], labels=list(iris.target_names))
plt.show()

print("\n--- Introdu datele pentru o floare noua ---")
try:
    sl = float(input("Lungimea sepalei (cm): "))
    sw = float(input("Latimea sepalei (cm): "))
    pl = float(input("Lungimea petalei (cm): "))
    pw = float(input("Latimea petalei (cm): "))

    new_flower = np.array([[sl, sw, pl, pw]])
    new_flower_scaled = scaler.transform(new_flower)

    predicted_class_index = knn.predict(new_flower_scaled)[0]
    predicted_class_name = iris.target_names[predicted_class_index]

    print(f"\n=> Modelul a prezis ca floarea introdusa apartine speciei: **{predicted_class_name}**")
except ValueError:
    print("Te rog sa introduci doar numere valide!")