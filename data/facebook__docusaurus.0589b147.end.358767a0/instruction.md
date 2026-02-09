# Bug Report

### Describe the bug

After a recent update, inline directives (leaf directives) are no longer being parsed correctly. It seems like the parser is rejecting valid directive syntax that should be accepted.

### Reproduction

```markdown
This is a text with :directive[content] in the middle of a line.
```

When parsing the above markdown, the directive should be recognized and processed, but instead it appears to be treated as plain text or rejected by the parser.

### Expected behavior

The inline directive `:directive[content]` should be properly tokenized and parsed as a directive leaf node, allowing it to appear inline within text content on the same line.

### Additional context

This affects any markdown content that uses inline/leaf directives within regular text paragraphs. The directives work fine when they're on their own line, but fail when embedded in flowing text.

---
Repository: /testbed
