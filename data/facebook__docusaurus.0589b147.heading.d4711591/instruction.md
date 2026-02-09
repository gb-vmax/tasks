# Bug Report

### Heading levels are off by one in MDX output

I've noticed that all heading levels in my MDX documents are being rendered one level deeper than expected. For example, `# Title` (which should be `<h1>`) is rendering as `<h2>`, `## Subtitle` is rendering as `<h3>`, and so on.

### Reproduction

```mdx
# This should be h1
## This should be h2
### This should be h3
```

When processed, the output is:
- `# This should be h1` → renders as `<h2>`
- `## This should be h2` → renders as `<h3>`
- `### This should be h3` → renders as `<h4>`

### Expected behavior

Headings should maintain their original depth:
- `#` should render as `<h1>`
- `##` should render as `<h2>`
- `###` should render as `<h3>`
- etc.

This appears to have started happening recently. All my document headings are now one level deeper than they should be, which breaks the semantic structure of the content.

---
Repository: /testbed
