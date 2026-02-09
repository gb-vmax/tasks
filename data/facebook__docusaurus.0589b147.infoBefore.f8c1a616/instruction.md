# Bug Report

### Describe the bug

I'm experiencing an issue with fenced code blocks in markdown parsing. When I have a code fence without an info string (like just ``` without a language specified), the parser seems to get stuck or behaves unexpectedly. The content after the opening fence isn't being processed correctly.

### Reproduction

```markdown
```
some code here
```
```

When parsing this markdown, the code block doesn't get recognized properly. It seems like the parser is not handling the case where there's no info string after the opening fence delimiter.

### Expected behavior

The parser should correctly handle fenced code blocks even when no language/info string is provided after the opening fence. The code content should be captured and the closing fence should be recognized.

### Additional context

This seems to affect basic code blocks without language specifications. Code blocks with language identifiers (like ```javascript) might work fine, but plain ``` blocks are problematic.

---
Repository: /testbed
