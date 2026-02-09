# Bug Report

### Describe the bug

I'm encountering an issue with footnote definitions in GFM (GitHub Flavored Markdown) parsing. When parsing markdown with footnote definitions, they seem to be getting treated as footnote references instead, which breaks the document structure.

### Reproduction

```markdown
Here's some text with a footnote[^1].

[^1]: This is the footnote definition.
```

When parsing this markdown, the footnote definition `[^1]: This is the footnote definition.` appears to be incorrectly identified in the AST. The definition should have a `type` of `"footnoteDefinition"` and include `children` for its content, but it's being created as something else.

### Expected behavior

Footnote definitions should be properly recognized and parsed with:
- Correct type identifier for definitions vs references
- Proper structure including children nodes for the definition content
- Ability to distinguish between where a footnote is used (reference) and where it's defined (definition)

### Additional context

This seems to affect the entire footnote system since definitions and references serve completely different purposes in the document structure. References point to footnotes while definitions contain the actual footnote content.

---
Repository: /testbed
