# Bug Report

### Describe the bug

Footnote definitions are not being parsed correctly in GFM markdown. The parser seems to be looking for the wrong character when processing footnote definition markers, causing valid footnote syntax to be rejected.

### Reproduction

```markdown
[^1]: This is a footnote definition
[^note]: Another footnote with a longer identifier
```

When parsing the above markdown, the footnote definitions are not recognized. The parser appears to be checking for an incorrect delimiter character after the footnote identifier.

### Expected behavior

Footnote definitions should be properly parsed and recognized when using the standard GFM syntax with a colon (`:`) after the footnote identifier in square brackets.

For example:
```markdown
[^1]: This should work
```

Should be parsed as a valid footnote definition.

### Additional context

This seems to have started recently. The footnote syntax was working fine before, but now valid footnote definitions are being ignored by the parser.

---
Repository: /testbed
