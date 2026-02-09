# Bug Report

### Describe the bug

I'm experiencing an issue with attribute serialization in rehype-stringify where boolean and overloaded boolean attributes are not being handled correctly. When setting attribute values, the serialization logic appears to be inverted, causing attributes to be rendered incorrectly in the output HTML.

### Reproduction

```js
const rehype = require('rehype');
const stringify = require('rehype-stringify');

const processor = rehype().use(stringify);

// Test with overloaded boolean attribute
const tree = {
  type: 'element',
  tagName: 'input',
  properties: {
    download: 'download'
  },
  children: []
};

const result = processor.stringify(tree);
console.log(result);
// Expected: <input download="download">
// Actual output is incorrect
```

### Expected behavior

Overloaded boolean attributes (like `download`) should be serialized correctly when their value matches the attribute name. The attribute should appear with its value in the output HTML when appropriate, and as a boolean when the value is true or an empty string.

### Additional context

This seems to affect attributes that can be both boolean and have string values. The serialization is producing unexpected output for these edge cases.

---
Repository: /testbed
