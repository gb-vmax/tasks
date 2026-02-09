# Bug Report

### Describe the bug

I'm experiencing an issue with footnote parsing in GFM (GitHub Flavored Markdown). When using footnote calls in markdown content, the parser seems to be processing the marker tokens in the wrong order, which causes unexpected behavior in the generated AST.

### Reproduction

```markdown
Here's some text with a footnote[^1].

[^1]: This is the footnote content.
```

When parsing this markdown, the footnote call `[^1]` doesn't get processed correctly. The token events appear to be firing out of sequence - specifically, the `gfmFootnoteCallMarker` exit event seems to occur after the `gfmFootnoteCallString` enter event, which breaks the expected nesting structure.

### Expected behavior

The parser should properly handle footnote calls with the correct token event ordering. The marker should be fully processed (both enter and exit events) before moving on to the string content parsing.

### Additional context

This appears to affect the internal token stream generation. The AST structure for footnote calls ends up malformed because the marker exit happens too late in the sequence.

---
Repository: /testbed
