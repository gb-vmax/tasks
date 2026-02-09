# Bug Report

### Describe the bug

I'm encountering an issue with JSX attribute parsing in MDX flow tags. When using JSX components with attributes, the attribute names are being incorrectly tokenized or processed, which appears to be causing parsing errors or unexpected behavior.

### Reproduction

```mdx
<MyComponent 
  attributeName="value"
  anotherAttribute={expression}
/>
```

When parsing MDX content with JSX flow tags that have attributes, the attribute name tokens seem to be getting mixed up or assigned to the wrong positions. This affects how attributes are recognized and processed.

### Expected behavior

JSX attributes in flow tags should be parsed correctly with their names properly identified and tokenized in the correct order. The attribute name primary token should come before the prefix marker and local name tokens.

### System Info
- remark-mdx version: 3.0.0
- Node version: 18.x

---
Repository: /testbed
