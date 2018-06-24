'''This code was adopted from https://gist.github.com/nkt1546789/e9fc84579b9c8356f1e5 accessed on June 23, 2018'''


from scipy import sparse

def ww_matrix(corpus,tokenizer,window_size):
    vocabulary={}
    data=[]
    row=[]
    col=[]
    for sentence in corpus:
        sentence=sentence.strip()
        tokens=[token for token in tokenizer(sentence) if token!=u""]
        for pos,token in enumerate(tokens):
            i=vocabulary.setdefault(token,len(vocabulary))
            start=max(0,pos-window_size)
            end=min(len(tokens),pos+window_size+1)
            for pos2 in range(start,end):
                if pos2==pos: 
                    continue
                j=vocabulary.setdefault(tokens[pos2],len(vocabulary))
                data.append(1.); row.append(i); col.append(j);
    cooccurrence_matrix=sparse.coo_matrix((data,(row,col)))
    return vocabulary, cooccurrence_matrix
