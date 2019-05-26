clear all
pkg load symbolic
format short g
clear global digits;
global digits = 9;
output_precision(10)

x = [-1, 1, 2, 4];
y = [-2.1, 3.5, 7.8, -7.2];

function cuadratic(x_val,y)
  # first n-1 polinomial
  n = size(x_val)(2);
  for i = 1:n-1
    printf("a%d * x^2 + b%d * x + c%d  %.2f <= x <= %.2f \n", i,i,i, x_val(i),x_val(i+1))
  endfor
  
  disp("Equations")
  x2 = x_val(1)^2;
  x = x_val(1);
  y_val = y(1);
  printf("a1 * %.2f + b1 * %.2f + c1 = %.3f\n", x2,x,y_val)
  
  x2 = x_val(2)^2;
  x = x_val(2);
  y_val = y(2);
  printf("a1 * %.2f + b1 * %.2f + c1 = %.3f\n", x2,x,y_val)
  disp("")
  for i = 2:n-1
    x2 = x_val(i)^2;
    x = x_val(i);
    y_val = y(i);
    printf("a%d * %.2f + b%d * %.2f + c%d = %.3f\n", i,x2,i,x,i,y_val)
    x2 = x_val(i+1)^2;
    x = x_val(i+1);
    y_val = y(i+1);
    printf("a%d * %.2f + b%d * %.2f + c%d = %.3f\n", i,x2,i,x,i,y_val)
    disp("")
  endfor
  
  for i = 1:n-2
    x = 2*x_val(i+1);
    printf("a%d * %.2f + b%d =", i,x,i)
    printf(" a%d * %.2f + b%d", i+1,x,i+1)
    disp("")
  endfor
  disp("")
  printf("a%d = 0\n", 1)
endfunction

function cubic(x_val,y)
  # first n-1 polinomial
  n = size(x_val)(2);
  for i = 1:n-1
    printf("a%dx^3 + b%dx^2 + c%dx + d%d  %.2f <= x <= %.2f \n", i,i,i,i, x_val(i),x_val(i+1))
  endfor
  
  disp("Equations")
  x3 = x_val(1)^3;
  x2 = x_val(1)^2;
  x = x_val(1);
  y_val = y(1);
  printf("a1 * %.2f + b1 * %.2f + c1 * %.2f + d1 = %.3f\n", x3,x2,x,y_val)
  
  x3 = x_val(2)^3;
  x2 = x_val(2)^2;
  x = x_val(2);
  y_val = y(2);
  printf("a1 * %.2f + b1 * %.2f + c1 * %.2f + d1 = %.3f\n", x3,x2,x,y_val)
  disp("")
  for i = 2:n-1
    x3 = x_val(i)^3;
    x2 = x_val(i)^2;
    x = x_val(i);
    y_val = y(i);
    printf("a%d * %.2f + b%d * %.2f + c%d * %.2f + d%d = %.3f\n", i,x3,i,x2,i,x,i,y_val)
    x3 = x_val(i+1)^3;
    x2 = x_val(i+1)^2;
    x = x_val(i+1);
    y_val = y(i+1);
    printf("a%d * %.2f + b%d * %.2f + c%d * %.2f + d%d = %.3f\n", i,x3,i,x2,i,x,i,y_val)
    disp("")
  endfor
  
  for i = 1:n-2
    x2 = 3*x_val(i+1)^2;
    x = 2*x_val(i+1);
    printf("a%d * %.2f + b%d * %.2f + c%d =", i,x2,i,x,i)
    printf(" a%d * %.2f + b%d * %.2f + c%d", i+1,x2,i+1,x,i+1)
    disp("")
  endfor
  disp("")
  
  
  for i = 1:n-2
    x = 6*x_val(i+1);
    printf("a%d * %.2f + 2 * b%d =", i,x,i)
    printf(" a%d * %.2f + 2 * b%d", i+1,x,i+1)
    disp("")
  endfor
  disp("")
  x = 6 * x_val(1);
  printf("a%d * %.2f + 2 * b%d = 0\n", 1,x,1)
  x = 6 * x_val(n);
  printf("a%d * %.2f + 2 * b%d = 0\n", 4,x,4)
endfunction

#cuadratic(x, y)
cubic(x,y)