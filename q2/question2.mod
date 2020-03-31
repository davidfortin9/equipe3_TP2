set I;
set J;
set K;

param D {i in I, j in J};
param l;

var x {i in I,j in J} binary;
var u {i in I};

minimize Z: sum{i in I, j in K} D[i, j] * x[i,j];
	
	
subject to chemin_continu {i in I, j in K}: u[i] - u[j] + (l*x[i,j]) + 1 <= l;

subject to parcourir_tous_lieux_I {i in I}: sum{j in J} x[i,j] = 1;

subject to parcourir_tous_lieux_J {j in J}: sum{i in I} x[i,j] = 1;
	