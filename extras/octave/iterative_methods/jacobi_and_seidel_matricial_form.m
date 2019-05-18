format short g
clear global digits;
global digits = 9;
output_precision(9)
#Correct decimals with round
#Aumented matrix
A = double(
[8 3 5 21;
-2 7 3 7;
4 -5 18 42]);
# Coeficient's matrix size
n = size(A)(1);


# Euclidean norm
function result = euclidean_norm(x, x_ini, n)
  sum = 0;
  for i = 1:n
    sum = sum + (x(i) - x_ini(i))^2;
  endfor
  result = sqrt(sum);
endfunction

function x = jacobi_matricial(A, n, x_ini, iter, tol)
  x = [];
  #Matrix of coeficients
  if iter <= 0
    disp("Error: Iterations must be greater than 0")
    return
  endif
  
  A_c = A(:,1:3)
  b = A(:,4)
  D = diag(diag(A_c))
  L = tril(-A_c,-1)
  U = triu(-A_c,1)
  
  k = 0;
  tol
  disp(cstrcat("Iteration ", mat2str(k)));
  dispersion = tol + 1;
  x_ini
  while dispersion > tol && k < iter  
    disp(cstrcat("Iteration ", mat2str(k+1)));
    x = inv(D) * (L+U) * x_ini' + inv(D) * b;
    dispersion = euclidean_norm(x, x_ini, n)
    x = x'
    disp("\n");
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

function x = gauss_seidel_matricial(A, n, x_ini, iter, tol)
  x = [];
  #Matrix of coeficients
  if iter <= 0
    disp("Error: Iterations must be greater than 0")
    return
  endif
  
  A_c = A(:,1:3)
  b = A(:,4)
  D = diag(diag(A_c))
  L = tril(-A_c,-1)
  U = triu(-A_c,1)
  
  k = 0;
  tol
  disp(cstrcat("Iteration ", mat2str(k)));
  dispersion = tol + 1;
  x_ini
  while dispersion > tol && k < iter  
    disp(cstrcat("Iteration ", mat2str(k+1)));
    x = inv(D-L) * U * x_ini' + inv(D-L) * b;
    dispersion = euclidean_norm(x, x_ini, n)
    x = x'
    disp("\n");
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

x_ini = [0 0 0]
#jacobi_matricial(A,n, x_ini, 5, 10^(-5))
gauss_seidel_matricial(A,n, x_ini, 5, 10^(-5))