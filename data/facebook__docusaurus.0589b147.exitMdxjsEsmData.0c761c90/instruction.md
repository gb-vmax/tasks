# Bug Report

### Describe the bug

I'm experiencing an issue with MDX ESM blocks where the data appears to be processed incorrectly. When using ESM imports/exports in MDX files, the content seems to be getting duplicated or handled in an unexpected way.

### Reproduction

```mdx
---
export const metadata = {
  title: 'Test Page'
}
---

# Hello World

Some content here
```

When this MDX is processed, the ESM data handling seems off - it's like the exit handler is being called twice on the same data, which causes weird behavior in the output.

### Expected behavior

ESM blocks in MDX should be processed cleanly with proper enter/exit handling. The data should only be processed once during the exit phase.

### System Info
- @mdx-js/mdx version: 3.0.0
- Node version: 18.x

---
Repository: /testbed
