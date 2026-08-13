import argparse
from pathlib import Path
import numpy as np,pandas as pd
from common import config
def norm(a,valid):
 a=np.asarray(a,dtype="float32")
 if a.ndim==2:a=a[...,None]
 o=np.zeros_like(a)
 for c in range(a.shape[-1]):
  v=a[...,c][valid & np.isfinite(a[...,c])]
  if v.size:
   lo,hi=np.percentile(v,[2,98])
   if hi>lo:o[...,c]=np.clip((a[...,c]-lo)/(hi-lo),0,1)
 return o
def main(a):
 c=config(a.config);ps,st=c["patch_size"],c["stride"];out=Path(a.output);out.mkdir(parents=True,exist_ok=True);rows=[]
 for d in sorted(Path(a.input).iterdir()):
  if not d.is_dir() or not all((d/f).exists() for f in ["pre_sar.npy","post_sar.npy","optical.npy","dem.npy","label.npy"]):continue
  lab=np.load(d/"label.npy");valid=np.load(d/"valid.npy").astype(bool) if (d/"valid.npy").exists() else np.isfinite(lab)
  pre=norm(np.load(d/"pre_sar.npy"),valid);post=norm(np.load(d/"post_sar.npy"),valid);opt=norm(np.load(d/"optical.npy"),valid);dem=norm(np.load(d/"dem.npy"),valid)
  H,W=lab.shape
  for y in range(0,H-ps+1,st):
   for x in range(0,W-ps+1,st):
    if not valid[y:y+ps,x:x+ps].all():continue
    f=out/f"{d.name}_y{y}_x{x}.npz";np.savez_compressed(f,pre_sar=pre[y:y+ps,x:x+ps],post_sar=post[y:y+ps,x:x+ps],optical=opt[y:y+ps,x:x+ps],dem=dem[y:y+ps,x:x+ps],label=lab[y:y+ps,x:x+ps].astype("uint8"));rows.append({"event":d.name,"path":str(f)})
 pd.DataFrame(rows).to_csv(out/"manifest.csv",index=False);print("patches",len(rows))
if __name__=="__main__":
 p=argparse.ArgumentParser();p.add_argument("--input",required=True);p.add_argument("--output",required=True);p.add_argument("--config",default="config/experiment_config.json");main(p.parse_args())
