# Bug Report

### Describe the bug

I'm experiencing an issue with HTML element rendering where self-closing tags are not being handled correctly for elements with empty children arrays. When an element has `children: []` (empty array), it's being rendered as a self-closing tag instead of with opening and closing tags.

### Reproduction

```js
const node = {
  type: 'element',
  tagName: 'div',
  properties: {},
  children: []
}

// Expected output: <div></div>
// Actual output: <div />
```

This seems to affect elements that should never be self-closing in HTML (like `div`, `span`, etc.) but happen to have an empty children array.

### Expected behavior

Elements with empty children arrays should still render with both opening and closing tags unless they are actual void/self-closing elements in HTML (like `img`, `br`, `hr`, etc.).

For example:
- `<div></div>` not `<div />`
- `<span></span>` not `<span />`

### System Info
- rehype-stringify version: 10.0.0

---
Repository: /testbed
