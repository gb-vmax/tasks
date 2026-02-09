# Bug Report

### Describe the bug

I'm encountering an issue with directive parsing where whitespace handling appears to be broken. When processing markdown directives, spaces that should be recognized and consumed are being skipped, causing the parser to fail on valid directive syntax.

### Reproduction

```markdown
::directive[content with spaces]

:directive{key="value with spaces"}
```

When parsing directives with whitespace, the parser doesn't properly enter the whitespace handling state. This causes directives that contain spaces to either fail parsing or produce incorrect AST nodes.

### Expected behavior

The parser should correctly handle whitespace within directives. Spaces should be properly consumed and the directive content should be parsed accurately regardless of internal spacing.

### Additional context

This seems to affect all directive types (text, leaf, and container directives) when they contain whitespace in their content or attributes. The issue appears to be in the space tokenization logic.

---
Repository: /testbed
