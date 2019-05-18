format short g
clear global digits;
global digits = 9;
output_precision(9)
#Correct decimals with round
A = double(
[5 3 1 24;
3 4 -1 30;
1 -1 4 -24]);
# Coeficient's matrix size
n = size(A)(1);

# Gauss Seidel Relaxation
#x = [2 3 -5 8 -10];
# norm 1 implementation
function result = norm(x)
  n = size(x)(2);
  result = 0;
  for i = 1:n
    result = result + abs(x(i));
  endfor
endfunction
#norm(x)

# Euclidean norm
function result = euclidean_norm(x, x_ini, n)
  sum = 0;
  for i = 1:n
    sum = sum + (x(i) - x_ini(i))^2;
  endfor
  result = sqrt(sum);
endfunction

# Weird norm
function max = mayor(x, x_ini, n)
  max = abs(x(1) - x_ini(1));
  for i = 1:n
    delta = abs(x(i) -x_ini(i));
    if delta > max
      max = delta;
    endif
  endfor
endfunction

# Is better if the matrix is positive definite. Isolates variables in
# matrix's diagonal
function x = gauss_seidel_relaxated(A, n, x_ini, iter, tol, parameter)
  x = [];
  if iter <= 0
    disp("Error: Iterations must be greater than 0")
    return
  endif
  k = 0;
  tol
  disp(cstrcat("Iteration ", mat2str(k)));  
  dispersion = tol + 1
  x_ini
  disp("\n")
  while (dispersion > tol) && (k < iter)
    disp(cstrcat("Iteration ", mat2str(k+1)))  
    for i = 1:n
      sum = 0;
      for j = 1:i-1
        if i != j
          sum = sum + A(i,j)*x(j);
        endif
      endfor
      
      for j = i+1:n
        if i != j
          sum = sum + A(i,j)*x_ini(j);
        endif
      endfor
      
      x(i) = (A(i,n+1) - sum)/A(i,i);
      x(i) = parameter * x(i) + (1 - parameter) * x_ini(i);
    endfor
    # dispersion = (norm(x) - norm(x_ini))/norm(x)
    dispersion = euclidean_norm(x, x_ini,n)
    x
    disp("\n")
    x_ini = x;
    k = k + 1;
  endwhile
  if dispersion < tol
    disp(cstrcat("Aproximation with tolerance = ", mat2str(tol)));
    x
  else
    disp(cstrcat("Fail in iteration = ", mat2str(k)));
  endif
endfunction

# Is better if the matrix is positive definite. Isolates variables in
# matrix's diagonal
function x = jacobi_relaxated(A, n, x_ini, iter, tol, parameter)
  x = [];
  if iter <= 0
    disp("Error: Iterations must be greater than 0")
    return
  endif
  k = 0;
  tol
  disp(cstrcat("Iteration ", mat2str(k)));  
  dispersion = tol + 1
  x_ini
  while (dispersion > tol) && (k < iter)
    disp(cstrcat("Iteration ", mat2str(k+1)))  
    for i = 1:n
      sum = 0;
      for j = 1:n
        if i != j
          sum = sum + A(i,j)*x_ini(j);
        endif
      endfor
      x(i) = (A(i,n+1) - sum)/A(i,i);
      x(i) = parameter * x(i) + (1 - parameter) * x_ini(i);
    endfor
    # dispersion = (norm(x) - norm(x_ini))/norm(x)
    dispersion = mayor(x, x_ini,n)
    x
    disp("\n")
    x_ini = x;
    k = k + 1;
  endwhile
  if dispersion <= tol
    disp(cstrcat("Aproximation with tolerance = ", mat2str(tol)));
    x
  else
    disp(cstrcat("Fail in iteration = ", mat2str(k)));
  endif
endfunction

x_ini = [0 0 0];
gauss_seidel_relaxated(A, n, x_ini, 5, 2.5*10^(-7), 1);
#jacobi_relaxated(A, n, x_ini, 30, 4.8*10^(-5), 1);
A = double([
13 -3 4 -8 -20;
-5 15 6 4 32;
7 -3 14 5 -36;
-6 4 9 17 40
]);
n = size(A)(1);
x_ini = [6.2 5.1 -7 7];
#jacobi_relaxated(A, n, x_ini, 30, 4.8*10^(-5), 0.6);
#gauss_seidel_relaxated(A, n, x_ini, 30, 1.35*10^(-14), 1.6);