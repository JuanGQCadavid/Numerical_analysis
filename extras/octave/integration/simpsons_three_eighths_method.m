clear all
pkg load symbolic
format short g
clear global digits;
global digits = 9;
output_precision(10)
x = sym('x');

xa = 20.57142857;
xb = 30;
# n = points - 1
n = 5;

fx = 2000 * log(140000 / (140000 - 2100 * x)) - 9.8 * x;
d4fx = diff(fx,4)
simplify(d4fx)

##xa = 0;
##xb = 9;
##n = 8;
##
##fx = 2 * x;
##d4fx = diff(fx,4)
##simplify(d4fx)

global f = function_handle(fx);
global d4f = function_handle(d4fx);

function result = simpsons_three_eighths_simple(a, b)
  global f;
  h = (b - a)/3;
  x0 = a;
  x1 = x0 + (b-a)/3;
  x2 = x0 + 2*(b-a)/3;
  x3 = b;  
  
  result = (3*h/8) * ( f(x0) + 3 * f(x1) + 3 * f(x2) + f(x3) );
  error = (b-a)^5 / 6480 *  d4f_si_max(a,b,0.1);
  #error = (b-a)^5 / 6480 *  d4f_si_prom(a,b,0.1);
  disp(cstrcat("By simpsons_three_eighths_simple method: ", mat2str(result), " - ",mat2str(error)));
endfunction

function result = composite_simpsons_three_eighths(a, b, n)
  global f;
  h = (b - a)/n
  result = f(a)+f(b);
  acum_one = 0;
  acum_two = 0;
  acum_three = 0;
  cont = 0
  a
  f(a)
  for i = a + h:3*h:b - h
      cont = cont + 1
      i
      f(i)
      acum_one += f(i);
    if i + h != b 
      cont = cont + 1
      i_two = i+h
      f(i+h)
      acum_two += f(i+h);
    endif
    
    if (i + 2 * h) <= b - h
      cont = cont + 1
      i_three = i + 2 * h
      f(i + 2 * h)
      acum_three += f(i + 2 * h);
    endif
  endfor
  result = (3 * h/8)*(result + 3 * acum_one + 3 * acum_two + 2 * acum_three);
  error = (b-a)*h^4 / (80) *  d4f_si_prom(a,b,0.1);
  
  disp(cstrcat("By composite_simpsons_three_eighths method: ", mat2str(result), " - ",mat2str(error)));
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

simpsons_three_eighths_simple(xa,xb);
n = 3;
composite_simpsons_three_eighths(xa,xb,3);