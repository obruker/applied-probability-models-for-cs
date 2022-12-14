import sys
from collections import Counter


def read_articles_file(filename):
    with open(dev_filename, "r") as f:
        content = f.read()
        lines = [l for l in content.split("\n") if l]
        i = 0
        while i < len(lines):
            header = lines[i]
            if header[0] != "<" or header[-1] != ">":
                raise Exception("header line expected to start with '<' and end with '>'")
            header = header[1:-1]
            _, id, *classes = header.split()
            article = lines[i + 1]
            i += 2
            yield id, classes, article


def concat_articles(articles_data):
    return "\n".join(
        [article for _, _, article in articles_data]
    )


def split_words(words, ratio):
    train_size = round(len(words) * ratio)
    return words[:train_size], words[train_size:]


if __name__ == "__main__":
    args = sys.argv[1:]
    if len(args) != 4:
        raise Exception("""
        Expecting the following arguments:
        (1) development set filename
        (2) test set filename
        (3) INPUT WORD
        (4) output filenam
        """)

    dev_filename, test_filename, INPUT_WORD, out_filename = args
    vocabulary_size = 300000

    articles_data = read_articles_file(dev_filename)
    corpus = concat_articles(articles_data)
    all_words = corpus.split()

    train_set, validation_set = split_words(all_words, ratio=0.9)
    train_words_counter = Counter(train_set)

    outputs = [
        dev_filename,
        test_filename,
        INPUT_WORD,
        out_filename,
        vocabulary_size,
        1 / vocabulary_size,
        len(all_words),
        len(validation_set),
        len(train_set),
        len(train_words_counter.keys()),
        train_words_counter[INPUT_WORD],
    ]

    with open(out_filename, "w") as f:
        for i, line in enumerate(outputs):
            f.write(f"Output{i + 1}: {line}\n")
