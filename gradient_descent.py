import numpy as np

x = np.array([1,2,3,4,5]);
y = np.array([5,7,9,11,13])

print("y-x", y-x)
print(sum(2*(y-x)))

z = [val**2 for val in x]
print('z: ', z)

def gradient_descent(x,y):
    m_curr = b_curr = 0
    iterations = 10000
    n = len(x)
    
    learning_rate = 0.08
    for i in range(iterations):
        y_predicted = m_curr*x + b_curr
        cost = (1/n) * sum([val**2 for val in (y-y_predicted)])
        print('y-predicted', y_predicted)
        # md === m derivatives
        md = -(2/n)*sum(x*(y-y_predicted))
        bd = -(2/n)*sum(y-y_predicted)
        m_curr = m_curr - learning_rate * md
        b_curr = b_curr - learning_rate * bd
        print("m {}, b {}, cost {}, iteartion {}".format(m_curr, b_curr, cost, i))
        
 
gradient_descent(x, y)

