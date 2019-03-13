'''
* Add attributes
  * `tensor.T` to transpose
  * `variable.T` to transpose
* Add methods
  * `tensor.reshape` as `tf.reshape(self, new_shape)`
  * `tensor.cast` to `tf.cast(self, new_dtype)`
  * `tensor.to_vector` to transfor the matrices as vectors
'''

import tensorflow as tf


tf.Tensor.T = property(lambda self: tf.transpose(self))
tf.Variable.T = property(lambda self: tf.transpose(self))

tf.Tensor.reshape = lambda self, shape: tf.reshape(self, shape=shape)
tf.Tensor.cast = lambda self, dtype: tf.cast(self, dtype=dtype)
tf.Tensor.to_vector = lambda self: self.reshape(shape=(-1, 1))
