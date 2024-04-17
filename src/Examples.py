import TextPlaceholders as tph
    
def main():
    template = tph.TextPlaceholders('../res/template.dat')
    print('Indexes:', template.get_placeholder_indexes())
    template.display_placeholders()
    return 0

if(__name__ == '__main__'):
    main()