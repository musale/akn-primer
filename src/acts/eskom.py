from src.acts import Act


def main():
    Act.validate('ext/akomantoso30.xsd', 'ext/eskom_act13_of2001.xml')


if __name__ == '__main__':
    main()
