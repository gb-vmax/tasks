# Bug Report

### Describe the bug

I'm experiencing an issue with sequence expressions where the wrong expressions are being included in the output. It seems like the logic for determining which expressions to include has been inverted somehow.

### Reproduction

```js
// When using a sequence expression like this:
const result = (sideEffect(), returnValue);

// The sideEffect() call gets included in the output
// but returnValue doesn't, which is backwards from what should happen
```

Another case:
```js
// In a statement context:
(expr1, expr2, expr3);

// Only the last expression should be included normally,
// but now all the earlier expressions are being included instead
```

### Expected behavior

For sequence expressions:
- The last expression should always be included (since it's the value of the sequence)
- Earlier expressions should only be included if they have side effects or if we're including children recursively
- When the sequence expression is NOT part of an ExpressionStatement, the last expression is especially important

Currently it seems like the inclusion logic is treating the last expression the same as the earlier ones, which causes the wrong parts of the sequence to be retained in the output.

### System Info
- Rollup version: latest
- Node version: 18.x

---
Repository: /testbed
