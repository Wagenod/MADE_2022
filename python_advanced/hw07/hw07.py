import json, csv


class BaseReader:
    def read(self, fileobj):
        pass


class BaseWriter:
    def dump(data, fileobj):
        pass


class TxtReader(BaseReader):
    def read(self, fileobj):
        pass


class TxtWriter(BaseWriter):
    pass



# использование
def read_data(fileobj, reader: BaseReader):
    return reader.read(fileobj)

def dump_data(data, fileobj, writer: BaseWriter):
    writer.dump(data, fileobj)


dump_data({"x": "1"}, fileobj, writer=JsonWriter())  # в fileobj записывается json {"x": "1"}

data = read_data(fileobj, reader=JsonReader())
assert data == {"x": "1"}