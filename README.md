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

## Usage
- Install Python 3
- Using arguments
  - `python converter.py -<type> "<your sentence here>"`
- Using stdin input
  - `python converter.py`
  - `What kind of conversion do you want? `
  - `Enter your sentence: "<your sentence here>"`
- Types
  - The types for the flags/input are as follows:
  - `lower`
  - `upper`
  - `sentence`
  - `title`
  - `title-all`
  - `studly`