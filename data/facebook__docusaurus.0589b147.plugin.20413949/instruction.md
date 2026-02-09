# Bug Report

### Describe the bug

I'm experiencing an issue with heading ID extraction in MDX files. When using headings with inline formatting (like bold or italic text), the heading IDs are not being generated correctly. It seems like HTML/JSX nodes are being included when they should be filtered out for text extraction.

### Reproduction

```markdown
## This is a **bold** heading {#custom-id}
```

When processing this heading, the ID extraction doesn't work as expected. The text nodes that should be used for generating the slug appear to be filtered incorrectly.

Also noticed that headings without explicit IDs but containing inline formatting elements don't generate proper auto-slugs:

```markdown
## My *italic* heading
```

### Expected behavior

1. For headings with explicit IDs like `{#custom-id}`, the custom ID should be extracted and applied correctly, regardless of inline formatting
2. For headings without explicit IDs, the auto-generated slug should be based on the plain text content (excluding HTML/JSX nodes)
3. After ID extraction, the ID syntax should be properly removed from the heading text

### System Info
- Docusaurus version: latest
- MDX loader package: @docusaurus/mdx-loader

---
Repository: /testbed
