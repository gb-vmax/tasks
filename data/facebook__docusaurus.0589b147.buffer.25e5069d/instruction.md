# Bug Report

### Describe the bug

I'm encountering an issue with MDX JSX parsing where the buffer function is not being called correctly. When processing MDX content with JSX tags, it seems like the internal buffering mechanism isn't working as expected, which can lead to parsing errors or incorrect output.

### Reproduction

```js
// When parsing MDX content with JSX elements like:
const mdxContent = `
# Hello

<CustomComponent>
  Some content here
</CustomComponent>
`;

// The parser fails to properly buffer the content
// resulting in unexpected behavior
```

### Expected behavior

The parser should correctly buffer and process JSX tags within MDX content. The `buffer()` method should be invoked to handle the buffering of parsed tokens.

### System Info
- remark-mdx version: 3.0.0
- Node version: Latest

This appears to be related to the internal token handling in the MDX JSX parser. The buffering step seems to be skipped or not executed properly.

---
Repository: /testbed
