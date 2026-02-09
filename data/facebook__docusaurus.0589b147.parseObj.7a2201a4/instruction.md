# Bug Report

### Describe the bug

I'm encountering an issue with object literal parsing where the first property in an object is not being recognized correctly. It seems like the parser is treating the first property as if it needs a comma before it, which is causing unexpected parsing behavior.

### Reproduction

```js
const obj = {
  name: 'test',
  value: 42
}
```

When parsing this simple object literal, the parser appears to be skipping or mishandling the first property. The issue seems to affect any object literal with multiple properties.

### Expected behavior

The parser should correctly handle object literals with the first property being parsed without requiring a preceding comma. All properties in an object literal should be parsed correctly regardless of their position.

### Additional context

This appears to have started recently and affects basic object literal syntax. The problem is specifically with how the first property in an object is being handled during the parsing phase.

---
Repository: /testbed
