#-------------Ensembles et paramètres-----------------------------
set I; # origine
set J; # destination
set T; # tour
set Y; # tour plus 1


param Dist_Matrice {I,J,T} >=0; #matrice des distance entre i et j


#-------------Variables de décision-----------------------------------

var X{t in T, i in I, j in J} binary; # determine si le point ij est visiter au tour t
var P{t in T, j in J} binary; # variable qui discrimini ou sera le prochain depart
var F{y in Y, i in I} binary; # variable qui discrimini ou sera le prochain depart

#-------------Fonction objective--------------------------------------
minimize Total_distance: sum{t in T, i in I, j in J} X [t,i,j] * Dist_Matrice [t,i,j];

#-------------Contrainte----------------------------------------------



subject to nombre_point_par_t {t in T}: sum{i in I, j in J} X[t,i,j] = 1;# limite le nombre de point par tour a 1
subject to point_different_par_t {i in I, j in J}: sum{t in T} X[t,i,j] <= 1;# empeche que le meme point soit visiter plusieurs fois
subject to arriver {t in T, j in J}: sum{i in I} X[t,i,j]  =  P[t,j];# permet de determiner dans quel colonne j le point est
subject to depart {y in Y, i in I}: sum {j in J} X[y,i,j] = F[y,i];# permet de determiner dans quel rangé i le point est
subject to arrive_t_depart_t1 {y in Y, i in I}: P[y-1,i] = F[y,i];# au tour suivant le point doit commencer dans la rangé i qu au tour precedant il a terminer dans la colonne j 
subject to destination_obligatoire {i in I}: sum {t in T} P[t,i] = 1;# un maximum d'un seule colonne visite par tour

