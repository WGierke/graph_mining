import sys
sys.path.append('..')
sys.path.append('.')

import logging

from corpus import HackernewsCorpus
from gensim import utils, models
from src.data.load_data import get_hackernews_files, load_hackernews_dataframe

logging.basicConfig(format="%(asctime)s : %(levelname)s : %(message)s", level=logging.INFO)


def training():
    # Load one HackerNews DataFrame
    files = get_hackernews_files()
    df = load_hackernews_dataframe(files[-1])

    # Focus on the stories
    comments_df = df[df.type == "comment"]
    comments_df = comments_df.dropna(subset=['text'])
    comments = comments_df['text']

    # Set up the streamed corpus
    corpus = HackernewsCorpus(comments)

    # Train 10 LDA topics using MALLET
    mallet_path = '/home/madness/Programs/mallet-2.0.6/bin/mallet'
    model = models.wrappers.LdaMallet(mallet_path, corpus, num_topics=10, id2word=corpus.dictionary)
    # 0	5	don data service doesn problem security system access bitcoin case network internet information phone account gt services key number
    # 1	5	google web open app source windows don facebook content pretty support game apple users apps site page free works
    # 2	5	code language pre data type write run system python languages js performance programming function memory simple java tools api
    # 3	5	https href rel nofollow www http org news github en wiki wikipedia amp html id ycombinator item blog youtube
    # 4	5	people don person world social law government women fact china bad society country state evidence opinion legal political situation
    # 5	5	quot gt don point doesn read understand article isn question true comment wrong make sense thing idea answer makes
    # 6	5	problem power space human change long point world system ai high large energy scale current speed problems isn low
    # 7	5	work company good software time working experience job product full tech make great team people jobs companies business end
    # 8	5	time don ve years things people good day back thing didn lot ll long bad feel days life ago
    # 9	5	money pay market cost people year buy car price high big live companies costs business worth cars area make

    # <1000> LL/token: -8.76975

    # Note how topic 2 is about programming, 3 represents parts of links, 4 is about social and political stuff,
    # 7 is about problems and 9 about businesses and money

    # Now use the trained model to infer topics on a new document
    doc = "Deep Learning is great"
    bow = corpus.dictionary.doc2bow(utils.simple_preprocess(doc))
    print(model[bow])  # print list of (topic id, topic weight) pairs
    #[(7, 0.12788259958071282), (6, 0.10691823899371071), (1, 0.10062893081761008), (8, 0.09853249475890986),
    # (9, 0.09433962264150945), (5, 0.09433962264150945), (4, 0.09433962264150945), (3, 0.09433962264150945),
    # (2, 0.09433962264150945), (0, 0.09433962264150945)]


if __name__ == '__main__':
    training()
