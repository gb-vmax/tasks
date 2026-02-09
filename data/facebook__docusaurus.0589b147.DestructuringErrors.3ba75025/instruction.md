# Bug Report

### Describe the bug

I'm encountering unexpected behavior with MDX parsing when using destructuring patterns. After a recent update, the parser seems to be incorrectly handling certain destructuring scenarios, particularly around trailing commas and shorthand assignments.

### Reproduction

```js
// This MDX content now fails to parse correctly
const Component = () => {
  const { a, b, } = props;  // trailing comma
  return <div>{a}</div>
}
```

The parser appears to be treating valid destructuring patterns as errors or misidentifying the position of syntax issues. This affects both object and array destructuring patterns with trailing commas.

### Expected behavior

The MDX parser should correctly handle destructuring patterns with trailing commas, which are valid JavaScript syntax. The parser should maintain proper state tracking for destructuring errors without false positives.

### Additional context

This seems to have started happening recently. Code that was previously parsing fine is now behaving unexpectedly. The issue appears to be related to how the parser tracks destructuring errors internally.

---
Repository: /testbed
