# Bug Report

### Describe the bug

I'm encountering an issue with self-closing MDX tags that have no attributes. When parsing JSX/MDX content with self-closing tags like `<Component />`, the parser seems to be handling them incorrectly.

### Reproduction

```jsx
// This MDX content doesn't parse correctly
<MyComponent />

// Also affects inline self-closing tags
Some text <Icon /> more text
```

The issue appears when you have a self-closing tag without any attributes - just the component name followed by `/>`.

### Expected behavior

Self-closing tags without attributes should be parsed correctly, just like they are in regular JSX. The parser should recognize the `/>` as a valid self-closing marker and handle it properly.

### Additional context

This seems to have started happening recently. Regular tags with attributes or non-self-closing tags work fine, it's specifically the combination of:
- Self-closing marker (`/>`)
- No attributes

that triggers the problem.

---
Repository: /testbed
