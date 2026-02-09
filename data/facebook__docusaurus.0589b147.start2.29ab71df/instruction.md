# Bug Report

### Describe the bug

I'm encountering an issue with fenced code blocks in markdown parsing. When there's whitespace before the closing fence, the parser doesn't handle it correctly. The closing fence should be recognized even when preceded by spaces (up to the indentation limit), but it seems like the logic is inverted.

### Reproduction

```markdown
~~~
code content here
   ~~~
```

The closing fence with leading spaces isn't being properly recognized. This affects code blocks where the closing fence is indented.

### Expected behavior

According to the CommonMark spec, closing fences can be indented by 0-3 spaces (or up to the opening fence's indentation). The parser should correctly identify and close the code block when encountering an indented closing fence within the allowed range.

Currently it seems like the whitespace check is backwards - it's calling `factorySpace` when there's NO whitespace instead of when there IS whitespace.

### Additional context

This is breaking markdown documents that have indented closing fences, which is valid markdown syntax. The code block never gets properly closed and subsequent content gets treated as part of the code block.

---
Repository: /testbed
