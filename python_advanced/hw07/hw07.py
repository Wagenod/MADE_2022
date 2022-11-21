import json, csv, os


class BaseReader:
    def read(self, fileobj):
        pass


class BaseWriter:
    def dump(data, fileobj):
        pass

# txt

class TxtReader(BaseReader):
    def read(self, fileobj):
        return fileobj.read()


class TxtWriter(BaseWriter):
    def dump(self, data, fileobj):
        fileobj.write(data)


# json

# csv

# использование
def read_data(fileobj, reader: BaseReader):
    return reader.read(fileobj)

def dump_data(data, fileobj, writer: BaseWriter):
    writer.dump(data, fileobj)

ROOT_DIR = r"python_advanced\\hw07"

with open(os.path.join(ROOT_DIR, "1.txt")) as f:
    print(read_data(f, TxtReader()))

with open(os.path.join(ROOT_DIR, "2.txt"), 'w') as f:
    dump_data("dump", f, TxtWriter())
# dump_data({"x": "1"}, fileobj, writer=JsonWriter())  # в fileobj записывается json {"x": "1"}

# data = read_data(fileobj, reader=JsonReader())
# assert data == {"x": "1"}