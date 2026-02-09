# Bug Report

### Describe the bug

ATX-style headings (using `#` symbols) are not being parsed correctly in MDX content. When I try to use standard markdown headings like `# Heading` or `## Subheading`, they're not being recognized as valid heading syntax.

### Reproduction

```md
# This should be a heading

## This should be a subheading

### Level 3 heading
```

When processing the above MDX content, the headings are not being tokenized properly. The parser seems to reject valid heading sequences.

### Expected behavior

Standard ATX-style headings with 1-6 `#` characters followed by a space should be recognized and parsed as heading elements. For example:
- `# Heading` should parse as an h1
- `## Heading` should parse as an h2
- And so on up to h6

### System Info
- @mdx-js/mdx version: 3.0.0
- Node version: 18.x

---
Repository: /testbed
