# Bug Report

### Describe the bug

I'm experiencing an issue with footnote definitions in GFM (GitHub Flavored Markdown) parsing. When a footnote definition is missing the colon (`:`) after the identifier, the parser seems to continue processing instead of properly rejecting the invalid syntax. Additionally, duplicate footnote identifiers are now being added to the defined list even when they already exist.

### Reproduction

```markdown
[^1] This should be invalid - missing colon after identifier

[^2]: First definition
[^2]: Duplicate definition - should not be added again
```

The parser accepts the first example without a colon when it should reject it. For the second example, the duplicate `[^2]` identifier gets added to the internal tracking list even though it already exists.

### Expected behavior

1. Footnote definitions without a colon after the identifier (e.g., `[^1]` instead of `[^1]:`) should be rejected as invalid syntax
2. Duplicate footnote identifiers should not be added to the defined list multiple times - only the first occurrence should be tracked

### System Info
- remark-gfm version: 4.0.0
- Node version: Latest

This seems like a regression as the validation was working correctly before. The parser should enforce proper footnote definition syntax and prevent duplicate identifier tracking.

---
Repository: /testbed
