import argparse
from pathlib import Path
import pandas as pd,matplotlib.pyplot as plt
def main(a):
 i=Path(a.input);o=Path(a.output);o.mkdir(parents=True,exist_ok=True)
 if (i/"history.csv").exists():
  d=pd.read_csv(i/"history.csv");fig,ax=plt.subplots();ax.plot(d.epoch,d.train_loss);ax.set(xlabel="Epoch",ylabel="Training loss");fig.savefig(o/"training_loss.png",dpi=600,bbox_inches="tight");plt.close(fig)
 if (i/"event_metrics.csv").exists():
  d=pd.read_csv(i/"event_metrics.csv");fig,ax=plt.subplots();ax.bar(d.event,d.flood_iou);ax.set_ylabel("Flood IoU");ax.tick_params(axis="x",rotation=45);fig.savefig(o/"event_flood_iou.png",dpi=600,bbox_inches="tight");plt.close(fig)
if __name__=="__main__":
 p=argparse.ArgumentParser();p.add_argument("--input",required=True);p.add_argument("--output",required=True);main(p.parse_args())
