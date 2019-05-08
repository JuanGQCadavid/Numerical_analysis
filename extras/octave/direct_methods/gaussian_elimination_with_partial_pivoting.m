clear global digits;
global digits = 10;
output_precision(7)
#Correct decimals with round
A = double([
2 -3 4 1 10;
-4 2 1 -2 -10;
1 3 -5 3 32;
-3 -1 1 -1 -21]);
n = size(A)(1);

A_aux = double(A);
function [retvar, marks] = gaussian_elimination_total_pivoting(A,n)
  marks = [1:n]
  for k = 1:n-1
    disp(cstrcat("Etapa: ", mat2str(k)))
    A
    [A, marks] = total_pivoting(A, k,n, marks)
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
  marks
endfunction

function [pivoted, marks] = total_pivoting(A, k,n, marks)
  pivoted = A;
  disp("Total pivoting");
  greater = 0;
  greater_row = k;
  greater_column = k;
  for j = k:n
    for i = k:n
      if abs(A(i,j)) > greater
        greater = abs(A(i,j));
        greater_row = i;
        greater_column = j;
      endif
    endfor
  endfor
  if greater == 0
    error("Equations system hasn't solution");
  endif
  greater
  changed = false;
  if greater_row != k
    pivoted = change_rows(A, k, greater_row)
    changed = true;
  endif
  if greater_column != k
    pivoted = change_column(pivoted,k,greater_column)
    aux = marks(k);
    marks(k) = marks(greater_column);
    marks(greater_column) = aux;
    changed = true;
  endif
  if !changed
    disp("Nothing changed");
  endif
endfunction

function changed_matrix = change_rows(A, k, greater_row)
  disp(cstrcat("Changing row ",mat2str(k), " with ",mat2str(greater_row)));
  aux = A(k,:);
  A(k,:) = A(greater_row,:);
  A(greater_row, :) = aux;
  changed_matrix = A;
endfunction

function changed_matrix = change_column(A, k, greater_column)
  disp(cstrcat("Changing column ",mat2str(k), " with ",mat2str(greater_column)));
  aux = A(:,k);
  A(:,k) = A(:,greater_column);
  A(:, greater_column) = aux;
  changed_matrix = A;
endfunction

function regressive_substitution(A,n, marks)
  global digits;
  x = [];
  x(n) = A(n,n+1)/A(n,n);
  disp(cstrcat("X",mat2str(marks(n)),": ",mat2str(x(n),digits)))
  for i = n-1:-1:1
    acum = 0;
    for p = i+1:n
      acum = acum + A(i,p)*x(p);
    endfor
    x(i) = (A(i,n+1)-acum)/A(i,i);
    disp(cstrcat("X",mat2str(marks(i)),": ",mat2str(x(i),digits)))
  endfor
endfunction


[T, marks] = gaussian_elimination_total_pivoting(A,n)
regressive_substitution(T,n,marks)