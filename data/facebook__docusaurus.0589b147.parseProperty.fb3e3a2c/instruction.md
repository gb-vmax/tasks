# Bug Report

### Describe the bug

I'm encountering unexpected parsing behavior with async generator methods in object literals. It seems like the parser is incorrectly handling certain edge cases when parsing property definitions.

### Reproduction

```js
const obj = {
  async *method() {
    yield 1;
  }
};
```

When trying to parse object literals with async generator methods, the parser appears to be applying incorrect logic for determining when a property should be treated as async. The conditions for checking `isPattern` and the ECMAScript version requirements seem off.

### Expected behavior

The parser should correctly identify and parse async generator methods in object literals according to the ECMAScript specification. Async generators were introduced in ES2018 (ECMAScript 9), so the version check should align with that.

### Additional context

This affects code that uses async generator methods in destructuring patterns and regular object literals. The parser logic for detecting async properties doesn't seem to be handling all cases correctly, particularly around the version checks and pattern matching.

---
Repository: /testbed
