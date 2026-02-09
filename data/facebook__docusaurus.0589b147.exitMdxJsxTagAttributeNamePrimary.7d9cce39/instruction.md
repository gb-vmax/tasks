# Bug Report

### Describe the bug

When parsing MDX JSX tags with multiple attributes, the attribute names are being assigned to the wrong attribute nodes. It appears that the parser is incorrectly indexing into the attributes array, causing attribute names to be set on the wrong elements.

### Reproduction

```jsx
// MDX content with multiple attributes
<Component firstName="John" lastName="Doe" />
```

When parsing this, the attribute names get misaligned with their values. The `firstName` name might end up on a different attribute node than expected.

### Expected behavior

Each attribute name should be correctly assigned to its corresponding attribute node in the order they appear in the source. The parser should use the correct index to access the attribute being processed.

### Additional context

This seems to affect JSX tags with 2 or more attributes. Single-attribute tags might work correctly, but once you have multiple attributes, the name assignment gets confused about which attribute node it should be updating.

---
Repository: /testbed
