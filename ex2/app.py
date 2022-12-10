import sys

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

    dev_filename, test_filename, word, out_filename = args
    vocabulary_size = 300000
    outputs = [
        dev_filename,
        test_filename,
        word,
        out_filename,
        vocabulary_size,
        1 / vocabulary_size,
    ]

    with open(out_filename, "w") as f:
        for i, line in enumerate(outputs):
            f.write(f"Output{i + 1}: {line}\n")
