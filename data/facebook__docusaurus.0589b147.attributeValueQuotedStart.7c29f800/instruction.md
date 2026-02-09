# Bug Report

### Describe the bug

I'm encountering an issue with quoted attribute values in JSX/MDX parsing. When using quoted attributes in JSX tags, the closing quote is not being properly recognized, causing the parser to incorrectly handle the attribute value.

### Reproduction

```jsx
<Component attr="value" />
```

When parsing JSX with quoted attribute values like the example above, the attribute value handling appears to be broken. The parser seems to be treating the closing quote incorrectly, which leads to unexpected parsing behavior.

### Expected behavior

The parser should correctly recognize and handle quoted attribute values in JSX tags. When encountering a closing quote that matches the opening quote, it should properly close the attribute value and continue parsing subsequent attributes or the tag closing.

### Additional context

This appears to affect the `@mdx-js/mdx` package's JSX parsing logic, specifically in how it handles the state transitions when processing quoted attribute values. The issue manifests when the parser encounters the closing quote marker in an attribute value.

---
Repository: /testbed
