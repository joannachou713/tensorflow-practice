import tensorflow as tf
width = tf.placeholder('int32', name='width')
height = tf.placeholder('int32', name='height')
area = tf.multiply(width,height, name='area')  

with tf.Session() as sess:
    init = tf.global_variables_initializer()
    sess.run(init)
    print('area=',sess.run(area,feed_dict={width: 6, height: 8}))

tf.summary.merge_all()  #整合要顯示的資料
train_writer = tf.summary.FileWriter('log/area',sess.graph)   #主要寫入當前執行目錄下的log/area子目錄