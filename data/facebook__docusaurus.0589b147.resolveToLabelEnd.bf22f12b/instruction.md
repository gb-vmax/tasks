# Bug Report

### Describe the bug

I'm experiencing an issue with nested link parsing in MDX content. When I have a link inside another link-like construct (specifically with label images), the parser seems to be incorrectly handling the nesting and producing unexpected results.

### Reproduction

```markdown
[![alt text](image.png)](https://example.com)
```

When parsing this type of nested structure (an image link wrapped in a link), the output doesn't match what I'd expect. The link resolution appears to be broken - it's treating the structure incorrectly and not properly balancing the label constructs.

I've also noticed similar issues with other combinations of nested label structures where the parser seems to get confused about which tokens belong together.

### Expected behavior

The parser should correctly handle nested link/image constructs and properly resolve label boundaries. Image links wrapped in links should parse correctly with all parts properly associated.

### System Info
- @mdx-js/mdx version: 3.0.0
- Node version: 18.x

---
Repository: /testbed
