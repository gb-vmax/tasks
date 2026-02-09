# Bug Report

### Describe the bug

I'm experiencing an issue with MDX JSX parsing where the buffer function doesn't seem to be called correctly. When processing MDX JSX tags, the buffer mechanism appears to be broken, which likely causes problems with parsing JSX elements in MDX files.

### Reproduction

```js
// Parse MDX content with JSX tags
const mdxContent = `
# Hello

<MyComponent prop="value">
  Some content
</MyComponent>
`

// Process with remark-mdx
const result = processor.parse(mdxContent)
```

When the parser encounters JSX tags, the internal buffer function is invoked but doesn't actually call the buffer method, so the content isn't properly buffered during parsing. This results in incorrect parsing behavior for MDX JSX elements.

### Expected behavior

The buffer should be properly flushed when processing JSX tags, and MDX content with JSX components should parse correctly without losing or corrupting content.

### System Info
- remark-mdx version: 3.0.0
- Node version: 18.x

---
Repository: /testbed
