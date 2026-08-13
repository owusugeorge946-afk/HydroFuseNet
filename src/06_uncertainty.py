import argparse,numpy as np,pandas as pd
def main(a):
 z=np.load(a.predictions,allow_pickle=True);r=[]
 for p,y,e in zip(z["probs"],z["labels"],z["events"]):
  p=np.asarray(p,float);y=np.asarray(y);pred=p.argmax(0);u=1-p.max(0);ok=pred==y;r.append({"event":str(e),"cs":u[ok].sum(),"cn":ok.sum(),"is":u[~ok].sum(),"in":(~ok).sum()})
 d=pd.DataFrame(r).groupby("event").sum();d["mean_uncertainty_correct"]=d.cs/d.cn.clip(lower=1);d["mean_uncertainty_incorrect"]=d["is"]/d["in"].clip(lower=1);d[["mean_uncertainty_correct","mean_uncertainty_incorrect"]].to_csv(a.output)
if __name__=="__main__":
 p=argparse.ArgumentParser();p.add_argument("--predictions",required=True);p.add_argument("--output",required=True);main(p.parse_args())
