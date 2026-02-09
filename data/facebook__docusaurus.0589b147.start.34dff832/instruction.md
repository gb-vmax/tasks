# Bug Report

### Describe the bug

I'm encountering an issue with directive parsing where line endings in multi-line directives are not being consumed correctly. The parser seems to be stuck in an infinite loop or behaving unexpectedly when processing directives that span multiple lines.

### Reproduction

```markdown
:::note
This is a multi-line
directive block
that should work
:::
```

When parsing the above directive, the tokenizer doesn't advance properly through the line endings. The code appears to enter the `lineEnding` state but doesn't actually consume the character before returning to the start state, causing the parser to get stuck.

### Expected behavior

Multi-line directives should be parsed correctly with each line ending properly consumed and the parser advancing to the next line. The `lineStart` function should be called after consuming the line ending character to check if the line is lazy.

### System Info
- remark-directive version: 3.0.0
- Node version: Latest

---
Repository: /testbed
