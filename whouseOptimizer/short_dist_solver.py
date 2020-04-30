import whouse_modules.pickseq as pickseq
import whouse_modules.whouse as whouse

dist_matrix1 = [[0, 20, 30, 40], [20, 0, 30, 5], [30, 30, 0, 10], [40, 5, 10, 0]]

def short_dist_solver(sku_pick, whouse, node_pick, start_node_id):
    node_pick = pickseq.sku_to_node_pick(sku_pick, whouse.slots(), whouse.start_node_id)
    dist_matrix = pickseq.create_dist_matrix(node_pick, start_node_id, whouse_graph())

    seq = []
    Z = 0
    #associer le node à la bonne liste dans la distance matrix
    for node in node_pick:
        for n, dist in enumerate(dist_matrix, 1):
            if node == n:
                Z = Z + min(dist_matrix[dist])
                seq.append(node)
        print(seq)
        print(Z)

    # Calcule la distance entre le start_node et tous les autres noeuds
    # Ajoute le noeud à la pickseq
    # Ajoute la distance à la obj value

    # Calculer la distance entre le noeud précédent et tous les autres noeuds
    # Ajoute le noeud à la pickseq
    # Ajoute la distance à la obj value
    # Répéter pour tous les noeuds



    

    # 




