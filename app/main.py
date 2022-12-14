import numpy as np

x_entree = np.array(([3, 1.5], [2,1], [4, 1.5], [3,1], [3.5, 0.5], [2, 0.5], [5.5, 1], [1,1], [4, 1.5]), dtype=float) # input data
y = np.array(([1], [0], [1], [0], [1], [0], [1], [0]), dtype=float) # output data / 1 = red / 0 = blue


# Changing the scale of our values to be between 0 and 1
x_entree = x_entree/np.amax(x_entree, axis=0) # Each input is divided by the maximum value of the inputs


# We get back what we want
X = np.split(x_entree, [8])[0] # Data on which we will train, the first 8 of our matrix
xPrediction = np.split(x_entree, [8])[1] # Value we want to find

# Our neural network class
class Neural_Network(object):
    def __init__(self):

        # Our Settings
        self.inputSize = 2 # Number of neurons to enter
        self.outputSize = 1 # Number of output neurons
        self.hiddenSize = 3 # Number of hidden neurons

        # Our weights
        self.W1 = np.random.randn(self.inputSize, self.hiddenSize) # (2x3) Weight matrix between input and hidden neurons
        self.W2 = np.random.randn(self.hiddenSize, self.outputSize) # (3x1) Weight matrix between input and hidden neurons

    # Forward propagation function
    def forward(self, X):
        self.z = np.dot(X, self.W1) # Matrix multiplication between the input values and the weights W1
        self.z2 = self.sigmoid(self.z) # Application of the activation function (Sigmoid)
        self.z3 = np.dot(self.z2, self.W2) # Matrix multiplication between hidden values and W2 weights
        o = self.sigmoid(self.z3) # Applying the activation function, and obtaining our final output value
        return o

    # Activation function
    def sigmoid(self, s):
        return 1/(1+np.exp(-s))
        
    # Derivative of the activation function
    def sigmoidPrime(self, s):
        return s*(1-s)

    # Backpropagation function
    def backward(self, X, y, o):
        self.o_error = y - o # Error calculation
        self.o_delta = self.o_error * self.sigmoidPrime(o) # Application of the derivative of the sigmoid to this error

        self.z2_error = self.o_delta.dot(self.W2.T) # Calculating the error of our hidden neurons 
        self.z2_delta = self.z2_error * self.sigmoidPrime(self.z2) # Application of the derivative of the sigmoid to this error

        self.W1 += X.T.dot(self.z2_delta) # We adjust our weights W1
        self.W2 += self.z2.T.dot(self.o_delta) # We adjust our weights W2

    # Training function
    def train(self, X, y):
        o = self.forward(X)
        self.backward(X,y,o)


    # Predictive function
    def predict(self):
        print("Predicted data after training : ")
        print("Input : \n" + str(xPrediction))
        print("Output : \n" + str(self.forward(xPrediction)))

        if(self.forward(xPrediction) < 0.5):
            print("The flower is BLUE ! \n")
        else:
            print("The flower is RED ! \n")


NN = Neural_Network()

for i in range(10000): #Choose a number of iterations, be careful, too many can create overfitting!
    print("# " + str(i) + "\n")
    print("Input values : \n" + str(X))
    print("Current output : \n" + str(y))
    print("AI-predicted output : \n" + str(np.matrix.round(NN.forward(X), 2)))
    print("\n")
    NN.train(X,y)

NN.predict()