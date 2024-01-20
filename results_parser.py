from Bio import SearchIO
import numpy as np
import datetime
from scipy.stats import gmean

hit_max = []
score_max = 0
candi_scores  = []
id = ''
for one_record in SearchIO.parse('tmp.hhr', 'hhsuite3-text'):
    id=one_record.id
    for hit in one_record.hits:
        if hit.score >= score_max:
            score_max = hit.score
            hit_max = [hit.id, hit.evalue, hit.score]
        if hit.evalue < 1.e-5:
            candi_scores.append(hit.score)
timestamp = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
fhOut = open("hhr_parse"+timestamp+".out", "w")
fhOut.write("query_id,hit_max,best_evalue,score_max,score_mean,score_std,score_gmean\n")
mean=format(np.mean(candi_scores), ".2f")
std=format(np.std(candi_scores), ".2f")
g_mean=format(gmean(candi_scores), ".2f")

fhOut.write(f"{id},{hit_max[0]},{hit_max[1]},{hit_max[2]},{mean},{std},{g_mean}\n")
fhOut.close()
