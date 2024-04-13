from enum import Enum
import sys

class TPHErrorCodes(Enum):
    OK = 0,
    NEGATIVE_INDEX = 1,
    INVALID_POSITION = 2,
    INVALID_INDEX = 3,
    VALUE_NOT_STRING = 4

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
            self.message = 'The value must be of type string.' + str(opt[0]) + '.'
        else:
            self.message = 'Undefined error.'
        super().__init__(self.message)
            

class TextPlaceholders:
    def __init__(self, path : str):
        PLACEHOLDER = '$tph$'
        LEN_PLACEHOLDER = len(PLACEHOLDER)
        self.text = ''
        self.placeholder_names = {}
        self.placeholder_position = {}
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
                self.placeholder_position[self.entries] = absolute_idx
                self.placeholder_names[ph_name] = absolute_idx
                self.placeholder_indexes[absolute_idx] = ''
                self.placeholder_lengths[absolute_idx] = LEN_PLACEHOLDER + ph_name_idx + 1
                absolute_idx += LEN_PLACEHOLDER + ph_name_idx + 1
                self.entries += 1
        self.inited = True
    
    def get_placeholder_indexes(self):
        return [i for i in self.placeholder_indexes.keys()]

    def get_surroundings_by_position(self, position : int):
        if(position < 0):
            raise TPHError(TPHErrorCodes.NEGATIVE_INDEX, [])
        if(position not in self.placeholder_position.keys()):
            raise TPHError(TPHErrorCodes.INVALID_POSITION, [position])
        index = self.placeholder_position[position]
        lower_bound = index - 10
        while(lower_bound < 0):
            lower_bound += 1
        upper_bound = index + self.placeholder_lengths[index] + 10
        while(lower_bound > len(self.text)):
            lower_bound -= 1
        print(self.text[lower_bound:upper_bound])

    def get_surroundings_by_index(self, index : int):
        if(index < 0):
            raise TPHError(TPHErrorCodes.NEGATIVE_INDEX, [])
        if(index not in self.placeholder_indexes.keys()):
            raise TPHError(TPHErrorCodes.INVALID_INDEX, [index])
        lower_bound = index - 10
        while(lower_bound < 0):
            lower_bound += 1
        upper_bound = index + self.placeholder_lengths[index] + 10
        while(lower_bound > len(self.text)):
            lower_bound -= 1
        print(self.text[lower_bound:upper_bound])

    # TODO: get surroundings by name

    def remove_placeholder_by_position(self, position : int):
        index = self.placeholder_position[position]
        del self.placeholder_position[position]
        del self.placeholder_indexes[index]
        self.entries -= 1

    def remove_placeholder_by_index(self, index):
        position = 0
        for i in self.placeholder_indexes.keys():
            if(index == i):
                break
            position += 1
        del self.placeholder_position[position]
        del self.placeholder_indexes[index]
        self.entries -= 1

    # TODO: remove placeholder by name

    # Set placeholder value by position
    def set_ph_value_by_position(self, position : int, value : str):
        if(position < 0):
            raise TPHError(TPHErrorCodes.NEGATIVE_INDEX, [])
        if(position not in self.placeholder_position.keys()):
            raise TPHError(TPHErrorCodes.INVALID_POSITION, [position])
        if(type(value) != type('')):
            raise TPHError(TPHErrorCodes.VALUE_NOT_STRING, [])
        self.placeholder_indexes[self.placeholder_position[position]] = value

    # Set placeholder value by index
    def set_ph_value_by_index(self, index : int, value : str):
        if(index < 0):
            raise TPHError(TPHErrorCodes.NEGATIVE_INDEX, [])
        if(index not in self.placeholder_indexes.keys()):
            raise TPHError(TPHErrorCodes.INVALID_INDEX, [index])
        if(type(value) != type('')):
            raise TPHError(TPHErrorCodes.VALUE_NOT_STRING, [])
        self.placeholder_indexes[index] = value

    # Set placeholder value by name
    def set_ph_value_by_name(self, name : int, value : str):
        if(name not in self.placeholder_names.keys()):
            raise TPHError(TPHErrorCodes.INVALID_INDEX, [name])
        self.placeholder_indexes[self.placeholder_names[name]] = value

    def process_text(self):
        if(self.entries == 0):
            return self.text
        placeholder_idxs = list(self.placeholder_indexes.keys())
        placeholder_idxs_len = len(placeholder_idxs)
        out = ''
        absolute_idx = 0
        for i in range(0, placeholder_idxs_len):
            out += self.text[absolute_idx:placeholder_idxs[i]]
            if(self.placeholder_indexes[placeholder_idxs[i]] == ''):
                out += ''
            else: 
                out += self.placeholder_indexes[placeholder_idxs[i]]
            print(self.text[absolute_idx:placeholder_idxs[i]])
            if(absolute_idx == 0):
                absolute_idx += placeholder_idxs[i] - absolute_idx + self.placeholder_lengths[placeholder_idxs[i]]
                continue
            absolute_idx += (placeholder_idxs[i] - absolute_idx) + self.placeholder_lengths[placeholder_idxs[i]]
        out += self.text[absolute_idx:]
        return out