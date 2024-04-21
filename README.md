
# TextPlaceholders

Perform text replacement using placeholders on a text file.

## Requirements

- Python 3.x
- Python imports: `enum`
- A template text file with placeholders

## Usage

- The template text file contains the original text with placeholders to be replaced. The placeholders must be denoted in the following fashion: `$tph$PlaceholderName$`.
- The library can be included to your project with `import TextPlaceholders as tph`.
- Once imported, you must initialize an instance of a `TextPlaceholders` object with the path to the template text file as an argument to the constructor method.
- Each placeholder can be addressed by index, position, or name.
- Check out the `src/Examples.py` source file that contains usage examples.
