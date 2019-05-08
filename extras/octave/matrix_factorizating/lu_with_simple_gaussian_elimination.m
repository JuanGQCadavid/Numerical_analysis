global digits = 9;
output_precision(9)
#Correct decimals with round
A = double(
[4 3 -2 -7 20;
3 12 8 -3 18;
2 3 -9 2 31;
1 -2 -5 6 12]);

n = size(A)(1);

A_aux = double(A)
function [L, U] = factorization_with_gaussian_elimination(A,n) 
  L = tril(ones(n))
  U = triu(A(1,1:n))
  for k = 1:n-1
    disp(cstrcat("Etapa: ", mat2str(k)))
    A
    for i = k+1:n
      M = A(i,k)/A(k,k);
      L(i,k) = M;
      disp(cstrcat("M",mat2str(i),mat2str(k), " = ",mat2str(M)))
      for j = k:n+1
        A(i,j) = A(i,j)-M*A(k,j);
      endfor
      U(i,:) = A(i,1:n);
    endfor
    A
  endfor
endfunction

function x = regressive_substitution(U, z,n)
  global digits;
  x = [];
  x(n) = z(n)/U(n,n);
  disp(cstrcat("X",mat2str(n),": ",mat2str(x(n), digits)))
  for i = n-1:-1:1
    acum = 0;
    for p = i+1:n
      acum = acum + U(i,p)*x(p);
    endfor
    x(i) = (z(i)-acum)/U(i,i);
    disp(cstrcat("X",mat2str(i),": ",mat2str(x(i), digits)))
  endfor
endfunction

function z = progressive_substitution(L,B,n)
  z = [];
  z(1) = B(1);
  for i = 1:n
    acum = 0;
    for j = i-1:-1:1
      acum = acum + L(i,j)*z(j);
    endfor
    z(i) = (B(i)-acum);
  endfor
endfunction

[L, U] = factorization_with_gaussian_elimination(A,n)
z = progressive_substitution(L,A(:,n+1),n);
x = regressive_substitution(U, z, n);