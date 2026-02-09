# Bug Report

### Describe the bug

I'm experiencing issues with template literal parsing after a recent update. When using backticks in JavaScript code, the parser seems to be mishandling the position tracking, which causes subsequent tokens to be parsed incorrectly.

### Reproduction

```js
const str = `hello world`;
console.log(str);
```

When this code is parsed, the backtick character isn't being processed correctly. The parser appears to skip over position tracking for the opening backtick, leading to incorrect tokenization of the rest of the template literal.

Additionally, numeric literals are being parsed with the wrong radix flag, which may cause issues with number parsing in certain contexts.

### Expected behavior

Template literals should be tokenized correctly with proper position tracking. The opening backtick should advance the parser position so that the content inside the template literal is parsed accurately.

Number literals should also be parsed with the correct parameters to ensure they're interpreted as intended.

### System Info
- MDX version: 3.0.0
- Parser: acorn-based tokenizer

---
Repository: /testbed
