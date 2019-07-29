
#coding:UTF-8

import tensorflow as tf
import tensorflow.examples.tutorials.mnist.input_data as input_data

import os

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

data_sets = input_data.read_data_sets(FLAGS.train_dir, FLAGS.fake_data)