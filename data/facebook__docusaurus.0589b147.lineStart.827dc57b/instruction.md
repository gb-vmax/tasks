# Bug Report

### Describe the bug

I'm experiencing an issue with directive parsing in markdown content. When using leaf directives (like `::directive`) inside lazy continuation lines (lines that continue a previous block without explicit markers), the parser is accepting them when it should be rejecting them, or vice versa.

### Reproduction

```markdown
> This is a blockquote
::myDirective
Content here
```

or

```markdown
- List item
  ::directive
  More content
```

The directive parsing behavior seems inverted - directives that should be parsed in lazy continuation contexts are being rejected, while those that should be rejected are being accepted.

### Expected behavior

Directives should be properly handled based on whether they appear in lazy continuation lines. The parser should correctly identify when a line is a lazy continuation and handle directives accordingly.

### Additional context

This affects how directives interact with block-level elements like blockquotes and lists. The parsing logic appears to have the condition backwards, causing incorrect behavior when directives are nested within these structures.

---
Repository: /testbed
