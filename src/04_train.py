import argparse,json
from pathlib import Path
import numpy as np,pandas as pd,torch
from torch.utils.data import DataLoader
from common import *
from importlib.machinery import SourceFileLoader
M=SourceFileLoader("M",str(Path(__file__).with_name("03_hydrofusenet_model.py"))).load_module()
def val(model,loader,dev):
 cm=np.zeros((3,3),int);model.eval()
 with torch.no_grad():
  for x,y,_ in loader:
   x={k:v.to(dev) for k,v in x.items()};p=model(x).argmax(1).cpu().numpy()
   for yy,pp in zip(y.numpy(),p):update(cm,yy,pp)
 return metrics(cm)
def main(a):
 c=config(a.config);seed_all(c["training"]["seed"]);s=json.loads(Path(a.splits).read_text());df=pd.read_csv(a.manifest);enabled=a.enabled.split(",") if a.enabled else MODALITIES
 tr=PatchDataset(df[df.event.isin(s["train"])],enabled);va=PatchDataset(df[df.event.isin(s["validation"])],enabled);sample=tr[0][0];ch={k:v.shape[0] for k,v in sample.items()}
 dev=torch.device("cuda" if torch.cuda.is_available() else "cpu");model=M.HydroFuseNet(ch,c["model"]["base_channels"],3,enabled).to(dev);print("parameters",sum(p.numel() for p in model.parameters()))
 opt=torch.optim.AdamW(model.parameters(),lr=c["learning_rate"],weight_decay=c["training"]["weight_decay"]);lossfn=torch.nn.CrossEntropyLoss(weight=torch.tensor(c["training"]["class_weights"],dtype=torch.float32,device=dev))
 tl=DataLoader(tr,batch_size=c["training"]["batch_size"],shuffle=True);vl=DataLoader(va,batch_size=c["training"]["batch_size"]);out=Path(a.output);out.mkdir(parents=True,exist_ok=True);hist=[];best=-1
 for ep in range(1,c["max_epochs"]+1):
  model.train();tot=0;n=0;valid=True
  for x,y,_ in tl:
   x={k:v.to(dev) for k,v in x.items()};y=y.to(dev);opt.zero_grad();loss=lossfn(model(x),y)
   if not torch.isfinite(loss):valid=False;break
   loss.backward();opt.step();tot+=loss.item();n+=1
  if not valid:hist.append({"epoch":ep,"valid":False});continue
  m=val(model,vl,dev);r={"epoch":ep,"train_loss":tot/max(n,1),"val_miou":m["miou"],"flood_iou":m["iou"][2],"flood_f1":m["f1"][2],"valid":True};hist.append(r);pd.DataFrame(hist).to_csv(out/"history.csv",index=False)
  if m["iou"][2]>best:best=m["iou"][2];torch.save({"model":model.state_dict(),"channels":ch,"enabled":enabled,"config":c},out/"best.pt")
if __name__=="__main__":
 p=argparse.ArgumentParser();p.add_argument("--manifest",required=True);p.add_argument("--splits",required=True);p.add_argument("--output",required=True);p.add_argument("--enabled");p.add_argument("--config",default="config/experiment_config.json");main(p.parse_args())
