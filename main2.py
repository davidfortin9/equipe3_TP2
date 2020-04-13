import fastroute_problem as frp 
import route_solution as rsol 
import FrpAmplMipSolver as frprsampl
import pickseq as psq


matrice = psq.create_dist_matrix
frp_inst = frp.FastRouteProb(dist_matrix=matrice)

# Run
print('Problème actuel:')
print(str(frp_inst))
print('Résoudre le problème...')
frp_solver = frprsampl.FrpAmplMipSolver()
frp_sol = frp_solver.solve(frp_inst)

print('Solution retournée:')
print(str(frp_sol))
#print(str(frp_sol.evaluate()))