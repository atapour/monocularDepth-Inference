echo "downloading pretrained models..."

mkdir -p ./checkpoints

MODELS=./checkpoints/checkpoints.zip
URL_MODELS=https://collections.durham.ac.uk/downloads/r2rf55z770q

echo "downloading the style transfer and depth estimation models..."

wget --quiet --no-check-certificate --show-progress $URL_MODELS -O $MODELS

echo "checking the MD5 checksum for downloaded models..."

cd checkpoints

CHECK_SUM_CHECKPOINTS='b176b00450ce9aaf3ef812087ed3ef49  checkpoints.zip'

echo $CHECK_SUM_CHECKPOINTS | md5sum -c

echo "Unpacking the zip file..."

unzip -q checkpoints.zip && rm checkpoints.zip && rm README.txt

echo "All Done!!"

