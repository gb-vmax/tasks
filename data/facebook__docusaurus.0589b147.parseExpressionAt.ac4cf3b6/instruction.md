# Bug Report

### Describe the bug

I'm experiencing an issue with `parseExpressionAt` where it seems to be parsing expressions incorrectly. When I try to parse an expression at a specific position in the input string, the parser appears to be reading from the wrong location or the position isn't being handled correctly.

### Reproduction

```js
const input = "const x = 5 + 3";
const result = Parser.parseExpressionAt(input, 10, {});
// Expected to parse "5 + 3" starting at position 10
// But getting unexpected results
```

When calling `parseExpressionAt` with a specific position, the parsed expression doesn't match what's actually at that position in the input string. It's like the position parameter isn't being applied correctly to the parser initialization.

### Expected behavior

The `parseExpressionAt` method should correctly parse the expression starting at the specified position in the input string. The position parameter should be respected so that parsing begins at the exact character index provided.

### Additional context

This is affecting my ability to parse partial expressions from larger code strings. I need to be able to specify exactly where in the input the expression parsing should start.

---
Repository: /testbed
