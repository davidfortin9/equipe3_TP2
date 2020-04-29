import whouse_modules.pickseq as pickseq
import whouse_modules.whouse as whouse

def short_dist_solver(sku_pick, whouse):
    node_pick = pickseq.sku_to_node_pick(sku_pick, whouse.slots(), whouse.start_node_id)
    # Calcule la distance entre le start_node et tous les autres noeuds
    # Ajoute le noeud à la pickseq
    # Ajoute la distance à la obj value

    # Calculer la distance entre le noeud précédent et tous les autres noeuds
    # Ajoute le noeud à la pickseq
    # Ajoute la distance à la obj value
    # Répéter pour tous les noeuds



    

    # 



graph = [
    [0, inf, inf, -3],
    [inf, 0, inf, 8],
    [inf, 4, 0, -2],
    [5, inf, 3, 0]
]

print(floyd_warshall(graph))


