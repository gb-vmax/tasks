# Bug Report

### Describe the bug

After a recent update, heading elements in MDX files are not being rendered correctly. The headings appear to be completely broken or missing from the output.

### Reproduction

```mdx
# My Heading

This is some content below the heading.

## Subheading

More content here.
```

When this MDX is processed, the headings don't appear in the rendered output. It seems like the heading nodes are not being created properly.

### Expected behavior

Headings should render normally as they did before. All heading levels (h1-h6) should be converted to proper heading elements in the output.

### Additional context

This seems to have started happening after the latest update. Previously, headings were working fine. Not sure if this is related to any changes in the MDX compiler or if it's a regression.

---
Repository: /testbed
