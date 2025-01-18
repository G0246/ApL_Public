# SKlearn

from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import MinMaxScaler, PolynomialFeatures
from sklearn.metrics import mean_squared_error, r2_score
import numpy as np

# 1. 初始化資料
# 建立範例資料：X 為輸入特徵，y 為目標值
X = np.array([[1], [2], [3], [4], [5]])  # 單一特徵
y = np.array([1.5, 3.5, 6.0, 8.0, 11.5])  # 目標值

print("1. 原始資料：")
print("X =", X.flatten())
print("y =", y)

# 2. 線性迴歸：使用 sklearn.linear_model.LinearRegression
# 初始化線性迴歸模型
model = LinearRegression()

# 訓練模型：使用 fit() 方法
model.fit(X, y)

# 預測結果：使用 predict() 方法
y_pred = model.predict(X)

# 輸出模型參數
print("\n2. 線性迴歸模型：")
print(f"斜率 (係數): {model.coef_[0]}")
print(f"截距: {model.intercept_}")

# 評估模型：使用 mean_squared_error 和 r2_score
mse = mean_squared_error(y, y_pred)
r2 = r2_score(y, y_pred)
print(f"均方誤差 (MSE): {mse}")
print(f"決定係數 (R²): {r2}")

# 3. 資料縮放：使用 sklearn.preprocessing.MinMaxScaler
# 初始化 MinMaxScaler，將資料縮放到 [0, 1] 區間
scaler = MinMaxScaler()

# 對 X 進行縮放
X_scaled = scaler.fit_transform(X)

print("\n3. 資料縮放（MinMaxScaler）：")
print("縮放後的 X =", X_scaled.flatten())

# 4. 多項式特徵生成：使用 sklearn.preprocessing.PolynomialFeatures
# 初始化 PolynomialFeatures，生成二次多項式特徵
poly = PolynomialFeatures(degree=2, include_bias=False)

# 將 X_scaled 轉換為多項式特徵
X_poly = poly.fit_transform(X_scaled)

print("\n4. 多項式特徵生成：")
print("多項式特徵 (degree=2):")
print(X_poly)

# 5. 使用多項式特徵進行迴歸
# 初始化並訓練線性迴歸模型（使用多項式特徵）
model_poly = LinearRegression()
model_poly.fit(X_poly, y)

# 預測結果
y_poly_pred = model_poly.predict(X_poly)

# 輸出多項式迴歸模型參數
print("\n5. 多項式迴歸模型：")
print(f"係數: {model_poly.coef_}")
print(f"截距: {model_poly.intercept_}")

# 評估多項式模型
mse_poly = mean_squared_error(y, y_poly_pred)
r2_poly = r2_score(y, y_poly_pred)
print(f"多項式模型 - 均方誤差 (MSE): {mse_poly}")
print(f"多項式模型 - 決定係數 (R²): {r2_poly}")

# 6. 模型比較
print("\n6. 模型比較：")
print(f"線性模型 - MSE: {mse}, R²: {r2}")
print(f"多項式模型 - MSE: {mse_poly}, R²: {r2_poly}")

# 7. 預測新資料的例子
new_X = np.array([[6]])  # 新的輸入特徵
new_X_scaled = scaler.transform(new_X)  # 縮放新資料
new_X_poly = poly.transform(new_X_scaled)  # 生成多項式特徵

# 預測
new_y_pred = model_poly.predict(new_X_poly)
print("\n7. 預測新資料：")
print(f"輸入特徵: {new_X.flatten()}")
print(f"預測結果: {new_y_pred[0]}")