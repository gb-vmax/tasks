# Bug Report

### Describe the bug

I'm experiencing an issue with CSS property name conversion in MDX. When using camelCase CSS properties in JSX style objects, they're not being converted to kebab-case correctly. Instead of getting the expected hyphenated lowercase format (e.g., `background-color`), the properties are being transformed to uppercase letters without hyphens.

### Reproduction

```jsx
const styles = {
  backgroundColor: 'red',
  fontSize: '16px'
}

<div style={styles}>Test</div>
```

When this gets processed, instead of generating:
```css
background-color: red;
font-size: 16px;
```

It appears to be generating something like:
```css
BACKGROUNDCOLOR: red;
FONTSIZE: 16px;
```

### Expected behavior

CamelCase CSS property names should be converted to standard kebab-case format with lowercase letters and hyphens (e.g., `backgroundColor` → `background-color`).

### System Info
- @mdx-js/mdx version: 3.0.0
- Node version: 18.x

---
Repository: /testbed
