import tensorflow as tf

x1 = tf.constant(5)
x2 = tf.constant(6)

result = tf.multiply(x1, x2)
#result=x1*x2 위 아래 두개 다 같은 결과값 출력 가능

#print(result) 세션이 열리지 않아서 출력되지 않음
sess = tf.Session() 

#print(sess.run(result))
with tf.Session() as sess:
    output = sess.run(result)
    print(output)

print(output) #세션이 닫혀도 레퍼런스 결과가 출력됨
# print(sess.run(result)) 하지만 닫힌 오브젝트는 출력될 수 없음

# cost가 들어가는 function을 최적화 해달라고 텐서에게 요청하는 것 

# sess.close()
# session은 connection object이다
