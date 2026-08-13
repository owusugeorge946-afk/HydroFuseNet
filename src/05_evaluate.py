import argparse,json
from pathlib import Path
import numpy as np,pandas as pd,torch
from torch.utils.data import DataLoader
from common import *
from importlib.machinery import SourceFileLoader
M=SourceFileLoader("M",str(Path(__file__).with_name("03_hydrofusenet_model.py"))).load_module()
def main(a):
 df=pd.read_csv(a.manifest);s=json.loads(Path(a.splits).read_text());ck=torch.load(a.checkpoint,map_location="cpu");ds=PatchDataset(df[df.event.isin(s["test"])],ck["enabled"]);dev=torch.device("cuda" if torch.cuda.is_available() else "cpu");model=M.HydroFuseNet(ck["channels"],ck["config"]["model"]["base_channels"],3,ck["enabled"]).to(dev);model.load_state_dict(ck["model"]);model.eval();cm=np.zeros((3,3),int);ec={e:np.zeros((3,3),int) for e in s["test"]};P=[];Y=[];E=[]
 with torch.no_grad():
  for x,y,e in DataLoader(ds,batch_size=1):
   x={k:v.to(dev) for k,v in x.items()};pr=torch.softmax(model(x),1).cpu().numpy()[0];pred=pr.argmax(0);yy=y.numpy()[0];update(cm,yy,pred);update(ec[e[0]],yy,pred);P.append(pr.astype("float16"));Y.append(yy.astype("uint8"));E.append(e[0])
 out=Path(a.output);out.mkdir(parents=True,exist_ok=True);m=metrics(cm);pd.DataFrame([{"accuracy":m["accuracy"],"miou":m["miou"],"mean_f1":m["mean_f1"],"flood_iou":m["iou"][2],"flood_precision":m["precision"][2],"flood_recall":m["recall"][2],"flood_f1":m["f1"][2]}]).to_csv(out/"final_test_metrics.csv",index=False)
 rows=[]
 for e,z in ec.items():
  q=metrics(z);rows.append({"event":e,"accuracy":q["accuracy"],"miou":q["miou"],"flood_iou":q["iou"][2],"flood_precision":q["precision"][2],"flood_recall":q["recall"][2],"flood_f1":q["f1"][2]})
 pd.DataFrame(rows).to_csv(out/"event_metrics.csv",index=False);np.savez_compressed(out/"pixel_outputs.npz",probs=np.array(P,dtype=object),labels=np.array(Y,dtype=object),events=np.array(E))
if __name__=="__main__":
 p=argparse.ArgumentParser();p.add_argument("--manifest",required=True);p.add_argument("--splits",required=True);p.add_argument("--checkpoint",required=True);p.add_argument("--output",required=True);main(p.parse_args())
