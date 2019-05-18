format short g
clear global digits;
global digits = 9;
output_precision(9)
#Correct decimals with round
A = double(
[45 13 -4 8 -25;
-5 -28 4 -14 82;
9 15 63 -7 75;
2 3 -8 -42 -43]);
# Coeficient's matrix size
n = size(A)(1);

#x = [2 3 -5 8 -10];
# Norma 1 implementation
function result = norma(x)
  n = size(x)(2);
  result = 0;
  for i = 1:n
    result = result + abs(x(i));
  endfor
endfunction
#norma(x)

# norma rara
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
function x = jacobi(A, n, x_ini, iter, tol)
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
    endfor
    # dispersion = (norma(x) - norma(x_ini))/norma(x)
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
x_ini = [2 2 2 2];
jacobi(A, n, x_ini, 20, 10^(-5));