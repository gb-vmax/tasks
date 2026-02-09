# Bug Report

### Describe the bug

JSX text content is not being rendered correctly. When using JSX text nodes, the content appears to be empty instead of displaying the actual text value.

### Reproduction

```jsx
const element = <div>Hello World</div>
```

When this JSX is processed, the text "Hello World" is not rendered. Instead, an empty string is returned.

### Expected behavior

The JSX text content should be properly rendered with whitespace normalized according to the rules (trimming leading/trailing whitespace and merging consecutive whitespace into single spaces).

For example:
```jsx
<div>  Hello   World  </div>
```

Should render as: `"Hello World"`

### System Info
- Rollup version: latest
- Node version: 18.x

This seems to have started happening recently. The text nodes are being created but the content is empty when it should contain the normalized text.

---
Repository: /testbed
