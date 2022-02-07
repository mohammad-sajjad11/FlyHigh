
if [ ! -d "stubs" ]; then
  mkdir -p "stubs"
else
  rm -rf ./stubs/*pb2*.py
fi
touch stubs/__init__.py
cd ./protos

python -m grpc_tools.protoc \
        -I ./ \
        --python_out=../ \
        --grpc_python_out=../ \
        stubs/*.proto

cd ..

mkdir -p ./flights/stubs
mkdir -p ./passengers/stubs
mkdir -p ./tickets/stubs

rm -rf ./flights/stubs/*_pb2*.py
rm -rf ./passengers/stubs/*_pb2*.py
rm -rf ./tickets/stubs/*_pb2*.py

cp -r ./stubs/*.py ./flights/stubs
cp -r ./stubs/*.py ./passengers/stubs
cp -r ./stubs/*.py ./tickets/stubs

