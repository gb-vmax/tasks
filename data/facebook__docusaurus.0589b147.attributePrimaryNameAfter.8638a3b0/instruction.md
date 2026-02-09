# Bug Report

### Describe the bug

When using JSX attributes with namespaces (e.g., `xml:lang` or `xmlns:xlink`), the colon separator is not being recognized correctly. This causes the parser to fail or incorrectly parse attribute names that include a namespace prefix.

### Reproduction

```jsx
<Component xml:lang="en" />
```

or

```jsx
<svg xmlns:xlink="http://www.w3.org/1999/xlink">
  <use xlink:href="#icon" />
</svg>
```

### Expected behavior

The parser should correctly handle the colon (`:`) character as a separator between the namespace prefix and the local attribute name. Attributes like `xml:lang` or `xlink:href` should be parsed without errors.

### System Info
- @mdx-js/mdx version: 3.0.0

---
Repository: /testbed
