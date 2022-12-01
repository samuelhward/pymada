import pymada.ai.neural_net.net
import pymada.ai.neural_net.layer


def test_add_layer():

    net = pymada.ai.neural_net.net.Net()
    layer = pymada.ai.neural_net.layer.Layer(10)
    net.add_layer(layer)
    net.add_layer(layer)

    assert net.number_layers == 2
    assert net.layer[0].neuron[0].activation == 0
