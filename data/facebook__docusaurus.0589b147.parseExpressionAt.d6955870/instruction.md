# Bug Report

### Describe the bug

I'm encountering an issue with `parseExpressionAt` where it seems to be parsing expressions incorrectly. The function appears to be processing the input in an unexpected way, leading to incorrect parsing results.

### Reproduction

```js
const input = "x + y";
const pos = 0;
const options = {};

const result = Parser.parseExpressionAt(input, pos, options);
// Result is not what's expected - the expression is not parsed correctly
```

When trying to parse an expression at a specific position, the parser doesn't seem to recognize the input string properly. It's like the position and input parameters are getting mixed up somehow.

### Expected behavior

The parser should correctly parse the expression starting at the given position in the input string. The `parseExpressionAt` method should handle the input string and position correctly to return a valid parsed expression.

### Additional context

This seems to have started happening recently. The parser was working fine before, but now expressions aren't being parsed as expected. Not sure if there was a recent change that might have affected this.

---
Repository: /testbed
