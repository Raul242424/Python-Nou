import pandas as pd
import matplotlib.pyplot as plt
from sklearn.datasets import load_wine
from sklearn.tree import DecisionTreeClassifier, plot_tree
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

wine = load_wine(as_frame=True)
df = wine.frame
X = wine.data
y = wine.target

print("--- Exercițiul 2: Primele 5 rânduri ---")
print(df.head())
print("\n")

print("--- Exercițiul 3: Caracteristici disponibile ---")
print(wine.feature_names)
print("\n")


X_subset = df[['alcohol', 'flavanoids']]

clf_limitat = DecisionTreeClassifier(max_depth=2, random_state=42)
clf_limitat.fit(X_subset, y)


plt.figure(figsize=(10, 6))
plot_tree(clf_limitat,
          feature_names=['alcohol', 'flavanoids'],
          class_names=wine.target_names,
          filled=True,
          rounded=True)
plt.title("Arbore de Decizie (max_depth=2, doar alcohol și flavanoids)")
plt.show()

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

clf_complet = DecisionTreeClassifier(max_depth=None, random_state=42)
clf_complet.fit(X_train, y_train)

y_pred = clf_complet.predict(X_test)
acuratete = accuracy_score(y_test, y_pred)
print(f"--- Exercițiul 5: Acuratețea arborelui complet ---")
print(f"Acuratețea pe setul de testare este: {acuratete * 100:.2f}%\n")

print("--- Exercițiul 6: Importanța caracteristicilor ---")
importante = clf_complet.feature_importances_

for nume, imp in zip(wine.feature_names, importante):
    if imp > 0:
        print(f"{nume}: {imp:.4f}")