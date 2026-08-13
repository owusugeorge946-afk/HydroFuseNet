import argparse,json
from pathlib import Path
import numpy as np,pandas as pd
from common import config
def main(a):
 c=config(a.config);events=sorted(pd.read_csv(a.manifest).event.unique());n=c["documented_event_counts"]
 if len(events)!=sum(n.values()):raise ValueError("Expected 28 events")
 rng=np.random.default_rng(c["training"]["seed"]);rng.shuffle(events);nt=n["train"];nv=n["validation"]
 s={"train":events[:nt],"validation":events[nt:nt+nv],"test":events[nt+nv:]};Path(a.output).write_text(json.dumps(s,indent=2))
 print(json.dumps(s,indent=2));print("WARNING: replace with original event identities if recovered.")
if __name__=="__main__":
 p=argparse.ArgumentParser();p.add_argument("--manifest",required=True);p.add_argument("--output",required=True);p.add_argument("--config",default="config/experiment_config.json");main(p.parse_args())
