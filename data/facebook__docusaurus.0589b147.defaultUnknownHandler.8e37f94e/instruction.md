# Bug Report

### Describe the bug

I'm experiencing an issue with markdown to HTML conversion where nodes with custom data properties (`hProperties` or `hChildren`) are being incorrectly converted to text nodes instead of element nodes. This seems to be breaking the rendering of custom markdown extensions.

### Reproduction

```js
const node = {
  type: 'custom',
  value: 'some text',
  data: {
    hProperties: { className: 'custom-class' }
  }
}

// The node is converted to a text node instead of an element
// Expected: element with div tag and custom properties
// Actual: text node with just the value
```

### Expected behavior

When a node has `hProperties` or `hChildren` in its data object, it should be treated as an element node with those properties applied, not converted to a plain text node. The custom properties should be preserved in the resulting HTML element.

### System Info
- remark-rehype version: 11.0.0

---
Repository: /testbed
