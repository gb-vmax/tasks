# Bug Report

### Describe the bug

I'm experiencing an issue with MDX ESM block parsing where the node stack appears to be in an incorrect state during processing. When working with MDX files that contain ESM import/export statements, the parser seems to be accessing nodes before properly exiting the token context.

### Reproduction

```mdx
---
title: Test
---

import { Component } from './component'

export const meta = {
  author: 'test'
}

# Content here

<Component />
```

When parsing MDX files with ESM blocks (imports/exports), the internal node stack state becomes inconsistent. The issue manifests when the parser tries to access the current node in the stack before the token exit has been properly handled.

### Expected behavior

The parser should maintain a consistent stack state throughout the parsing process. The current node should be accessible in the correct state after resuming and before performing operations on it.

### Additional context

This seems to be related to the order of operations in the `exitMdxjsEsm` function where node access and token exit are not properly sequenced. The node should be in the correct state when accessed from the stack.

---
Repository: /testbed
