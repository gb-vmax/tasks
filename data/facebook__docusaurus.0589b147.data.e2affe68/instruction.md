# Bug Report

### Describe the bug

I'm experiencing an issue with inline code rendering in markdown. When I use backticks in inline code blocks, the parser seems to get confused and doesn't properly close the code span.

### Reproduction

```markdown
This is `code with backticks` in text.
```

When parsing markdown with inline code that contains backtick characters, the code block doesn't get closed properly. The parser appears to exit the code text data state prematurely, before actually exiting the effects.

### Expected behavior

Inline code blocks should be parsed correctly and closed properly, even when they contain special characters like backticks. The parser should maintain the correct state transitions.

### Additional context

This seems to affect any inline code that uses backtick delimiters. The rendering breaks and subsequent text may be incorrectly treated as part of the code block or vice versa.

---
Repository: /testbed
