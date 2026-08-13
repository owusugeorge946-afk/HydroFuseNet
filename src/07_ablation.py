import argparse,subprocess,sys
from pathlib import Path
from common import MODALITIES
def main(a):
 out=Path(a.output);out.mkdir(parents=True,exist_ok=True);train=Path(__file__).with_name("04_train.py")
 for name,en in [("full_model",MODALITIES)]+[(f"no_{m}",[x for x in MODALITIES if x!=m]) for m in MODALITIES]:
  subprocess.run([sys.executable,str(train),"--manifest",a.manifest,"--splits",a.splits,"--output",str(out/name),"--config",a.config,"--enabled",",".join(en)],check=True)
if __name__=="__main__":
 p=argparse.ArgumentParser();p.add_argument("--manifest",required=True);p.add_argument("--splits",required=True);p.add_argument("--output",required=True);p.add_argument("--config",default="config/experiment_config.json");main(p.parse_args())
