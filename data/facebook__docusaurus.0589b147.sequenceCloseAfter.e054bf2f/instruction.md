# Bug Report

### Describe the bug

I'm experiencing an issue with fenced code blocks in MDX files. After a recent update, code blocks are not being parsed correctly and the content is not being rendered as expected.

### Reproduction

```mdx
# My Document

Some text before the code block.

```js
function example() {
  console.log('test');
}
```

More text after the code block.
```

When I try to render this MDX content, the code fence doesn't close properly and the subsequent content gets treated as part of the code block instead of regular markdown.

### Expected behavior

The fenced code block should be properly recognized and closed, with the text after the closing fence being treated as normal markdown content. The code block should render with syntax highlighting and the following content should appear as regular text.

### Additional context

This seems to have started happening recently. The same MDX files were working fine before. It appears to affect all fenced code blocks regardless of the language specified.

---
Repository: /testbed
