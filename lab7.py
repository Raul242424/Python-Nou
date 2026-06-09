import pandas as pd
import matplotlib.pyplot as plt
from sklearn.datasets import load_diabetes
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

diabetes = load_diabetes()
df = pd.DataFrame(diabetes.data, columns=diabetes.feature_names)
df['target'] = diabetes.target

print(df.head())

print("\n3. Caracteristici disponibile:")
print(diabetes.feature_names)

print("\n4. Statistici descriptive:")
print(df.describe())

plt.figure(figsize=(8, 5))
plt.hist(df['bmi'], bins=20, color='skyblue', edgecolor='black')
plt.title('Distribuția BMI (Normalizat)')
plt.xlabel('Valoare BMI')
plt.ylabel('Frecvență')
plt.show()

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))

ax1.scatter(df['bmi'], df['target'], color='blue', alpha=0.5)
ax1.set_title('BMI vs Progresia Bolii')
ax1.set_xlabel('BMI')
ax1.set_ylabel('Target')

ax2.scatter(df['age'], df['target'], color='green', alpha=0.5)
ax2.set_title('Vârstă vs Progresia Bolii')
ax2.set_xlabel('Age')
ax2.set_ylabel('Target')

plt.tight_layout()
plt.show()

X = df[['bmi']]
y = df['target']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model_simplu = LinearRegression()
model_simplu.fit(X_train, y_train)

y_pred = model_simplu.predict(X_test)

plt.figure(figsize=(8, 5))
plt.scatter(X_test, y_test, color='black', label='Date reale')
plt.plot(X_test, y_pred, color='red', linewidth=3, label='Linia de regresie')
plt.title('Regresie Liniara: BMI vs Target')
plt.legend()
plt.show()

mse = mean_squared_error(y_test, y_pred)
print(f"MSE: {mse:.2f}")

X_multi = df[['bmi', 'bp']]
y_multi = df['target']

X_train_m, X_test_m, y_train_m, y_test_m = train_test_split(X_multi, y_multi, test_size=0.2, random_state=42)

model_multi = LinearRegression()
model_multi.fit(X_train_m, y_train_m)

print(f"Coeficient BMI: {model_multi.coef_[0]:.2f}")
print(f"Coeficient BP: {model_multi.coef_[1]:.2f}")

y_pred_m = model_multi.predict(X_test_m)
r2 = r2_score(y_test_m, y_pred_m)
print(f"Scorul R2: {r2:.4f}")