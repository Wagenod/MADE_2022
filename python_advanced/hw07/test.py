import unittest
import io
import python_advanced.hw07.hw07 as utils


class TestTXT(unittest.TestCase):
    def setUp(self) -> None:
        self.io_stream = io.StringIO()

    def test_read_write(self) -> None:
        txt_data = "Hello world!\nKitty"
        utils.dump_data(txt_data, self.io_stream, utils.TxtWriter())
        saved_to_stream = self.io_stream.getvalue()
        self.io_stream.seek(0)
        self.assertEqual(saved_to_stream,
                         utils.read_data(self.io_stream, utils.TxtReader()))


class TestJSON(unittest.TestCase):
    def setUp(self) -> None:
        self.io_stream = io.StringIO()

    def test_read_write(self) -> None:
        json_data = {
            "name": "sathiyajith",
            "rollno": "56",
            "cgpa": "8.6",
            "phonenumber": "9976770500"
        }

        json_data_repr = '{"name": "sathiyajith", "rollno": "56", \
                           "cgpa": "8.6", "phonenumber": "9976770500"}'

        utils.dump_data(json_data, self.io_stream, utils.JSONWriter())
        self.assertEqual(json_data_repr, self.io_stream.getvalue())
        self.io_stream.seek(0)
        self.assertDictEqual(json_data,
                             utils.read_data(self.io_stream, utils.JSONReader()))


class TestCSV(unittest.TestCase):
    def setUp(self) -> None:
        self.io_stream = io.StringIO()

    def test_read_write(self):
        csv_data = [["NAME", "JOB", "BIRTHDATE"],
                    ["Виктор", "Токарь", "1995"],
                    ["Сергей", "Сварщик", "1983"]]

        csv_data_repr = """NAME,JOB,BIRTHDATE\n
                           Виктор,Токарь,1995\n
                           Сергей,Сварщик,1983\n
                        """
        utils.dump_data(csv_data, self.io_stream, utils.CSVWriter())
        self.assertEqual(csv_data_repr, self.io_stream.getvalue())
        self.io_stream.seek(0)
        self.assertListEqual(csv_data,
                             utils.read_data(self.io_stream, utils.CSVReader()))


class TestBatchGenerator(unittest.TestCase):
    io_stream = io.StringIO("cat dog rabbit\n" \
                        "yellow red blue\n" \
                        "minsk vitebsk moscow\n" \
                        "rabbit house sun flower\n" \
                        "cat1 dog1 rabbit1\n" \
                        "yellow1 red1 blue1\n" \
                        "minsk1 vitebsk1 moscow1\n" \
                        "rabbit1 house1 sun1 flower1\n" \
                        "cat2 dog2 rabbit2\n" \
                        "yellow2 red2 blue2\n" \
                        "minsk2 vitebsk2 moscow2\n" \
                        "rabbit2 house2 sun2 flower2\n" \
                        "cat3 dog3 rabbit3\n" \
                        "yellow3 red3 blue3\n" \
                        "minsk3 vitebsk3 moscow3\nr" \
                        "abbit3 house3 sun3 flower3\n" \
                        "cat4 dog4 rabbit4\n" \
                        "yellow4 red4 blue4\n")

    def test_batch_gen(self):
        self.assertListEqual(next(utils.read_batch(self.io_stream)), 
                            ['cat dog rabbit', 'yellow red blue', 
                            'minsk vitebsk moscow', 'rabbit house sun flower', 
                            'cat1 dog1 rabbit1'])

    def test_batch_filter(self):
        self.assertListEqual(utils.filter_big_file(self.io_stream, ["cat", "cat1", "cat2"]),
                            ['cat dog rabbit', 'cat1 dog1 rabbit1', 'cat2 dog2 rabbit2'])

if __name__ == "__main__":
    unittest.main()
