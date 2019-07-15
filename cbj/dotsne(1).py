from sklearn.manifold import TSNE
import csv
from datetime import datetime
start = datetime.now()

outfile = open("oregonf_t_SNE.csv","w",newline="")
fw1=csv.writer(outfile)

# fo2=open("_vector.txt",'r',encoding="utf-8")
# fw=open("_node_x_y.txt",'w',encoding="utf-8")
fo2=open("oregonf.txt",'r',encoding="utf-8")
fw=open("oregonf_t_SNE.txt",'w',encoding="utf-8")
vec_list=[]
id=[]
line=fo2.readline()
while(True):
    line = fo2.readline()
    if not line:
        break
    else:
        term = line.strip().split("\t")
        arr = []
        for i in range(len(term)):
            if i!=0:
                arr.append(float(term[i]))
            else:
                id.append(term[i])
        vec_list.append(arr)
print("ok")

tsne=TSNE(metric='cosine',method='barnes_hut',angle=0.2,n_iter=2000)

data_tsne = tsne.fit_transform(vec_list)

fw1.writerow(["id","x","y"])
fw.write(str(len(data_tsne))+" 2 \n")
j=0
for line in data_tsne:
    fw.write(str(line[0])+" "+str(line[1])+"\n")
    fw1.writerow([str(id[j]),str(line[0]),str(line[1])])
    j=j+1
print("end!")
fw.close()

end = datetime.now()
print((end - start).seconds)
