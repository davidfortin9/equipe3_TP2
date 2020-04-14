#-------------Ensembles et param�tres-----------------------------

param n >= 0; #Quantit� de noeuds
param K >= 0; #Quantit� de picker disponible
param B >= 0; #Capacit� de transport par picker

set I;
set J;
set N := 0..n; # Ensemble du nombre de noeuds
set A := {i in N, j in N: i <> j}; # Ensemble des pair (i,j) ou i est diff�rent de j

param c{A} >= 0; # Matrice des distance entre i et j
param d{1 .. n}; # Quantit� de stock au noeud i

#-------------Variables de d�cision-----------------------------------

var x{A} binary; # determine si le point ij est visiter
var u{1..n} >= 0; # variable qui discrimini ou sera le prochain depart

#-------------Fonction objective--------------------------------------

minimize Z: sum{i in N, j in N: i<>j} c[i,j]*x[i,j]; 

#-------------Contraintes----------------------------------------------

s.t. arc_entrant {j in 1..n}: sum{i in N: i <> j} x[i,j] = 1; # assure qu'on entre dans tous les arc 1 seul fois

s.t. arc_sortant {i in 1..n}: sum{j in N: j <> i} x[i,j] = 1; # assure qu'on sorte dans tous les arc 1 seul fois

s.t. vehicules: sum{j in 1..n} x[0,j] <= K; # assure que tous les vehicules retourne au point de depart
 
s.t. sub_routine {i in 1..n, j in 1..n: i <> j}: u[j] - u[i] + B*x[i,j] <= B - d[i]; # assure que le chemin reste continu du depart a l'arrive

s.t. Limites {i in 1..n}: d[i] <= u[i] <= B; # determine les limites parcouru par le vehicule