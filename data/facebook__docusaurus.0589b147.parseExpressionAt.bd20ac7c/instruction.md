# Bug Report

### Describe the bug

I'm encountering an issue with `parseExpressionAt` where expressions are being parsed incorrectly when specifying a position. It seems like the parser is starting from the wrong position or parsing the expression twice, leading to unexpected results.

### Reproduction

```js
const input = "x + y + z";
const result = Parser.parseExpressionAt(input, 4, options);

// The result is not what I expected - seems like it's parsing from position 3 instead of 4
// or doing some kind of double parsing
```

When I try to parse an expression at a specific position in the input string, the parser appears to be off by one position and/or the expression gets evaluated multiple times.

### Expected behavior

`parseExpressionAt` should parse the expression starting exactly at the specified position and return the parsed result once. The position parameter should correspond to the exact index in the input string where parsing should begin.

### System Info
- remark-mdx version: 3.0.0
- Node version: 18.x

---
Repository: /testbed
