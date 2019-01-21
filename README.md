# ispell_stemmer

Tool for creating lists of possible "base" words of a word.

## Script usage

```
$ ispell-export-stem --aff ispell_stemmer/tests/basic.aff --ispell ispell_stemmer/tests/basic.ispell 
{"1xa": ["1x"], "1x": ["1x"], "2ya": ["2y"], "2y": ["2y"], "3xb": ["3x"], "3x": ["3x"], "3yb": ["3y"], "3y": ["3y"]}
```

## Usage in python

See tests.

## Where do I get dictionaries and affix files?

A good list can be found at https://www.cs.hmc.edu/~geoff/ispell-dictionaries.html

Notice that ispell_stemmer doesn't understand all rules (yet).
