from collections import defaultdict

import networkx as nx

from trees.parse_tree import ParseTree


def extract_relation_ngrams(
        g: nx.DiGraph | ParseTree,
        relation_ngrams: list[tuple[int, int]]
):
    if not isinstance(g, nx.DiGraph):
        g = g.to_networkx()
    leaf_nodes = [node for node, data in g.nodes(data=True) if g.out_degree(node) == 0]
    paths_all = []
    root_node = [node for node, data in g.nodes(data=True) if g.in_degree(node) == 0][0]
    for leaf_node in leaf_nodes:
        paths = nx.all_simple_paths(g, root_node, leaf_node)
        paths_all.extend(paths)
    relevant_paths = {}
    for start, end in relation_ngrams:
        for l in range(start, end + 1):
            if l not in relevant_paths:
                relevant_paths[l] = set()
            for path in paths_all:
                for i in range(len(path) - l + 1):
                    relevant_paths[l].append(path[i:i + l])
    relation_counts = {k: defaultdict(int) for k in relevant_paths.keys()}
    for l, paths in relevant_paths.items():
        for path in paths:
            ngram = tuple(g.nodes[node]['relation'] for node in path)
            relation_counts[l][ngram] += 1
    print(relevant_paths)


def extract_metrics(
        g: nx.DiGraph | ParseTree,
        relation_ngrams: list[tuple[int, int]] = None
) -> dict:
    if not isinstance(g, nx.DiGraph):
        g = g.to_networkx()
    depth = nx.dag_longest_path_length(g)
    concept_counts = defaultdict(int)
    relation_counts = defaultdict(int)
    for node, data in g.nodes(data=True):
        concept = data['concept']
        concept_counts[concept] += 1

        relation = data['relation']
        relation_counts[relation] += 1

    return {
        'depth': depth,
        'concept_counts': dict(concept_counts),
        'relation_counts': dict(relation_counts)
    }
