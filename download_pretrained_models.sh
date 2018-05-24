echo "downloading pretrained models..."

mkdir -p ./checkpoints
MODEL_A2B=./checkpoints/netG_A2B.pth
URL_A2B=https://www.dropbox.com/s/zg2txeh8u2crspd/netG_A2B.pth

MODEL_B2C=./checkpoints/netG_B2C.pth
URL_B2C=https://www.dropbox.com/s/jzo0zf0dp17x6ig/netG_B2C.pth

MODELS=./checkpoints/checkpoints.zip
URL_MODELS=https://collections.durham.ac.uk/single_use_link/show/b83f95631a515561056ee69445f9c94003b1e1986df584caed035263d610e3f6

echo "downloading the style transfer model"

wget --quiet --show-progress $URL_A2B -O $MODEL_A2B

echo "downloading the depth estimation model"

wget --quiet --show-progress $URL_B2C -O $MODEL_B2C

echo "downloading the style transfer and depth estimation models..."

wget --quiet --show-progress $URL_MODELS -O $MODELS

echo "checking MD5 checksum for downloaded models..."

cd checkpoints

CHECK_SUM_A2B='988541ba8fb6c355cac40a0099f81adc  netG_A2B.pth'
CHECK_SUM_B2C='ac637db112f358566f071e2bbfd57675  netG_B2C.pth'
CHECK_SUM_CHECKPOINTS='ea88bd783fc5b25a0a50fc18d25b2a3e  checkpoints.zip'

echo $CHECK_SUM_A2B | md5sum -c
echo $CHECK_SUM_B2C | md5sum -c
echo $CHECK_SUM_CHECKPOINTS | md5sum -c

echo "Unpacking the zip file..."

unzip checkpoints.zip && rm checkpoints.zip
