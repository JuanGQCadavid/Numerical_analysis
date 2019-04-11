def incremental_search(point_x0,delta,niter,function,function_derivate):
    f_x0 = function(point_x0)
    if f_x0 == 0:
        print('The point ', f_x0,' is a root')
        return f_x0
    else:
        point_x1 = point_x0 + delta
        iter_counter = 1
        f_x1 = function(point_x1)

        while(f_x0*f_x1 > 0) and (iter_counter < niter):
            point_x0 = point_x1
            f_x0 = f_x1

            point_x1 = point_x0 + delta
            f_x1 = function(point_x1)

            iter_counter += 1
        if f_x1 == 0:
            print('The point ', f_x1,' is a root')
            return f_x1
        elif (f_x0*f_x1 < 0):
            print('There is a root between ',point_x0,' , ',point_x1)
            return point_x0,point_x1
        else:
            print('There is no root, fail by niter')
            return None

            
    
    

