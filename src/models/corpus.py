"""
Train a LDA model using mallet on the HackerNews data.
Adapted from https://rare-technologies.com/tutorial-on-mallet-in-python/
"""

import logging

from gensim import corpora, utils

logging.basicConfig(format="%(asctime)s : %(levelname)s : %(message)s", level=logging.INFO)


def iter_documents(documents):
    """Iterate over comments, yielding one document at a time."""
    for document in documents:
        # parse document into a list of utf8 tokens
        yield utils.simple_preprocess(document)


class HackernewsCorpus(object):
    def __init__(self, documents):
        """
        Initialize the HackerNews corpus
        :param documents: pd.Series of comments, titles, ...
        """
        self.documents = documents
        self.dictionary = corpora.Dictionary(iter_documents(documents))
        self.dictionary.filter_extremes()

    def __iter__(self):
        for tokens in iter_documents(self.documents):
            yield self.dictionary.doc2bow(tokens)
