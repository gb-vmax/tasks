# Bug Report

### Describe the bug

I'm encountering an issue with JSX attribute values in MDX files. When using quoted attribute values, the closing quote is not being recognized correctly, causing parsing errors.

### Reproduction

```mdx
<Component name="value" />
```

The parser seems to be looking for the wrong character code when trying to match the closing quote. Instead of properly closing the attribute value, it's checking for a character code that's off by one.

### Expected behavior

The JSX tag with quoted attribute values should parse correctly without errors. The closing quote should be properly matched with the opening quote.

### Additional context

This affects any JSX element in MDX that uses quoted attribute values (both single and double quotes). The issue appears to be in the attribute value parsing logic where it's comparing against the wrong marker value.

---
Repository: /testbed
