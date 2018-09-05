import unittest
from src.acts import Act


class TestAct(unittest.TestCase):
    """Test acts."""

    def setUp(self):
        self.xsd_schema_path = 'ext/akomantoso30.xsd'
        self.act_xml_path = 'ext/eskom_act13_of2001.akn'

    def test_valid_act(self):
        """Check if an act is akomantoso 3.0 compliant."""
        self.assertTrue(
            Act.validate(xsd_schema_path=self.xsd_schema_path,
                         xml_doc_path=self.act_xml_path))


if __name__ == '__main__':
    Act.validate('ext/akomantoso30.xsd', 'ext/eskom_act13_of2001.akn')
