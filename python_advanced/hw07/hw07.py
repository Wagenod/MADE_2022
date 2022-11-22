import json


class BaseReader:
    def read(self, fileobj):
        pass


class BaseWriter:
    def dump(self, data, fileobj):
        pass


class TxtReader(BaseReader):
    def read(self, fileobj):
        return fileobj.read()


class TxtWriter(BaseWriter):
    def dump(self, data, fileobj):
        fileobj.write(data)


class JSONReader(BaseReader):
    def read(self, fileobj):
        return json.load(fileobj)


class JSONWriter(BaseReader):
    def dump(self, data, fileobj):
        json.dump(data, fileobj)


class CSVWriter(BaseWriter):
    def dump(self, data, fileobj):
        fileobj.writelines([",".join(list(map(str, row))) + "\n" for row in data])


class CSVReader(BaseReader):
    def read(self, fileobj):
        return [line.strip().split(",") for line in fileobj.readlines()]


# использование
def read_data(fileobj, reader: BaseReader):
    return reader.read(fileobj)


def dump_data(data, fileobj, writer: BaseWriter):
    writer.dump(data, fileobj)


def read_batch(fileobj, batchsize=5):
    data = []
    line = fileobj.readline()
    while line:
        if len(data) == batchsize:
            yield data
            data = []
        data.append(line.strip())
        line = fileobj.readline()
    
def filter_big_file(fileobj, search_words=None, **args):
    if not isinstance(search_words, list) and search_words is not None:
        raise TypeError
    founded_lines = []
    for batch in read_batch(fileobj, **args):
        for line in batch:
            if (search_words is None) or (set(search_words) & set(line.split(" "))):
                founded_lines.append(line)            
    return founded_lines


if __name__ == "__main__":
    with open(r"python_advanced\\hw07\\bigfile.txt") as f:
        #print(filter_big_file(f, ["cat", "cat1", "cat2"]))
        #print(filter_big_file(f))
        print(next(read_batch(f)))
    