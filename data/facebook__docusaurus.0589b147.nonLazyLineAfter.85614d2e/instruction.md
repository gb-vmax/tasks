# Bug Report

### Describe the bug

I'm experiencing an issue with directive containers where lazy line continuation is not being handled correctly. When using container directives with multi-line content, the parser seems to be incorrectly marking lines as lazy/non-lazy, which causes unexpected parsing behavior.

### Reproduction

```markdown
:::note
This is a container directive
with multiple lines of content
that should be parsed correctly
:::
```

When parsing the above markdown with directive containers, the line continuation logic appears to be broken. Lines that should be treated as non-lazy are being marked as lazy (or vice versa), resulting in incorrect AST generation.

### Expected behavior

The parser should correctly identify which lines are lazy continuations and which are not. All lines within a container directive should be parsed as part of the directive's content block, maintaining proper line tracking throughout the parsing process.

### System Info
- remark-directive version: 3.0.0
- Parser: micromark-based

This seems to have broken recently and is affecting how nested content within directive containers is being processed. The line tracking mechanism appears to be using the wrong reference point when determining lazy line status.

---
Repository: /testbed
