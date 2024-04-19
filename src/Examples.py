import TextPlaceholders as tph
    
def init_example() -> int:
    template = tph.TextPlaceholders('../res/template.dat')
    template.display_placeholders()
    return 0

def remove_placeholder_by_index_example() -> int:
    template = tph.TextPlaceholders('../res/template.dat')
    template.remove_placeholder_by_index(151)
    template.display_placeholders()
    return 0

def remove_placeholder_by_position_example() -> int:
    template = tph.TextPlaceholders('../res/template.dat')
    template.remove_placeholder_by_position(1)
    template.display_placeholders()
    return 0

def remove_placeholder_by_name_example() -> int:
    template = tph.TextPlaceholders('../res/template.dat')
    template.remove_placeholder_by_name('zip')
    template.display_placeholders()
    return 0

if(__name__ == '__main__'):
    init_example()
    remove_placeholder_by_index_example()
    remove_placeholder_by_position_example()
    remove_placeholder_by_name_example()