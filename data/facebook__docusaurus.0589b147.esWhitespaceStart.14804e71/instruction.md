# Bug Report

### Describe the bug

I'm experiencing an issue with MDX parsing where certain whitespace characters are not being handled correctly in JSX expressions. When using unicode whitespace characters (like non-breaking spaces or other unicode whitespace) in JSX tags, the parser seems to get stuck or behaves unexpectedly.

### Reproduction

```jsx
<Component
  prop="value" 
  anotherProp="test"
/>
```

When there's a unicode whitespace character (not a regular space or line ending) between attributes or in the JSX expression, the parsing doesn't work as expected. The component fails to render or the parser enters an infinite loop.

### Expected behavior

Unicode whitespace characters should be treated similarly to regular spaces in JSX expressions and should not cause parsing issues. The parser should either skip over them or handle them gracefully without getting stuck.

### Additional context

This seems to affect JSX tags specifically when whitespace handling is involved. Regular markdown spaces and line endings work fine, but unicode whitespace characters cause problems.

---
Repository: /testbed
