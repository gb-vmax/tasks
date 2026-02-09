# Bug Report

### Describe the bug

I'm encountering an issue with MDX JSX text tag parsing. It appears that inline JSX components are not being tokenized correctly, causing parsing failures or unexpected behavior when using JSX syntax within text content.

### Reproduction

```mdx
This is some text with an inline <Component prop="value" /> tag.
```

When parsing MDX content that contains inline JSX tags (text-level JSX), the tokenizer doesn't handle them properly. The issue seems specific to JSX tags that appear inline within text content, as opposed to block-level JSX.

### Expected behavior

Inline JSX components should be parsed and tokenized correctly, allowing them to be used seamlessly within text content. The parser should recognize these as valid MDX JSX text tags and process them accordingly.

### System Info
- remark-mdx version: 3.0.0
- Node version: Latest

This seems to have appeared recently and is affecting our ability to use inline components in MDX documents.

---
Repository: /testbed
