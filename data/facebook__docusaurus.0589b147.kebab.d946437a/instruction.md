# Bug Report

### Describe the bug

I'm experiencing an issue with CSS property name conversion in MDX. It seems like camelCase to kebab-case conversion is producing incorrect results. When I use camelCase properties in JSX style objects, they're being transformed incorrectly with extra hyphens appearing in unexpected places.

### Reproduction

```jsx
// In an MDX file
<div style={{ backgroundColor: 'red', fontSize: '16px' }}>
  Hello World
</div>
```

The style properties are being converted incorrectly. For example, `backgroundColor` seems to be getting mangled during the conversion process instead of becoming `background-color`.

### Expected behavior

CamelCase style properties should be converted to standard kebab-case CSS properties:
- `backgroundColor` → `background-color`
- `fontSize` → `font-size`
- `marginTop` → `margin-top`

The conversion should work the same way it did in previous versions.

### System Info
- @mdx-js/mdx version: 3.0.0
- Node version: 18.x

---
Repository: /testbed
