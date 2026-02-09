# Bug Report

### Describe the bug

I'm encountering an issue with GFM (GitHub Flavored Markdown) footnote parsing where the AST structure for footnote definitions appears to be malformed. When parsing markdown with footnote definitions, the resulting syntax tree doesn't properly close the label node before exiting the definition node.

### Reproduction

```markdown
Here's a sentence with a footnote.[^1]

[^1]: This is the footnote content.
```

When parsing this markdown, the AST structure for the footnote definition seems incorrect - the label node isn't being properly entered/exited in the token stream, which causes issues when traversing or manipulating the syntax tree.

### Expected behavior

The footnote definition should have a properly structured AST with:
1. Enter `gfmFootnoteDefinitionLabel`
2. Exit `gfmFootnoteDefinitionLabel`
3. Exit `gfmFootnoteDefinition`

Currently it appears to be missing the enter event for the label node.

### System Info
- remark-gfm version: 4.0.0

---
Repository: /testbed
