# Bug Report

### Describe the bug

I'm experiencing an issue with inline JSX tags in MDX content. When using inline JSX components (text-level JSX), they are being parsed incorrectly and causing unexpected behavior in the output.

### Reproduction

```mdx
This is some text with an <InlineComponent prop="value" /> embedded in it.

Another example: <Highlight color="yellow">highlighted text</Highlight> continues here.
```

When parsing this MDX content, the inline JSX components don't render properly. It seems like they're being treated as block-level elements instead of inline text elements.

### Expected behavior

Inline JSX components should be parsed as text-level elements and render inline with the surrounding text content, not as separate block elements.

### System Info
- remark-mdx version: 3.0.0
- Node version: Latest

---
Repository: /testbed
