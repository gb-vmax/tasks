# Bug Report

### Describe the bug

I'm experiencing an issue with text node transformations where position information seems to be getting lost or applied incorrectly. When converting markdown text nodes to HAST, the resulting nodes don't have the proper position data attached to them.

### Reproduction

```js
const mdast = {
  type: 'text',
  value: '  some text  ',
  position: {
    start: { line: 1, column: 1 },
    end: { line: 1, column: 14 }
  },
  data: {
    hName: 'span'
  }
}

// Process the text node
const result = toHast(mdast)

// The position information is missing or incorrect
console.log(result.position) // undefined or wrong values
```

### Expected behavior

The transformed HAST node should retain the position information from the original MDAST node. The `position` property should be properly transferred during the transformation process.

### Additional context

This seems to affect text nodes specifically. Other node types appear to work fine. The issue might be related to how the transformation pipeline applies data and patches position information.

---
Repository: /testbed
