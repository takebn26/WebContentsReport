import matplotlib.pyplot as plt
import networkx as nx

G = nx.DiGraph()

G.add_nodes_from([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
G.add_edges_from([
	(2, 1), (3, 1), (4, 1),
	(5, 1), (2, 4), (3, 8),
	(3, 6), (4, 9), (5, 4),
	(6, 4), (6, 10), (7, 9),
	(7, 10), (7, 4),
	(8, 6), (8, 2)
])

# pagerank計算 ランダムサーフ率デフォルト0.85
mapping_pr = nx.pagerank(G)

# label付け替え 小数点4位以下切り捨て
mapping_pr = { k:"[%s] %s" % (k, round(v, 4)) for (k, v) in mapping_pr.items() }
G = nx.relabel_nodes(G, mapping_pr)

# 表示整形
pos = nx.spring_layout(G, k=0.3)
nx.draw_networkx_nodes(G, pos, node_color='pink', alpha=0.6, node_size=2000)
nx.draw_networkx_labels(G, pos, fontsize=14, font_weight="bold")
nx.draw_networkx_edges(G, pos, alpha=0.4, edge_color='C')

plt.axis('off')
plt.savefig("./images/pr_report02.png")
plt.show()
