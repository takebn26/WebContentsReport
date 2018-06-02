import matplotlib.pyplot as plt
import networkx as nx

G = nx.DiGraph()

# node作成 edge作成
G.add_nodes_from([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
G.add_edges_from([
	(2, 1), (3, 1), (4, 1),
	(5, 1), (6, 1), (7, 1),
	(8, 1), (9, 1), (10, 1),
	(11, 1), (12, 1), (2, 10)
])

# pagerank計算 ランダムサーフ率0.15
mapping_pr = nx.pagerank(G, alpha=0.85)

# label付け替え 小数点4位以下切り上げ
mapping_arranged_pr = { k:"[%s] %s" % (k, round(v, 4)) for (k, v) in mapping_pr.items() }
G = nx.relabel_nodes(G, mapping_arranged_pr)

# 表示整形
pos = nx.spring_layout(G, k=0.3)
nx.draw_networkx_nodes(G, pos, node_color='pink', alpha=0.6, node_size=500)
nx.draw_networkx_labels(G, pos, fontsize=14, font_weight="bold", alpha=0.1)
nx.draw_networkx_edges(G, pos, alpha=0.4, edge_color='C', width=2.0)

plt.axis('off')
plt.savefig("./images/pr_report03.png")
plt.show()
