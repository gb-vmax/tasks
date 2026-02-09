# Bug Report

### Describe the bug

I'm experiencing an issue with heading levels in MDX rendering. All headings are being rendered one level deeper than they should be. For example, `# Heading` (which should be `<h1>`) is being rendered as `<h2>`, `## Heading` (should be `<h2>`) becomes `<h3>`, and so on.

This is breaking the document outline structure and causing accessibility issues since the heading hierarchy is now incorrect.

### Reproduction

```mdx
# Main Title
## Subsection
### Sub-subsection
```

Expected HTML output:
```html
<h1>Main Title</h1>
<h2>Subsection</h2>
<h3>Sub-subsection</h3>
```

Actual HTML output:
```html
<h2>Main Title</h2>
<h3>Subsection</h3>
<h4>Sub-subsection</h4>
```

### Expected behavior

Headings should render at their correct semantic level:
- `#` should produce `<h1>`
- `##` should produce `<h2>`
- `###` should produce `<h3>`
- etc.

The heading depth from the markdown should map directly to the HTML heading tag number without any offset.

### System Info
- @mdx-js/mdx version: 3.0.0
- Node version: 18.x

---
Repository: /testbed
