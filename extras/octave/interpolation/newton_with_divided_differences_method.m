clear all
format short g
clear global digits;
global digits = 9;
output_precision(9)
x = [-4 -2 -1];
y = [-2.59625884456571, -0.696958389857672, 0.908181747039582];

global table = [];
table(:,1) = x;
table(:,2) = y;

function newton_dd(x, y, diff_num)
  global table;
  table_row_size = size(table)(1); 
  table_colunm_size = diff_num + 2;
  for j = 3:table_colunm_size
    x_indx = 1;
    for i = j - 1:table_row_size
      table(i, j) = (table(i-1,j-1)-table(i, j-1))/(x(x_indx)-x(i));
      x_indx += 1;
    endfor 
  endfor      
endfunction




function table_printer(table, x_size, fx_size, diff_size)
  [table_row_size, table_colunm_size] = size(table);
  x_tittle = ["x" blanks(x_size+1)];
  fx_tittle = [" fx" blanks(fx_size+1)];
  diff_tittle = [" ", mat2str(1) blanks(diff_size + 3)];  
  for i = 2: table_colunm_size - 2
    diff_tittle = cstrcat(diff_tittle," ",[mat2str(i) blanks(diff_size + 3)]);  
  endfor
  printf('%s  %s  %s', x_tittle, fx_tittle, diff_tittle);
  disp("")
  
  for i = 1:table_row_size
    for j = 1:table_colunm_size
      sign = " ";#+
      if table(i,j) < 0
        sign = "";
      endif
      if j == 1
        printf([sign '%.' num2str(x_size) 'f  '], table(i,j));
      elseif j == 2
       printf([sign '%.' num2str(fx_size) 'f  '], table(i,j));
      #elseif table(i,j) == 0
       #  printf([sign '%.' num2str(diff_size) 's  '], blanks(1));
      else
       printf([sign '%.' num2str(diff_size) 'f  '], table(i,j));
     endif   
    endfor
    disp("");  
  endfor
endfunction
newton_dd(x,y, 5);
table_printer(table, 1,15,15);