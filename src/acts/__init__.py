from lxml import etree


class Act(object):
    """An act."""

    @staticmethod
    def validate(xsd_schema_path, xml_doc_path):
        """Checks if the akn file is akomantoso 3.0 compliant."""
        xsd_schema_doc = etree.parse(xsd_schema_path)
        xsd_schema = etree.XMLSchema(xsd_schema_doc)
        akn_xml_doc = etree.parse(xml_doc_path)
        try:
            xsd_schema.assertValid(akn_xml_doc)
            print(f'✔ Valid AKN file {xml_doc_path}')
            return True

        except etree.XMLSyntaxError as err:
            print(f'✘ {err}')
            return False

        except etree.DocumentInvalid as err:
            print(f'✘ {err}')
            return False
