# Bug Report

### Describe the bug

When serializing HTML attributes using rehype-stringify, extra whitespace is being added after the last attribute value in certain cases. This results in malformed HTML output with trailing spaces inside attribute values.

### Reproduction

```js
// When serializing attributes without quotes
const element = {
  type: 'element',
  tagName: 'div',
  properties: {
    class: 'foo bar baz'
  }
}

// The output includes unexpected trailing space
// Expected: <div class="foo bar baz">
// Actual: <div class="foo bar baz ">
```

The issue appears when the last attribute value doesn't end with a quote character. An extra space is being appended where it shouldn't be.

### Expected behavior

Attribute values should not have trailing whitespace added. The serializer should only add spaces between multiple attributes, not after the final one.

### System Info
- rehype-stringify version: 10.0.0
- Node version: Latest

---
Repository: /testbed
