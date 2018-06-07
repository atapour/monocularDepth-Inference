import torch
import os

#This script is hastily written to remove the running stats (mean and var) from the instanceNorm layers in netG_A2B checkpint since pytorch 4 does not keep these anymore. Thus, this should only be run if and only if you are using pyTorch 4.

ckeckpoint_name = './checkpoints/netG_A2B.pth' #path and name of the chekcpoint we intend to remove the stats from

checkpoint_in = torch.load(ckeckpoint_name)
ckeckpoint_out = {}

print('removing running means and variances from %s.' % ckeckpoint_name)
for key in checkpoint_in.keys():
    if 'model' in key and not 'running' in key: 
        ckeckpoint_out[key] = checkpoint_in[key]
torch.save(ckeckpoint_out,ckeckpoint_name)
print('checkoint %s has now been overwritten.' % ckeckpoint_name)
