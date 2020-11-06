import nltk
from tqdm import tqdm
import json,re

def sentence_slid_window(sent,length,bag):
	toks=nltk.word_tokenize(sent)
	pos=nltk.pos_tag(toks)

	for i in range(len(toks)-length+1):
		# if (pos[i][1] in ["TO", "IN","VBP",'PRP','VBD','MD']
		# 	or pos[i+length-1][1] in ["TO", "IN","VBP",'PRP','VBD','MD']):
		# 	# print(pos[i],pos[i+length-1])
		# 	continue

		term_pos=" ".join([p for w,p in pos[i:i+length]])
		# print(term_pos)
		res=re.match(r"(JJ )*(NN )*NN$",term_pos)

		if res:
			term=toks[i:i+length]
			key=" ".join(term)
			# if re.match(r"[\w\d\s-]+$",s):
			if key in bag:
				bag[key]+=1
			else:
				bag[key]=1


def clean_term(bag):
	keys=[]
	for k,v in bag.items():
		if v<2:
			keys.append(k)

	for k in keys:
		bag.pop(k)
	# pass

INPUT="/home/zack/pubmed/huangfu/pubmedCorpus"
OUTPUT="term.json"
interval=1000
total=100000

bag_2={}
bag_3={}
bag_4={}
bag_5={}
with open(INPUT,"r") as f:
	for i,l in tqdm(enumerate(f)):
		l=l.lower().strip()
		doc=nltk.sent_tokenize(l) 
		for s in doc:
			sentence_slid_window(s,2,bag_2)
			sentence_slid_window(s,3,bag_3)
			sentence_slid_window(s,4,bag_4)
			sentence_slid_window(s,5,bag_5)
		if i%interval==0:
			print(len(bag_2),len(bag_3),len(bag_4),len(bag_5))
			# clean_term(bag_2)
			# clean_term(bag_3)
			# clean_term(bag_4)
			# clean_term(bag_5)
		if i>total:
			break

clean_term(bag_2)
clean_term(bag_3)
clean_term(bag_4)
clean_term(bag_5)

res={"2":bag_2,"3":bag_3,"4":bag_4,"5":bag_5}

with open(OUTPUT,"w") as f:
	json.dump(res,f)


# s="I have a big apple."
# c=detector(s,2)
# print(c)
