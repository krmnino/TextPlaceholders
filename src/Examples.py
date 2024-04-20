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

def get_placeholder_positions_example() -> int:
    print('===== get_placeholder_positions_example =====')
    template = tph.TextPlaceholders('../res/template.dat')
    print(template.get_placeholder_positions())
    print()
    return 0

def get_placeholder_names_example() -> int:
    print('===== get_placeholder_names_example =====')
    template = tph.TextPlaceholders('../res/template.dat')
    print(template.get_placeholder_names())
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

def set_ph_value_by_index_example() -> int:
    print('===== set_ph_value_by_index_example =====')
    template = tph.TextPlaceholders('../res/template.dat')
    template.set_ph_value_by_index(73, 'New York City')
    template.display_placeholders()
    print()
    return 0

def set_ph_value_by_position_example() -> int:
    print('===== set_ph_value_by_index_example =====')
    template = tph.TextPlaceholders('../res/template.dat')
    template.set_ph_value_by_position(1, 'Smith')
    template.display_placeholders()
    print()
    return 0

def set_ph_value_by_name_example() -> int:
    print('===== set_ph_value_by_name_example =====')
    template = tph.TextPlaceholders('../res/template.dat')
    template.set_ph_value_by_name('zip', '10001')
    template.display_placeholders()
    print()
    return 0

def apply_placeholder_values_example() -> int:
    print('===== apply_placeholder_values_example =====')
    template = tph.TextPlaceholders('../res/template.dat')
    template.set_ph_value_by_name('fname', 'John')
    template.set_ph_value_by_name('lname', 'Smith')
    template.set_ph_value_by_name('addr', '123 Main St.')
    template.set_ph_value_by_name('city', 'New York City')
    template.set_ph_value_by_name('state', 'NY')
    template.set_ph_value_by_name('zip', '10001')
    template.set_ph_value_by_name('phone', '123-456-7890')
    template.set_ph_value_by_name('cstatus', 'single')
    template.set_ph_value_by_name('email', 'john.smith@email.com')
    print(template.apply_placeholder_values())
    print()
    return 0

if(__name__ == '__main__'):
    init_example()
    get_placeholder_indexes_example()
    get_placeholder_positions_example()
    get_placeholder_names_example()
    remove_placeholder_by_index_example()
    remove_placeholder_by_position_example()
    remove_placeholder_by_name_example()
    set_ph_value_by_index_example()
    set_ph_value_by_position_example()
    set_ph_value_by_name_example()
    apply_placeholder_values_example()