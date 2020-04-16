import numpy as np
def multiSGD(train_data, learning_rate, n_iter, k, divideby):
    # Initially we will keep our W and B as 0 as per the Training Data
    w = np.zeros(shape=(1, train_data.shape[1] - 1))
    b = 0

    cur_iter = 1
    while (cur_iter <= n_iter):

        # We will create a small training data set of size K
        temp = train_data.sample(k)

        # We create our X and Y from the above temp dataset
        y = np.array(temp['price'])
        x = np.array(temp.drop('price', axis=1))

        # We keep our initial gradients as 0
        w_gradient = np.zeros(shape=(1, train_data.shape[1] - 1))
        b_gradient = 0

        for i in range(k):  # Calculating gradients for point in our K sized dataset
            prediction = np.dot(w, x[i]) + b
            w_gradient = w_gradient + (-2) * x[i] * (y[i] - (prediction))
            b_gradient = b_gradient + (-2) * (y[i] - (prediction))

        # Updating the weights(W) and Bias(b) with the above calculated Gradients
        w = w - learning_rate * (w_gradient / k)
        b = b - learning_rate * (b_gradient / k)

        # Incrementing the iteration value
        cur_iter = cur_iter + 1

        # Dividing the learning rate by the specified value
        learning_rate = learning_rate / divideby

    return w, b  # Returning the weights and Bias