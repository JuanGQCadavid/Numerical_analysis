import numpy as np

def main():
    ecu_1 = [25.,-3.,4.,-7.,8.]
    ecu_2 = [6.,42.,-7.,9.,21.]
    ecu_3 = [5.,12.,-73.,8.,19.]
    ecu_4 = [2.,-7.,13.,-95.,-25.]

    matrix = np.array([ecu_1,ecu_2,ecu_3,ecu_4])
    new_matrix = gausianElimination(matrix)

    final_matriz,b_vector,ans = resolveMatrix(new_matrix)

    print('*'*64)
    print('-------------Matrix-------------')
    print(final_matriz)
    print('-------------  b   -------------')
    print(b_vector)
    print('------------- ans  -------------')
    print(ans)
    print('*'*64)
    

def gausianElimination(matrix):
    ecuations_number = len(matrix)
    x0_xn_b = len(matrix[0]) #x0 x1 .. xn b

    for k in range(0,ecuations_number -1):
        for i in range(k + 1,ecuations_number):
            mult = matrix[i,k]/matrix[k,k]
            for j in range(k, x0_xn_b):
                matrix[i,j] = matrix[i,j] - mult* matrix[k,j]
        print(matrix)
        print('------------------------')    


    return matrix

def resolveMatrix(matrix):
    
    x0_xn = len(matrix[0]) -1 #x0 x1 .. xn
    
    b_vector = np.ravel(matrix[:,x0_xn:])
    matrix = matrix[:,0:len(matrix)]
    ans = np.zeros(len(b_vector))
    
    ecuations_number = len(matrix)

    


    #Resolve X4, start point.
    ans[len(ans)-1] = b_vector[len(ans)-1]/matrix[len(ans)-1][len(ans)-1]
    k = ecuations_number - 2
    while(k >= 0):
        sum = 0
        for i in range(k,x0_xn):
            sum += matrix[k][i]*ans[i]
        ans[k] = (b_vector[k]-sum)/matrix[k][k]
        k -= 1

    return matrix,b_vector,ans
    
main()