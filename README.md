# text converter

This is a tool to let you convert a sentence into a different case.

e.g. 
`This is a normal sentence`

- Lower
  - `this is a normal sentence`
- Upper
  - `THIS IS A NORMAL SENTENCE`
- Sentence
  - `This is a normal sentence.`
- Title
  - `This is a Normal Sentence`
- Title (incl. articles)
  - `This Is A Normal Sentence`
- Studly (AnNoYiNg)
  - `ThIs Is A nOrMaL sEnTeNcE`

## Installation
- Install python 3.5+
- Clone this repo & cd into it

## Usage
```
Usage: python converter.py [<OPTION>] ["<your sentence here>"]

Convert strings. If you provide any CLI arguments, you must provide an option
 along with the sentence in double quotes. If you do not provide arguments,
 you'll be asked for the arguments.

Options:
  -lower                convert to lowercase
  -upper                CONVERT TO UPPERCASE
  -sentence             Convert to sentence case.
  -title                Convert to Title Case
  -title-all            Convert To Title Case, Including The Arcicles
  -studly, -annoying    CoNvErT tO sTuDlY cAsE

  -help                 Print this help message
  ```
