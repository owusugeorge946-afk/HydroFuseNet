import torch
from torch import nn
from common import MODALITIES
class B(nn.Module):
 def __init__(self,a,b):super().__init__();self.n=nn.Sequential(nn.Conv2d(a,b,3,padding=1,bias=False),nn.BatchNorm2d(b),nn.ReLU(),nn.Conv2d(b,b,3,padding=1,bias=False),nn.BatchNorm2d(b),nn.ReLU())
 def forward(self,x):return self.n(x)
class E(nn.Module):
 def __init__(self,c,b):super().__init__();self.a=B(c,b);self.z=B(b,b*2);self.p=nn.MaxPool2d(2)
 def forward(self,x):a=self.a(x);return a,self.z(self.p(a))
class HydroFuseNet(nn.Module):
 def __init__(self,ch,base=32,nclass=3,enabled=None):
  super().__init__();self.enabled=enabled or MODALITIES;self.e=nn.ModuleDict({m:E(ch[m],base) for m in self.enabled});n=len(self.enabled);self.f=B(base*2*n,base*4);self.u=nn.ConvTranspose2d(base*4,base*2,2,2);self.d=B(base*2+base*n,base*2);self.h=nn.Conv2d(base*2,nclass,1)
 def forward(self,x):
  lo=[];hi=[]
  for m in self.enabled:a,b=self.e[m](x[m]);lo.append(a);hi.append(b)
  return self.h(self.d(torch.cat([self.u(self.f(torch.cat(hi,1)))]+lo,1)))
