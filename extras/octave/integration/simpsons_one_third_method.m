clear all
pkg load symbolic
format short g
clear global digits;
global digits = 9;
output_precision(10)
x = sym('x');

##xa = 0;
##xb = 1;
##n = 5;
##
##fx = exp(x^2);
##d2fx = exp(x^2);

xa = 1;
xb = 2;
n = 10;

fx = exp(x) - 2 * x;
d2fx = exp(x);
d4fx = exp(x);

global f = function_handle(fx);
global d4f = function_handle(d4fx);

function result = simpsons_one_third_simple(a, b)
  global f;
  h = (b - a)/2;
  m = (a + b) / 2;
  result = (h/3) * ( f(a) + 4 * f(m) + f(b) );
  error = h^5 / 90 *  d4f_si_max(a,b,0.1);
  #error = h^5 / 90 *  d4f_si_prom(a,b,0.1);
  disp(cstrcat("By simpsons_one_third_simple method: ", mat2str(result), " - ",mat2str(error)));
endfunction

function result = composite_simpsons_one_third(a, b, n)
  global f;
  n;
  h = (b - a)/n;
  result = f(a)+f(b);
  acum_par = 0;
  acum_impar = 0;
##  cont = 0
##  a
##  f(a)
  for i = a+h:2*h:b-h
##      cont = cont + 1
##      i
##      f(i)
      acum_impar += f(i);
    if i+h != b 
##      cont = cont + 1
##      i_par = i+h
##      f(i+h)
      acum_par += f(i+h);
    endif
  endfor
  result = (h/3)*(result+4*acum_impar+2*acum_par);
  error = (b-a)*h^4 / (180) *  d4f_si_prom(a,b,0.1);
  
  disp(cstrcat("By composite_simpsons_one_third method: ", mat2str(result), " - ",mat2str(error)));
endfunction


function result = d4f_si_max(a,b, h)
  global d4f;
  result = d4f(a);
  for i = a+h:h:b
    actual = d4f(i);
    if actual > result
     result = actual;
    endif
 endfor
endfunction

function result = d4f_si_prom(a,b, h)
  global d4f;
  acum = 0;
  n = (b - a) / h / 2;
  for i = a+2*h:2*h:b
    acum += d4f_si_max(i-2*h,i,0.1);
    #acum += d4f(i);
  endfor
  result = acum / n;
endfunction

simpsons_one_third_simple(xa,xb);
composite_simpsons_one_third(xa,xb,n);