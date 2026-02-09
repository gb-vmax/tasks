# Bug Report

### Describe the bug

I'm experiencing an issue with strikethrough rendering in MDX. It seems like the position information for strikethrough elements is being applied incorrectly, causing the generated output to have wrong source position data.

### Reproduction

```mdx
This is ~~strikethrough~~ text.
```

When processing this MDX content, the resulting HAST node for the strikethrough element has incorrect position information. The position data appears to be applied twice or in the wrong order, leading to unexpected behavior when trying to map back to source locations.

### Expected behavior

The strikethrough element should have accurate position information that correctly maps to the original source location in the MDX file. The position data should only be applied once and in the correct sequence.

### System Info
- @mdx-js/mdx version: 3.0.0
- Node version: Latest

---
Repository: /testbed
