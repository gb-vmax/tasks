# Bug Report

### Describe the bug

I'm encountering an issue when rendering inline code blocks in MDX. The content inside backticks is not being displayed correctly - instead of showing the actual code text, I'm getting errors or unexpected behavior.

### Reproduction

```mdx
Here is some `inline code` in my document.
```

When processing this MDX content, the inline code portion fails to render properly. The text that should appear between the backticks is not being extracted correctly.

### Expected behavior

The inline code should render as a `<code>` element with the text content preserved. For example, `` `hello world` `` should produce `<code>hello world</code>` in the output.

### Additional context

This seems to affect all inline code usage in MDX documents. Regular text renders fine, but anything wrapped in backticks causes issues. The problem appears to be related to how the inline code nodes are being processed during the MDX-to-HTML transformation.

---
Repository: /testbed
