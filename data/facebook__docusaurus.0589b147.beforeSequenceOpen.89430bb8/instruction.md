# Bug Report

### Describe the bug

I'm experiencing an issue with fenced code blocks in markdown parsing. When using code fences (triple backticks or tildes), the parser seems to be handling the prefix calculation incorrectly, which causes problems with indented code blocks.

### Reproduction

```markdown
    ```js
    console.log('test');
    ```
```

When parsing markdown with indented fenced code blocks, the behavior is inconsistent. The issue appears to be related to how the parser calculates the initial prefix length when determining if a line belongs to a code fence.

### Expected behavior

Fenced code blocks should be properly recognized and parsed regardless of indentation level. The prefix length calculation should correctly identify when a line is part of a code fence sequence.

### Additional context

This seems to affect code blocks that have leading whitespace or are nested within other block elements. The parser's handling of the `linePrefix` type check appears to be inverted from what it should be.

---
Repository: /testbed
