# Bug Report

### Describe the bug

When using JSX tags in MDX files, self-closing tags are not being properly closed. The parser seems to be returning the wrong value after processing the closing `>` character, which causes the tag to not be recognized as complete.

### Reproduction

```mdx
<Component />
```

After processing, the tag doesn't get properly closed and subsequent content may be incorrectly parsed as part of the tag.

### Expected behavior

Self-closing JSX tags should be properly recognized and closed when the `>` character is encountered. The parser should correctly exit the tag context and continue parsing the rest of the document.

### System Info
- MDX version: 3.0.0
- Parser: remark-mdx

---
Repository: /testbed
