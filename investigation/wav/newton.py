import numpy
x = [-4, -2, -1];
y = [-2.59625884456571, -0.696958389857672, 0.908181747039582];

table = [];
table.append(x);
table.append(y);

def newton_dd(x, y, diff_num):
    global table
    table_row_size = len(table[0]); 
    table_colunm_size = diff_num + 2;
    for i in range(2, table_colunm_size):
        table.append(numpy.zeros(table_row_size));
    for j in range(1, table_colunm_size):
        x_indx = 0;
        for i in range(j, table_row_size):
            result = (table[j][i]-table[j][i-1])/(x[i]-x[x_indx]);
            table[j+1][i]= result;
            x_indx += 1;

def evaluate(x, table):
    x_values = table[0];
    n = len(x_values);
    b = numpy.diag(table, -1);
    px = b[0];
    for i in range(1, n):
        mult = 1;
        for j in range(0, i):
            mult = mult * (x - x_values[j]);
        px = px + b[i] * mult;
    return px;

newton_dd(x,y, 2)
x_value = 1.45
print("")
res = evaluate(x_value,table)
print(res)