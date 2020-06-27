import tensorflow as tf
from tensorflow.keras import Model
from tensorflow.keras.layers import BatchNormalization, Conv2D, Input
from tensorflow.keras.layers import ZeroPadding2D, LeakyReLU, UpSampling2D


# Reading and parse the cfg file
def parse_cfg(cfgfile):

    with open(cfgfile, 'r') as file:
        lines = [line.rstrip('\n') for line in file if line != '\n' and line[0] != '#']

    # It holds the full network
    networkBlock = []
    # It holds each layer of the network
    netBlocks = {}

    for line in lines:
        if line[0] == '[':
            line = 'type='+line[1:-1].rstrip()
            if len(netBlocks) != 0:
                networkBlock.append(netBlocks)
                netBlocks = {}
            
        key, value = line.split('=')
        netBlocks[key.rstrip()] = value.lstrip()
        
    networkBlock.append(netBlocks)

    return networkBlock

'''
construct = parse_cfg('cfg/yolov3.cfg')
print(construct,"/n constructed from cfg file")
'''