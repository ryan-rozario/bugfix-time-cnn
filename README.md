# bugfix-time-cnn
Use a character level cnn to predict the time to fix bug based on the different states during the life cycle of a bug.

## Construct Model

We use the char_cnn_zhang model from this paper:

- Xiang Zhang, Junbo Zhao, Yann LeCun. [Character-level Convolutional Networks for Text Classification](http://arxiv.org/abs/1509.01626). NIPS 2015

The model structure:

![](https://cdn-images-1.medium.com/max/1600/0*fovAEUSdSkbsnJw5.png)

This graph may look difficult to understand. Here is the model setup. 


![](https://img-blog.csdn.net/20170721104727009)

We choose the small frame, 256 filters in convolutional layer and 1024 output units in dense layer. 

- Embedding Layer
- Six convolutional layers, and 3 convolutional layers followed by a max pooling layer
- Two fully connected layer(dense layer in keras), neuron units are 1024. 
- Output layer(dense layer), neuron units depends on classes. In this task, we set it 2. 
