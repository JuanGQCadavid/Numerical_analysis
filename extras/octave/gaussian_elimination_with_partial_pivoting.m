output_precision(7)
#Correct decimals with round
A = double([
-7 2 -3 4 -12;
5 -1 14 -1 13;
1 9 -7 5 31;
-12 13 -8 -4 -32]);
n = size(A)(1);

A_aux = double(A)
function retvar = simple_gaussian_elimination(A,n)
  for k = 1:n-1
    disp(cstrcat("Etapa: ", mat2str(k)))
    A
    A = partial_pivoting(A, k,n)
    for i = k+1:n
      M = A(i,k)/A(k,k);
      disp(cstrcat("M",mat2str(i),mat2str(k), " = ",mat2str(M)))
      for j = k:n+1
        A(i,j) = A(i,j)-M*A(k,j);
      endfor
    endfor
    A
  endfor
  retvar = A;
endfunction

function pivoted = partial_pivoting(A, k,n)
  disp("Partial pivoting");
  greater = abs(A(k,k));
  greater_row = k;
  for i = k + 1:n
    if abs(A(i,k)) > greater
      greater = abs(A(i,k))
      greater_row = i
    endif
  endfor
  if greater == 0
    error("Equations system hasn't solution");
  endif
  pivoted = change_rows(A, k, greater_row);
endfunction

function changed_matrix = change_rows(A, k, greater_row)
  aux = A(k,:);
  A(k,:) = A(greater_row,:);
  A(greater_row, :) = aux;
  changed_matrix = A;
endfunction

function regressive_substitution(A,n)
  x = [];
  x(n) = A(n,n+1)/A(n,n);
  disp(cstrcat("X",mat2str(n),": ",mat2str(x(n),10)))
  for i = n-1:-1:1
    acum = 0;
    for p = i+1:n
      acum = acum + A(i,p)*x(p);
    endfor
    x(i) = (A(i,n+1)-acum)/A(i,i);
    disp(cstrcat("X",mat2str(i),": ",mat2str(x(i),10)))
  endfor
endfunction


T = double(simple_gaussian_elimination(A,n))
regressive_substitution(T,n)
