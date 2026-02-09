# Bug Report

### Describe the bug

I'm encountering an issue with self-closing JSX tags in MDX content. When I use a self-closing tag with a forward slash (like `<Component />`), the parser seems to be incorrectly processing it and causing unexpected behavior.

### Reproduction

```jsx
<MyComponent />
```

When parsing the above MDX content, the closing slash appears to be handled incorrectly. The parser seems to skip over the component name validation after encountering the `/` character.

### Expected behavior

Self-closing JSX tags should be properly parsed with the component name validated before the closing `/>` sequence. The parser should recognize this as a valid self-closing tag pattern.

### Additional context

This appears to affect any self-closing JSX element in MDX files. Regular opening/closing tag pairs (like `<Component></Component>`) seem to work fine, but the self-closing syntax is problematic.

---
Repository: /testbed
