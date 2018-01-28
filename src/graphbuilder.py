import math

from tqdm import tqdm
from igraph import Graph


class GraphBuilder:
    def __init__(self):
        self.graph = Graph()
        self.author_index = set()

    def _add_non_existent_node(self, author, topic):
        if author not in self.author_index:
            self.author_index.add(author)
            self.graph.add_vertex(author, label=topic)

    def extend_graph(self, df):
        for _, row in tqdm(df.iterrows()):
            author = row['by']
            topic = row['topic']
            self._add_non_existent_node(author, topic)
            parent = row['parent']
            if math.isnan(parent):
                continue
            parent_df = df[df['id'] == int(parent)]
            if len(parent_df) == 0:
                continue
            parent_author = parent_df.iloc[0]['by']
            parent_topic = parent_df.iloc[0]['topic']
            self._add_non_existent_node(parent_author, parent_topic)
            self.graph.add_edges([(author, parent_author)])