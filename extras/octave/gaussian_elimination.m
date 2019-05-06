output_precision(7)
#Correct decimals with round
A = double([14 6 -2 3 12;
3 15 2 -5 32;
-7 4 -23 2 -24;
1 -3 -2 16 14]);
n = size(A)(1);

A_aux = double(A)
function retvar = simple_gaussian_elimination(A,n)
  for k = 1:n-1
    disp(cstrcat("Etapa: ", mat2str(k)))
    A
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

function regressive_substitution(A,n)
  x = [];
  x(n) = A(n,n+1)/A(n,n);
  disp(cstrcat("X",mat2str(n),": ",mat2str(x(n))))
  for i = n-1:-1:1
    acum = 0;
    for p = i+1:n
      acum = acum + A(i,p)*x(p);
    endfor
    x(i) = (A(i,n+1)-acum)/A(i,i);
    disp(cstrcat("X",mat2str(i),": ",mat2str(x(i))))
  endfor
endfunction


T = double(simple_gaussian_elimination(A,n))
regressive_substitution(T,n)