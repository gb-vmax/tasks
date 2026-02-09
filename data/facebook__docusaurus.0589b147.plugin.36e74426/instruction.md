# Bug Report

### Describe the bug

I'm experiencing an issue with heading ID extraction from markdown content. When I have headings with custom IDs (using the `{#id}` syntax), the text content is being incorrectly parsed and the heading structure gets corrupted.

### Reproduction

```markdown
## My Heading *with emphasis* and text {#custom-id}
```

When processing this heading, the parser seems to be filtering the wrong nodes and accessing incorrect indices. The heading text gets mangled and sometimes parts of it disappear entirely.

Another case that breaks:

```markdown
### Simple Heading {#my-id}
```

The ID extraction logic appears to be looking at the wrong child node (accessing `length - 2` instead of the last node), which causes the heading content to be incorrectly modified.

### Expected behavior

- The heading text should be preserved correctly (minus the `{#id}` part)
- The custom ID should be extracted properly
- Emphasized or formatted text within headings should remain intact
- When the last part only contains the ID, that node should be removed cleanly

### System Info

- Package: @docusaurus/mdx-loader
- Node version: 18.x

This seems to have broken recently - headings with custom IDs used to work fine but now they're getting corrupted during processing.

---
Repository: /testbed
