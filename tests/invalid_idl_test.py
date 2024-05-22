import traceback
import unittest
from idl_parser import parser
from idl_parser.exception import IDLParserException

idl_path = 'idls/invalid_idl.idl'


class InvalidIDLTestFunctions(unittest.TestCase):
    def setUp(self):
        pass

    def test_invalid_message(self):
        parser_ = parser.IDLParser()
        try:
            with open(idl_path, 'r') as idlf:
                parser_.load(idlf.read(), filepath=idl_path)
        except IDLParserException as ex:
            self.assertEqual(ex.line_number, 10)

        except Exception as ex:
            traceback.print_exc()
            raise ex


if __name__ == '__main__':
    unittest.main()


def suite():
    suite = unittest.TestSuite()
    suite.addTests(unittest.makeSuite(InvalidIDLTestFunctions))
    return suite
