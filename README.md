[TermInformer: unsupervised term mining and analysis in biomedical literature](https://link.springer.com/article/10.1007/s00521-020-05335-2)

[Dataset Link](https://drive.google.com/file/d/1Ov5B-jNCgFxodq4_0TdLtu-AJrqvvX4z/view?usp=sharing)

## dataset
term.10w: word vector from 10,000 pubmed abstracts

term.1w: word vector from 1,0000 pubmed abstracts

- short: single word vector
- long: phrase vector
  - *.npy: vectors
  - *.txt: vocabulary

term.json: all possible terms from the above corpus

10w.abstract.phrase.tokenize.txt: use term.json to re.replace("original text","terms") words to phrase

10w.abstract.phrase.txt: same as "10w.abstract.phrase.tokenize.txt" but without tokenization.

10w.abstract.palin.tokenize.txt: The original published abstract without any phrases replaced


