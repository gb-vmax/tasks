# Bug Report

### Describe the bug

Footnote references are generating incorrect IDs when the same footnote is referenced multiple times in a document. The first reference to a footnote is getting an unexpected suffix in its ID attribute.

### Reproduction

```markdown
Here is a sentence with a footnote[^1].

Here is another reference to the same footnote[^1].

[^1]: This is the footnote content.
```

When this is processed, the generated HTML for the first footnote reference has an ID like `fnref-1-1` instead of just `fnref-1`. The second reference correctly gets `fnref-1-2`.

### Expected behavior

The first reference to a footnote should have an ID without any numeric suffix (e.g., `fnref-1`). Only subsequent references to the same footnote should include the counter suffix (e.g., `fnref-1-2`, `fnref-1-3`, etc.).

Expected output:
- First reference: `id="fnref-1"`
- Second reference: `id="fnref-1-2"`

Actual output:
- First reference: `id="fnref-1-1"` ❌
- Second reference: `id="fnref-1-2"`

This breaks the expected linking behavior and makes the IDs inconsistent with standard footnote conventions.

---
Repository: /testbed
