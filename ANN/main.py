from numpy import exp, array, random, dot, rint

class NeuronLayer():
    def __init__(self, number_of_neurons, number_of_inputs_per_neuron):
        self.synaptic_weights = 2 * random.random((number_of_inputs_per_neuron, number_of_neurons)) - 1

class NeuralNetwork():
    def __init__(self, layer1, layer2, learningRate):
        self.layer1 = layer1
        self.layer2 = layer2
        self.learningRate = learningRate

    def __sigmoid(self, x):
        return 1 / (1 + exp(-x))

    def __sigmoid_derivative(self,x):
        return x*(1-x)

    def think(self, inputs):
        output_from_layer1 = self.__sigmoid(dot(inputs, self.layer1.synaptic_weights))
        output_from_layer2 = self.__sigmoid(dot(output_from_layer1, self.layer2.synaptic_weights))
        return output_from_layer1, output_from_layer2

    def cosFxn(self, t, a):
        pass
    
    def train(self, traing_set_inputs, traing_set_outputs, number_of_training_iterations):
        for iteration in range(number_of_training_iterations):
            output_from_layer_1, output_from_layer_2 = self.think(training_set_inputs)

            layer2_error = training_set_outputs - output_from_layer_2
            layer2_delta = layer2_error * self.__sigmoid_derivative(output_from_layer_2)

            layer1_error = layer2_delta.dot(self.layer2.synaptic_weights.T)
            layer1_delta = layer1_error * self.__sigmoid_derivative(output_from_layer_1)

            layer1_adjustment = training_set_inputs.T.dot(layer1_delta)
            layer2_adjustment = output_from_layer_1.T.dot(layer2_delta)

            self.layer1.synaptic_weights += layer1_adjustment
            self.layer2.synaptic_weights += layer2_adjustment

    def print_weights(self):
        print ("    Layer 1 (4 neurons, each with 2 inputs): ")
        print (self.layer1.synaptic_weights)
        print ("    Layer 2 (1 neuron, with 4 inputs):")
        print (self.layer2.synaptic_weights)


if __name__ == "__main__":

    layer1 = NeuronLayer(10,2)

    layer2 = NeuronLayer(1,10)

    learningRate = 1

    neural_network = NeuralNetwork(layer1, layer2, learningRate)


    training_set_inputs = array([[0, 0], [1, 1], [1, 0], [0, 1]])
    training_set_outputs = array([[0, 1, 0, 0]]).T

    neural_network.train(training_set_inputs, training_set_outputs, 60000)

    hidden_state, output = neural_network.think(array([[0, 0], [1, 1], [1, 0], [0, 1]]))
    print(rint(output))



