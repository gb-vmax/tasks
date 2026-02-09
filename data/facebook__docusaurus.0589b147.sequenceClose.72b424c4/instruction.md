# Bug Report

### Describe the bug

I'm experiencing an issue with inline code parsing in MDX content. When using backticks for inline code, the parser seems to be incorrectly handling the closing sequence, especially when there are more closing backticks than opening ones.

### Reproduction

```mdx
This is some text with `inline code` that should work fine.

But this breaks: `code with extra backticks``
```

The second example with an extra closing backtick doesn't parse correctly. The inline code block either extends beyond where it should end or fails to close properly.

### Expected behavior

The parser should correctly match opening and closing backtick sequences for inline code blocks. If there are extra backticks after the closing sequence, they should either be treated as separate characters or the code block should close at the matching sequence length.

For example:
- `` `code` `` should parse as inline code
- `` `code`` `` should handle the extra backtick gracefully
- Multiple backticks should only close when the count matches the opening sequence

### System Info
- @mdx-js/mdx version: 3.0.0
- Node version: Latest LTS

This seems to have started occurring recently and is affecting our documentation rendering. Any help would be appreciated!

---
Repository: /testbed
