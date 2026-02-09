# Bug Report

### Describe the bug

When using explicit heading IDs in Markdown with the `{#id}` syntax, the heading text is not being properly stripped when there's only a single text node. The original full heading string (including the ID syntax) is being preserved instead of just the text portion.

### Reproduction

```markdown
# My Heading {#custom-id}
```

When processing this heading with a single text node, the heading text should be "My Heading" but instead it remains as "My Heading {#custom-id}".

This works correctly when the heading has multiple child nodes (e.g., with emphasis or bold):

```markdown
# My *Heading* {#custom-id}
```

But fails when it's a simple single-node heading.

### Expected behavior

For a heading like `# My Heading {#custom-id}`, the processed heading text should be "My Heading" with the ID set to "custom-id", regardless of whether the heading has single or multiple child nodes.

### System Info
- Docusaurus MDX Loader
- Issue occurs with simple single-node headings using explicit ID syntax

---
Repository: /testbed
