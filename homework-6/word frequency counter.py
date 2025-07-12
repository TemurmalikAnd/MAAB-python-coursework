import string
from itertools import islice

def text_to_list():
    with open("sample.txt", 'r') as f:
        txt = f.read()
    text_no_punct = txt.translate(str.maketrans('', '', string.punctuation)) # removing punctuations
    words_clean = text_no_punct.lower().split()  # Convert to lowercase for case insensitivity
    d = dict.fromkeys(words_clean, 0)
    for val in words_clean:
        d[val] += 1
    sorted_val = {k: v for k, v in sorted(d.items(), key=lambda v: v[1], reverse=True)}
    top_dict = dict(islice(sorted_val.items(), 5))
    print(f"""Total words: {len(words_clean)}
Top 5 most common words:""")
    for key, value in top_dict.items():
        top_5 = f"{key} - {str(value)}"
        print(top_5)

    with open("word_count_report.txt", 'w') as r:
        r.write(f"Word Count Report\n")
        r.write(f"Total words: {len(words_clean)}\n")
        r.write("Top 5 words:\n")
        for key, value in top_dict.items():
            r.write(f"{key} - {value}\n")

text_to_list()