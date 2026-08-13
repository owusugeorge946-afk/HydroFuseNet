from pathlib import Path
import json,random,numpy as np,torch
from torch.utils.data import Dataset
MODALITIES=["pre_sar","post_sar","sar_change","optical","dem"]
def config(p="config/experiment_config.json"): return json.loads(Path(p).read_text())
def seed_all(s):
 random.seed(s);np.random.seed(s);torch.manual_seed(s)
 if torch.cuda.is_available():torch.cuda.manual_seed_all(s)
def chw(a):
 a=np.asarray(a)
 if a.ndim==2:a=a[...,None]
 return np.moveaxis(a,-1,0).astype("float32")
class PatchDataset(Dataset):
 def __init__(self,df,enabled=None):self.df=df.reset_index(drop=True);self.enabled=set(enabled or MODALITIES)
 def __len__(self):return len(self.df)
 def __getitem__(self,i):
  z=np.load(self.df.loc[i,"path"]);pre=chw(z["pre_sar"]);post=chw(z["post_sar"])
  a={"pre_sar":pre,"post_sar":post,"sar_change":post-pre,"optical":chw(z["optical"]),"dem":chw(z["dem"])}
  return {k:torch.from_numpy(v) for k,v in a.items() if k in self.enabled},torch.from_numpy(z["label"].astype("int64")),str(self.df.loc[i,"event"])
def update(cm,y,p,n=3):
 y=np.asarray(y).ravel();p=np.asarray(p).ravel();ok=(y>=0)&(y<n);cm+=np.bincount(n*y[ok]+p[ok],minlength=n*n).reshape(n,n);return cm
def metrics(cm):
 cm=cm.astype(float);tp=np.diag(cm);fp=cm.sum(0)-tp;fn=cm.sum(1)-tp
 pr=np.divide(tp,tp+fp,out=np.zeros_like(tp),where=tp+fp>0);re=np.divide(tp,tp+fn,out=np.zeros_like(tp),where=tp+fn>0)
 f1=np.divide(2*pr*re,pr+re,out=np.zeros_like(tp),where=pr+re>0);iou=np.divide(tp,tp+fp+fn,out=np.zeros_like(tp),where=tp+fp+fn>0)
 return {"accuracy":tp.sum()/max(cm.sum(),1),"precision":pr,"recall":re,"f1":f1,"iou":iou,"miou":iou.mean(),"mean_f1":f1.mean()}
