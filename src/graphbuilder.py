from tqdm import tqdm
from igraph import Graph


class GraphBuilder:
    def __init__(self):
        self.graph = Graph()
        self.author_index = set()

    def _add_non_existent_node(self, author):
        if author not in self.author_index:
            self.author_index.add(author)
            self.graph.add_vertices(author)

    def extend_graph(self, df):
        for _, row in tqdm(df.iterrows()):
            author = row['by']
            self._add_non_existent_node(author)
            parent = row['parent']
            if not parent:
                continue
            parent_df = df[df['id'] == parent]
            if len(parent_df) == 0:
                continue
            parent_author = parent_df.iloc[0]['by']
            self._add_non_existent_node(parent_author)
            self.graph.add_edges([(author, parent_author)])
