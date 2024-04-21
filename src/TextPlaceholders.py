from enum import Enum

class TPHErrorCodes(Enum):
    OK = 0,
    NEGATIVE_INDEX = 1,
    INVALID_POSITION = 2,
    INVALID_INDEX = 3,
    INVALID_NAME = 4,
    VALUE_NOT_STRING = 5


class TPHError(Exception):
    def __init__(self, err_code : TPHErrorCodes, opt : list):
        self.error_code = err_code
        if(self.error_code == TPHErrorCodes.OK):
            self.message = ''
        elif(self.error_code == TPHErrorCodes.NEGATIVE_INDEX):
            self.message = 'Index value cannot be negative.'
        elif(self.error_code == TPHErrorCodes.INVALID_POSITION):
            self.message = 'There is not a placeholder at this position value: ' + str(opt[0]) + '.'
        elif(self.error_code == TPHErrorCodes.INVALID_INDEX):
            self.message = 'There is not a placeholder at this index value: ' + str(opt[0]) + '.'
        elif(self.error_code == TPHErrorCodes.INVALID_NAME):
            self.message = 'There is not a placeholder with this name value: ' + str(opt[0]) + '.'
        elif(self.error_code == TPHErrorCodes.VALUE_NOT_STRING):
            self.message = 'The input value must be of type string.'
        else:
            self.message = 'Undefined error.'
        super().__init__(self.message)
            

class TextPlaceholders:
    def __init__(self, path : str):
        PLACEHOLDER = '$tph$'
        LEN_PLACEHOLDER = len(PLACEHOLDER)
        self.text = ''
        self.placeholder_names = {}
        self.placeholder_positions = {}
        self.placeholder_indexes = {} 
        self.placeholder_lengths = {} 
        self.entries = 0
        with open(path) as file:
            for line in file:
                self.text += line
            absolute_idx = 0
            relative_idx = 0
            while(True):
                relative_idx = self.text[absolute_idx:].find(PLACEHOLDER)
                if(relative_idx == -1):
                    break
                ph_name_idx = self.text[absolute_idx + relative_idx + LEN_PLACEHOLDER:].find('$')
                ph_name = self.text[absolute_idx + relative_idx + LEN_PLACEHOLDER:absolute_idx + relative_idx + LEN_PLACEHOLDER + ph_name_idx]
                absolute_idx += relative_idx
                self.placeholder_indexes[absolute_idx] = ''
                self.placeholder_positions[self.entries] = absolute_idx
                self.placeholder_names[ph_name] = self.entries
                self.placeholder_lengths[absolute_idx] = LEN_PLACEHOLDER + ph_name_idx + 1
                absolute_idx += LEN_PLACEHOLDER + ph_name_idx + 1
                self.entries += 1
    
    def get_placeholder_indexes(self):
        return [i for i in self.placeholder_indexes.keys()]
    
    def get_placeholder_positions(self):
        return [i for i in self.placeholder_positions.keys()]
    
    def get_placeholder_names(self):
        return [i for i in self.placeholder_names.keys()]
    
    def display_placeholders(self):
        # Define header and for now, maximum text lengths per column
        header = ['NAME', 'POSITION', 'INDEX', 'VALUE']
        name_max_len = len(header[0])
        position_max_len = len(header[1])
        index_max_len = len(header[2])
        value_max_len = len(header[3])
        # Find the element with maximum length in a column
        for name in self.placeholder_names:
            position = self.placeholder_names[name]
            index = self.placeholder_positions[position]
            value = self.placeholder_indexes[index]
            name_max_len = max(name_max_len, len(name))
            position_max_len = max(position_max_len, len(str(position)))
            index_max_len = max(index_max_len, len(str(index)))
            value_max_len = max(value_max_len, len(value))
        # Prepare header print
        if(name_max_len > len(header[0])):
            header[0] += ''.join(['.' for i in range(0, name_max_len - len(header[0]))])
        if(position_max_len > len(header[1])):
            header[1] += ''.join(['.' for i in range(0, position_max_len - len(header[1]))])
        if(index_max_len > len(header[2])):
            header[2] += ''.join(['.' for i in range(0, index_max_len - len(header[2]))])
        if(value_max_len > len(header[3])):
            header[3] += ''.join(['.' for i in range(0, value_max_len - len(header[3]))])
        print(header[0], header[1], header[2], header[3])
        # Prepate table entries print
        for name in self.placeholder_names:
            position = self.placeholder_names[name]
            index = self.placeholder_positions[position]
            value = self.placeholder_indexes[index]
            index = str(self.placeholder_positions[position])
            if(index_max_len > len(index)):
                index = ''.join(['.' for i in range(0, index_max_len - len(index))]) + index
            position = str(self.placeholder_names[name])
            if(position_max_len > len(position)):
                position = ''.join(['.' for i in range(0, position_max_len - len(position))]) + position
            if(name_max_len > len(name)):
                name += ''.join(['.' for i in range(0, name_max_len - len(name))])
            if(value_max_len > len(value)):
                value += ''.join(['.' for i in range(0, value_max_len - len(value))])
            print(name, position, index, value)

    def remove_placeholder_by_index(self, index : int):
        if(index not in self.placeholder_indexes):
            raise TPHError(TPHErrorCodes.INVALID_INDEX, [index])
        for i in self.placeholder_positions:
            if(self.placeholder_positions[i] == index):
                position = i
                break
        for i in self.placeholder_names:
            if(self.placeholder_names[i] == position):
                name = i
                break
        del self.placeholder_indexes[index]
        del self.placeholder_positions[position]
        del self.placeholder_names[name]
        self.entries -= 1

    def remove_placeholder_by_position(self, position : int):
        if(position not in self.placeholder_positions):
            raise TPHError(TPHErrorCodes.INVALID_POSITION, [position])
        index = self.placeholder_positions[position]
        for i in self.placeholder_names:
            if(self.placeholder_names[i] == position):
                name = i
                break
        del self.placeholder_indexes[index]
        del self.placeholder_positions[position]
        del self.placeholder_names[name]
        self.entries -= 1

    def remove_placeholder_by_name(self, name : str):
        if(name not in self.placeholder_names):
            raise TPHError(TPHErrorCodes.INVALID_NAME, [name])
        if(type(name) != str):
            raise TPHError(TPHErrorCodes.VALUE_NOT_STRING, [])
        position = self.placeholder_names[name]
        index = self.placeholder_positions[position]
        del self.placeholder_indexes[index]
        del self.placeholder_positions[position]
        del self.placeholder_names[name]
        self.entries -= 1

    def set_ph_value_by_index(self, index : int, value : str):
        if(index < 0):
            raise TPHError(TPHErrorCodes.NEGATIVE_INDEX, [])
        if(index not in self.placeholder_indexes.keys()):
            raise TPHError(TPHErrorCodes.INVALID_INDEX, [index])
        if(type(value) != str):
            raise TPHError(TPHErrorCodes.VALUE_NOT_STRING, [])
        self.placeholder_indexes[index] = value

    def set_ph_value_by_position(self, position : int, value : str):
        if(position < 0):
            raise TPHError(TPHErrorCodes.NEGATIVE_INDEX, [])
        if(position not in self.placeholder_positions.keys()):
            raise TPHError(TPHErrorCodes.INVALID_POSITION, [position])
        if(type(value) != type('')):
            raise TPHError(TPHErrorCodes.VALUE_NOT_STRING, [])
        index = self.placeholder_positions[position]
        self.placeholder_indexes[index] = value

    def set_ph_value_by_name(self, name : int, value : str):
        if(name not in self.placeholder_names.keys()):
            raise TPHError(TPHErrorCodes.INVALID_INDEX, [name])
        position = self.placeholder_names[name]
        index = self.placeholder_positions[position]
        self.placeholder_indexes[index] = value

    def apply_placeholder_values(self):
        if(self.entries == 0):
            return self.text
        placeholder_idxs = list(self.placeholder_indexes.keys())
        out = ''
        absolute_idx = 0
        for i in range(0, self.entries):
            out += self.text[absolute_idx:placeholder_idxs[i]]
            if(self.placeholder_indexes[placeholder_idxs[i]] == ''):
                out += ''
            else: 
                out += self.placeholder_indexes[placeholder_idxs[i]]
            if(absolute_idx == 0):
                absolute_idx += placeholder_idxs[i] - absolute_idx + self.placeholder_lengths[placeholder_idxs[i]]
                continue
            absolute_idx += (placeholder_idxs[i] - absolute_idx) + self.placeholder_lengths[placeholder_idxs[i]]
        out += self.text[absolute_idx:]
        return out
