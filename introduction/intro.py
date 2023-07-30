import tensorflow as tf  # now import the tensorflow module
print(tf.test.is_gpu_available())  # make sure you have GPU support
print(tf.version.VERSION) #this will print the version of tensorflow you are using

#create a string tensor
string = tf.Variable("this is a string tensor", tf.string)
print(string)
#this will print the string tensor

#create a number tensor
number = tf.Variable(324, tf.int16)
print(number)
#this will print the number tensor

#create a floating point tensor
floating = tf.Variable(3.567, tf.float64)
print(floating)
#this will print the floating point tensor

#we can also create a tensor with a range of values
list1 = tf.Variable([1,2,3,4,5], tf.int16)
print(list1)
#this will print the list tensor
#that is a 1D tensor

#we can also create a tensor of mutiple dimensions
list2 = tf.Variable([[1,2,3,4,5],[6,7,8,9,10]], tf.int16)
print(list2)
#this will print the list2 tensor
#that is a 2D tensor