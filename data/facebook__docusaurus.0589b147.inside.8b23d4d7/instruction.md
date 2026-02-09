# Bug Report

### Describe the bug

I've encountered an issue with setext heading parsing where underlines with multiple characters are not being processed correctly. When a setext heading underline contains more than one `=` or `-` character, only the first character is consumed before the parser exits the sequence.

### Reproduction

```markdown
Heading
===

Another heading
---
```

When parsing the above markdown, the setext heading underlines should consume all consecutive `=` or `-` characters on the line, but currently it appears to only process the first character in the sequence before moving on.

### Expected behavior

The parser should consume all consecutive underline characters (either `=` for level 1 headings or `-` for level 2 headings) before exiting the `setextHeadingLineSequence` state. Multi-character underlines like `===` or `---` should be fully tokenized as a single sequence.

### Additional context

This affects standard markdown documents where setext headings typically use multiple underline characters for visual clarity. The current behavior breaks the expected tokenization flow for these heading types.

---
Repository: /testbed
