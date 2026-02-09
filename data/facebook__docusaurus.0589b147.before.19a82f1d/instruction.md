# Bug Report

### Describe the bug

I'm experiencing an issue with MDX JSX flow tag parsing where the token names appear to be incorrect. Specifically, the tag name and attribute name tokens seem to be swapped or misaligned, which is causing parsing problems with JSX components in MDX files.

### Reproduction

```mdx
<MyComponent attributeName="value" />
```

When parsing this JSX flow tag, the token classification for the tag name and attribute name properties doesn't match what's expected. The issue appears to be related to how the factory function parameters are ordered when processing JSX flow tags.

### Expected behavior

The parser should correctly identify and tokenize:
- Tag names with the appropriate `mdxJsxFlowTagNamePrimary` token
- Attribute names with the appropriate `mdxJsxFlowTagAttributeNamePrimary` token

Currently, these seem to be getting mixed up during the parsing process.

### System Info
- @mdx-js/mdx version: 3.0.0
- Node version: Latest

---
Repository: /testbed
