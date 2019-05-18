clear global digits;
global digits = 3;
output_precision(9)
#Correct decimals with round
A = double([
-7 2 -3 4 -12;
5 -1 14 -1 13;
1 9 -7 5 31;
-12 13 -8 -4 -32]);

n = size(A)(1);

A_aux = double(A);
function [L,U, A_changed] = factorization_with_gaussian_elimination_partial_pivoting(A,n)
  for k = 1:n-1
    disp(cstrcat("Etapa: ", mat2str(k)))
    A
    A = partial_pivoting(A, k,n)
    for i = k+1:n
      M = A(i,k)/A(k,k);
      disp(cstrcat("M",mat2str(i),mat2str(k), " = ",mat2str(M)))
      for j = k:n
        A(i,j) = A(i,j)-M*A(k,j);
      endfor
      A(i,k) = M;
    endfor
    A
  endfor
  U = triu(A(:,1:n));
  A_changed = A
  A(1:n+1:end) = diag(ones(n));
  L = tril(A(:,1:n));
endfunction

function pivoted = partial_pivoting(A, k,n)
  pivoted = A;
  disp("Partial pivoting");
  greater = abs(A(k,k));
  greater_row = k;
  for i = k + 1:n
    if abs(A(i,k)) > greater
      greater = abs(A(i,k));
      greater_row = i;
    endif
  endfor
  if greater == 0
    error("Equations system hasn't solution");
  endif
  if greater_row != k
    pivoted = change_rows(A, k, greater_row);
  else
    disp("Nothing");
  endif
endfunction

function changed_matrix = change_rows(A, k, greater_row)
  disp(cstrcat("Changing row ",mat2str(k), " with ",mat2str(greater_row)));
  aux = A(k,:);
  A(k,:) = A(greater_row,:);
  A(greater_row, :) = aux;
  changed_matrix = A;
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

[L, U, A_changed] = factorization_with_gaussian_elimination_partial_pivoting(A,n)
z = progressive_substitution(L,A_changed(:,n+1),n);
x = regressive_substitution(U, z, n);