# Bug Report

### Describe the bug

I'm experiencing an issue with MDX ESM data processing where the output seems to be duplicated or incorrectly handled. When using ESM imports/exports in MDX files, the data appears to be processed twice during the exit phase instead of being properly entered and then exited.

### Reproduction

```mdx
---
export const metadata = {
  title: 'Test Page'
}
---

# My Page

Content here
```

When this MDX is processed, the ESM data handling seems off - it looks like the exit callback is being called twice or the enter/exit flow is not balanced correctly, leading to unexpected behavior in the generated output.

### Expected behavior

The ESM data should be processed with a proper enter/exit flow - entering the data processing phase and then exiting it cleanly. Currently it seems like the same operation is being called twice during what should be the exit phase.

### System Info
- @mdx-js/mdx version: 3.0.0
- Node version: 18.x

This might be related to recent changes in the ESM data handling logic. The issue manifests when MDX files contain export statements at the top.

---
Repository: /testbed
