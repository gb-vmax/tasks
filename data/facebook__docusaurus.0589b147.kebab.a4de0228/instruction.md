# Bug Report

### Describe the bug
I'm experiencing an issue with property name transformations in MDX. When using camelCase property names, they're being converted incorrectly - instead of the expected kebab-case format with lowercase letters and hyphens, I'm getting uppercase letters with underscores.

### Reproduction
```js
// When processing attributes like:
const element = {
  backgroundColor: 'red',
  fontSize: '16px'
}

// Expected output: background-color, font-size
// Actual output: _BACKGROUND_COLOR, _FONT_SIZE
```

### Expected behavior
CamelCase properties should be converted to kebab-case format (e.g., `backgroundColor` → `background-color`), not to uppercase with underscores.

### System Info
- @mdx-js/mdx version: 3.0.0

This seems to have broken attribute name conversion for HTML/CSS properties. Any help would be appreciated!

---
Repository: /testbed
