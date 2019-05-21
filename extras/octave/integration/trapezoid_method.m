clear all
pkg load symbolic
format short g
clear global digits;
global digits = 9;
output_precision(10)

xa = 1;
xb = 2;

x = sym('x');
fx = exp(x) - 2 * x;
d2fx = exp(x);
global f = function_handle(fx);
global d2f = function_handle(d2fx);

function result = trapezoid_simple(a, b)
  global f;
  h = b - a;
  result = h * ( f(a) + f(b) )/2;
  error = h^3 / 12 *  d2f_si_max(a,b,0.1);
  #error = h^3 / 12 *  d2f_si_prom(a,b,0.1);
  disp(cstrcat("By trapezoid_simple method: ", mat2str(result), " + ",mat2str(error)));
endfunction

function result = composite_trapezoid(a, b, n)
  global f;
  h = (b - a)/n;
  result = f(a)+f(b);
  acum = 0;
##  cont = 0
##  a
##  f(a)
  for i = a+h:h:b-h
##    cont += 1
##    i
##    f(i)
    acum += f(i);
  endfor
  result = (h/2)*(result+2*acum);
  error = h^3 / (12 * n^2) *  d2f_si_prom(a,b,0.1);
  
  disp(cstrcat("By composite_trapezoid method: ", mat2str(result), " + ",mat2str(error)));
endfunction


function result = d2f_si_max(a,b, h)
  global d2f;
  result = d2f(a);
  for i = a+h:h:b
    actual = d2f(i);
    if actual > result
     result = actual;
    endif
 endfor
endfunction

function result = d2f_si_prom(a,b, h)
  global d2f;
  acum = 0;
  n = (b - a) / h;
  for i = a+h:h:b
    acum += d2f_si_max(i-h,i,0.1);
    #acum += d2f(i);
  endfor
  result = acum / n;
endfunction

trapezoid_simple(xa,xb);
composite_trapezoid(xa,xb,10);