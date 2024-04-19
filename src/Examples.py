import TextPlaceholders as tph
    
def init_example() -> int:
    print('===== init_example =====')
    template = tph.TextPlaceholders('../res/template.dat')
    template.display_placeholders()
    print()
    return 0

def get_placeholder_indexes_example() -> int:
    print('===== get_placeholder_indexes_example =====')
    template = tph.TextPlaceholders('../res/template.dat')
    print(template.get_placeholder_indexes())
    print()
    return 0

def remove_placeholder_by_index_example() -> int:
    print('===== remove_placeholder_by_index_example =====')
    template = tph.TextPlaceholders('../res/template.dat')
    template.remove_placeholder_by_index(151)
    template.display_placeholders()
    print()
    return 0

def remove_placeholder_by_position_example() -> int:
    print('===== remove_placeholder_by_position_example =====')
    template = tph.TextPlaceholders('../res/template.dat')
    template.remove_placeholder_by_position(1)
    template.display_placeholders()
    print()
    return 0

def remove_placeholder_by_name_example() -> int:
    print('===== remove_placeholder_by_name_example =====')
    template = tph.TextPlaceholders('../res/template.dat')
    template.remove_placeholder_by_name('zip')
    template.display_placeholders()
    print()
    return 0

if(__name__ == '__main__'):
    init_example()
    get_placeholder_indexes_example()
    remove_placeholder_by_index_example()
    remove_placeholder_by_position_example()
    remove_placeholder_by_name_example()