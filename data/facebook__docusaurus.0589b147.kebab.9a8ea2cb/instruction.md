# Bug Report

### Describe the bug
I'm encountering an issue with CSS property name conversion in MDX. When using camelCase property names in JSX style objects, they're being converted incorrectly to kebab-case format. Instead of getting the expected lowercase kebab-case (e.g., `background-color`), I'm getting uppercase with double dashes (e.g., `--BACKGROUND-COLOR`).

### Reproduction
```jsx
// In an MDX file
<div style={{ backgroundColor: 'red', fontSize: '16px' }}>
  Hello World
</div>
```

The style attributes are being transformed incorrectly. For example:
- `backgroundColor` becomes `--BACKGROUND-COLOR` instead of `background-color`
- `fontSize` becomes `--FONT-SIZE` instead of `font-size`

This breaks the styling completely as browsers don't recognize these malformed CSS property names.

### Expected behavior
CamelCase style properties should be converted to standard kebab-case format:
- `backgroundColor` → `background-color`
- `fontSize` → `font-size`
- `marginTop` → `margin-top`

The current behavior with double dashes and uppercase letters is not valid CSS syntax.

### System Info
- @mdx-js/mdx version: 3.0.0
- Browser: Chrome/Firefox (affects all browsers)

---
Repository: /testbed
