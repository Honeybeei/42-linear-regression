# 🚀 FT Linear Regression

- [🚀 FT Linear Regression](#-ft-linear-regression)
  - [📘 Introduction](#-introduction)
  - [🎯 Goal of the Project](#-goal-of-the-project)
  - [📈 Linear Regression](#-linear-regression)
    - [❓ What is it?](#-what-is-it)
    - [📏 Linear Regression Equation](#-linear-regression-equation)
  - [⚖️ Cost Function (Loss Function)](#️-cost-function-loss-function)
  - [🔍 Gradient of the Cost Function](#-gradient-of-the-cost-function)
  - [🏄 Gradient Descent](#-gradient-descent)
    - [🔢 Step 1: Initialize the Parameters](#-step-1-initialize-the-parameters)
    - [📉 Step 2: Compute the Gradients of the Cost Function](#-step-2-compute-the-gradients-of-the-cost-function)
    - [🔄 Step 3: Update the Parameters](#-step-3-update-the-parameters)
    - [🔁 Step 4: Repeat](#-step-4-repeat)
    - [🔮 Step 5: Predict](#-step-5-predict)
  - [🤩 Features I added](#-features-i-added)
    - [📝 Continuous theta logging and updating](#-continuous-theta-logging-and-updating)
    - [📉 Learning rate decay when overshooting](#-learning-rate-decay-when-overshooting)
    - [⚙️ Optimization at the beginning](#️-optimization-at-the-beginning)
    - [🦾 Theta0 Acceleration](#-theta0-acceleration)

## 📘 Introduction

This subject is about implementing a linear regression model from scratch.

## 🎯 Goal of the Project

- Train a **linear regression** model using the **gradient descent** algorithm
- Predict the price of a car using its **mileage** as the single input feature

## 📈 Linear Regression

### ❓ What is it?

Linear Regression is a supervised machine learning algorithm used to model the relationship between one or more independent variables (input features) and a continuous dependent variable (the value we are trying to predict).

Goal:

- Find a straight line (or a hyperplane in higher dimensions) that **best fits** the data points.
- This "best fit" line should minimize the difference between the predicted values and the actual values.

Key Terms:

- **Independent Variable**: The input feature(s) used to predict the dependent variable (in this case, the **mileage** of a car)
- **Dependent Variable**: The value we are trying to predict (in this case, the price of a car)
- **Parameters**: The coefficients and the intercept that define the line

### 📏 Linear Regression Equation

For a single input feature, the equation is:

$$\hat{y} = wx + b$$

Where:

- $\hat{y}$ is **Predicted** Value (dependent variable).
- $x$ is the **Input** Feature (independent variable)
- $w$ is the **Slope** of the line (weight or coefficient)
- $b$ is the **Intercept** of the line (bias)

The goal of linear regression is to find the optimal values for the parameters $w$ and $b$ that **best fit** the data. And this process is called **training** the model.

## ⚖️ Cost Function (Loss Function)

The cost function is used to measure how well the model fits the data. It measures **how far off** the predicted values are from the actual values.

The cost function for linear regression is the **Mean Squared Error (MSE)**:

$$
MSE(w,b) = \frac{1}{n} \sum_{i=1}^{n} \left(\hat{y}^{(i)} - y^{(i)}\right)^2 = \frac{1}{n} \sum_{i=1}^{n} \left(wx_i + b - y_i\right)^2
$$

Where:

- $n$ is the number of data points
- $y_i$ is the actual value for the i-th data point
- $\hat{y}_i$ is the predicted value for the i-th data point

The Goal is to **minimize** the MSE by finding the optimal values for the parameters $w$ and $b$.

## 🔍 Gradient of the Cost Function

Our main goal is to find the optimal values for the parameters $w$ and $b$ that minimize the cost function. Right? To minimize the cost function, we need figure out how to **update** the parameters $w$ and $b$. This is where the **gradient** comes in.

A **gradient** tells us "which direction to move the parameters from their current position to reduce the loss."

Cost function is a function of $w$ and $b$. So, we can use **partial derivatives** with respect to $w$ and $b$ to find the minimum value of the cost function.

$$
\frac{\partial MSE}{\partial w} = \frac{2}{n} \sum_{i=1}^{n} x_i(wx_i + b - y_i)
$$

$$
\frac{\partial MSE}{\partial b} = \frac{2}{n} \sum_{i=1}^{n} (wx_i + b - y_i)
$$

Okay, we have the partial derivatives. But, what does this actually mean?

**Partial Derivative with respect to $w$**: We can determine how much the cost function will change if we change the value of $w$ by a very small amount. If the derivative is **positive**, the cost function will **increase**. Therefore, we need to **decrease** the value of $w$. If the derivative is **negative**, the cost function will **decrease**. Therefore, we need to **increase** the value of $w$.

And the same thing applies to the partial derivative with respect to $b$.

This is the **key** to the gradient descent algorithm.

## 🏄 Gradient Descent

Gradient Descent is an optimization algorithm used to minimize the cost function by **iteratively moving** in the direction of **steepest descent**.

The algorithm is as follows:

### 🔢 Step 1: Initialize the Parameters

Initialize the parameters $w$ and $b$ with random values(or zeros). These are the values that will be **updated** during the training process.

### 📉 Step 2: Compute the Gradients of the Cost Function

Compute the partial derivatives of the cost function with respect to the parameters $w$ and $b$.

### 🔄 Step 3: Update the Parameters

Now, we have the gradients, which tell us the direction to move the parameters to reduce the cost function. But, how much do we move the parameters? This is determined by the **learning rate** $\alpha$.

- If the learning rate is **too small**, the model will take a **long time** to converge.
- If the learning rate is **too large**, the model may **overshoot** the minimum and **fail** to converge.

The update rule is:

$$
w := w - \alpha \frac{\partial MSE}{\partial w}, \quad b := b - \alpha \frac{\partial MSE}{\partial b}
$$

Why subtract the gradient? Because we want to **minimize** the cost function. If the gradient is **positive**, increasing \(w\) or \(b\) further will increase the cost function, so we do the opposite. Conversely, if it's **negative**, we move in the positive direction.

### 🔁 Step 4: Repeat

We just took a small step in the direction that reduces the cost function. Now, we repeat the process until the cost function converges to a minimum value.

### 🔮 Step 5: Predict

After training the model, we can use it to make predictions on new data points.

## 🤩 Features I added

### 📝 Continuous theta logging and updating

While updating the parameters, after `CoreConstants.ITERATIONS` iterations, the theta values will be updated in the `data/theta.csv` file. The updated theta value will be used for the next iteration.

### 📉 Learning rate decay when overshooting

If the cost function **increases** after updating the parameters, it means we overshot the minimum (the learning rate was too high). In this case, the learning rate will be decreased by `CoreConstants.LEARNING_RATE_DECAY_FACTOR`. The `data/theta.csv` file will be wiped out, and the training process will start from scratch.

### ⚙️ Optimization at the beginning

Usually, the initial weights (thetas) are set to zero, as the project document states. However, starting at zero can take a long time to converge. To speed things up, I added a feature that initializes the weights by drawing a line between the **first** and the **last** data points. This often leads to faster convergence.

### 🦾 Theta0 Acceleration

While updating the parameters, the theta0 (which corresponds to the intercept \(b\)) will be updated by `CoreConstants.THETA0_ACCELERATION_FACTOR` times the gradient of the cost function. This helps speed up the convergence process and can reduce the final cost value.
