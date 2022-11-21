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

class JSONReader(BaseReader):
    def read(self, fileobj):
        return json.load(fileobj)

class JSONWriter(BaseReader):
    def dump(self, data, fileobj):
        json.dump(data, fileobj)
# csv

# использование
def read_data(fileobj, reader: BaseReader):
    return reader.read(fileobj)

def dump_data(data, fileobj, writer: BaseWriter):
    writer.dump(data, fileobj)

if __name__ == '__main__':
    ROOT_DIR = r"hw07\\files"
    txt_data = "dump to txt file"
    json_data = {
        "name": "sathiyajith",
        "rollno": 56,
        "cgpa": 8.6,
        "phonenumber": "9976770500"
    }

    with open(os.path.join(ROOT_DIR, "in.txt")) as f_in, \
         open(os.path.join(ROOT_DIR, "out.txt"), 'w') as f_out, \
         open(os.path.join(ROOT_DIR, "out.json"), "w") as f_json_out, \
         open(os.path.join(ROOT_DIR, "in.json")) as f_json_in:
        
        print(read_data(f_in, TxtReader()))
        dump_data(txt_data, f_out, TxtWriter())

        print(read_data(f_json_in, JSONReader()))
        dump_data(json_data, f_json_out, JSONWriter())
        

