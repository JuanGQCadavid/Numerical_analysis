clear global digits;
global digits = 9;
output_precision(9)
#Correct decimals with round
A = double(
[4 3 -2 -7 20;
3 12 8 -3 18;
2 3 -9 2 31;
1 -2 -5 6 12]);

n = size(A)(1);

function [L, U] = direct_factization_lu(A,n,type)
  if strcmp(type,"doolittle")
    [L, U] = direct_factization_doolittle(A,n);
  elseif strcmp(type,"crout")
    [L, U] = direct_factization_crout(A,n);
  elseif strcmp(type,"cholesky")
    [L, U] = direct_factization_cholesky(A,n);
  else 
    disp("Error");
  endif
endfunction

function [L, U] = direct_factization_crout(A,n)
  U = diag(diag(ones(n)));
  U = tril(U); 
  L = zeros(n);
  for k = 1:n
    disp(cstrcat("Etapa ",mat2str(k), ":"));
    acum = 0;
    for p = 1:k-1
      acum = acum + L(k,p)*U(p,k);
    endfor
    L(k,k) = A(k,k) - acum;
    
    for i = k+1:n
      acum = 0;
      for p = 1:k-1
        acum = acum + L(i,p)*U(p,k);
      endfor
      L(i,k) = (A(i,k) - acum)/U(k,k);
    endfor
    
    for j = k+1:n
      acum = 0;
      for p = 1:k-1
        acum = acum + L(k,p)*U(p,j);
      endfor
      U(k,j) = (A(k,j) - acum)/L(k,k);
    endfor
    L
    U 
  endfor
endfunction


function [L, U] = direct_factization_doolittle(A,n)
  L = diag(diag(ones(n)));
  L = tril(L); 
  U = zeros(n);
  for k = 1:n
    disp(cstrcat("Etapa ",mat2str(k), ":"));
    acum = 0;
    for p = 1:k-1
      acum = acum + L(k,p)*U(p,k);
    endfor
    U(k,k) = A(k,k) - acum;
    
    for i = k+1:n
      acum = 0;
      for p = 1:k-1
        acum = acum + L(i,p)*U(p,k);
      endfor
      L(i,k) = (A(i,k) - acum)/U(k,k);
    endfor
    
    for j = k+1:n
      acum = 0;
      for p = 1:k-1
        acum = acum + L(k,p)*U(p,j);
      endfor
      U(k,j) = (A(k,j) - acum)/L(k,k);
    endfor
    L
    U 
  endfor
endfunction

function [L, U] = direct_factization_cholesky(A,n)
  L = diag(diag(ones(n)));
  U = triu(L)
  L = tril(L) 
  for k = 1:n
    disp(cstrcat("Etapa ",mat2str(k), ":"));
    acum = 0;
    for p = 1:k-1
      acum = acum + L(k,p)*U(p,k);
    endfor
    L(k,k) = sqrt(A(k,k) - acum);
    U(k,k) = L(k,k);
    for i = k+1:n
      acum = 0;
      for p = 1:k-1
        acum = acum + L(i,p)*U(p,k);
      endfor
      L(i,k) = (A(i,k) - acum)/U(k,k);
    endfor
    
    for j = k+1:n
      acum = 0;
      for p = 1:k-1
        acum = acum + L(k,p)*U(p,j);
      endfor
      U(k,j) = (A(k,j) - acum)/L(k,k);
    endfor
    L
    U   
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
  z(1) = B(1)/L(1,1);
  for i = 2:n
    acum = 0;
    for j = i-1:-1:1
      acum = acum + L(i,j)*z(j);
    endfor
    z(i) = (B(i)-acum)/L(i,i);
  endfor
endfunction

[L, U] = direct_factization_lu(A,n,"doolittle")
z = progressive_substitution(L,A(:,n+1),n);
x = regressive_substitution(U, z, n);