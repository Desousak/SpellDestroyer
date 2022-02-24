# Misspelling Convertor
### A script for converting the corpora of spelling mistakes into an easy to read JSON.
<br />

## JSON Format:
Each key within the `missp.json` file is a word (string), with the value corresponding to the misspellings of that word (string[]).

```
{
    Word: string[],
    ...
}
```

## How to convert:
1. Ensure that `misspell.dat` is within this folder
2. Run `process.py`
3. Ensure that `missp.json` is created and valid
