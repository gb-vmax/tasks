# Bug Report

### Describe the bug

When using emphasis/italic markdown syntax (with `*` or `_`), the content inside the emphasis tags is not being rendered correctly. The emphasized text appears to be missing or empty in the output.

### Reproduction

```markdown
This is *emphasized text* in a sentence.
```

Expected HTML output:
```html
<p>This is <em>emphasized text</em> in a sentence.</p>
```

Actual output:
```html
<p>This is <em></em> in a sentence.</p>
```

The `<em>` tag is generated but the children/content is missing.

### Steps to reproduce
1. Parse markdown with emphasis syntax (e.g., `*text*` or `_text_`)
2. Convert to HTML
3. Notice that the emphasized content is not present in the output

This seems to have started happening recently. Basic text rendering works fine, but any emphasis formatting loses its content during the conversion process.

### Expected behavior
The text wrapped in emphasis markers should appear inside the `<em>` tags in the HTML output.

---
Repository: /testbed
