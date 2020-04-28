set LOCATIONS ordered;

param dist {LOCATIONS, LOCATIONS};

var vX {LOCATIONS} integer;
 
var vD {LOCATIONS} integer >= 0;

minimize Z: 
    sum {i in LOCATIONS} vD[i];

subject to all_diff:
    alldiff {i in LOCATIONS} vX[i];
    
subject to distances {k in LOCATIONS diff {last(LOCATIONS)}, i in LOCATIONS, j in LOCATIONS}:
     vX[k] = i and vX[k + 1] = j ==> vD[i] = dist[i,j];
     
subject to lb {i in LOCATIONS}:
    vX[i] >= first(LOCATIONS);

subject to ub {i in LOCATIONS}:
    vX[i] <= last(LOCATIONS);
