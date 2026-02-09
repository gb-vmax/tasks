# Bug Report

### Describe the bug

I'm experiencing an issue with footnote definition parsing in GFM (GitHub Flavored Markdown). When parsing footnote definitions, the marker tokens appear to be emitted in the wrong order, causing the AST structure to be malformed.

### Reproduction

```markdown
[^1]: This is a footnote definition
```

When parsing this footnote definition, the token events are not properly sequenced. The `gfmFootnoteDefinitionMarker` exit event happens after the `gfmFootnoteDefinitionLabelString` enter event, which breaks the expected nesting structure.

Expected token sequence:
1. Enter `gfmFootnoteDefinitionMarker`
2. Consume character
3. Exit `gfmFootnoteDefinitionMarker`
4. Enter `gfmFootnoteDefinitionLabelString`

Actual behavior:
The exit event for the marker occurs after entering the label string, creating an invalid token tree where nodes overlap incorrectly.

### Expected behavior

The tokenizer should emit events in the correct order so that all enter/exit pairs are properly nested without overlapping. This is critical for building a valid AST structure.

### System Info
- remark-gfm version: 4.0.0
- Node version: 18.x

---
Repository: /testbed
