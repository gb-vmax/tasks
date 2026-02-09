# Bug Report

### Describe the bug

I'm encountering an issue with object property parsing where colons (`:`) in object literals are not being consumed properly. This causes the parser to fail or produce incorrect AST nodes when parsing object properties with explicit key-value pairs.

### Reproduction

```js
const obj = {
  key: value
}
```

When parsing the above object literal, the colon token is checked but not consumed, leading to unexpected behavior in subsequent parsing steps. The parser seems to be stuck on the colon token instead of moving past it to parse the property value.

### Expected behavior

The parser should properly consume the colon token when parsing object property key-value pairs, allowing it to correctly parse the value expression that follows.

### Additional context

This appears to affect standard object property syntax with explicit colons. Shorthand properties (without colons) may work differently but I haven't tested that thoroughly yet.

---
Repository: /testbed
