# Bug Report

### Describe the bug

I'm experiencing an issue with MDX pragma comment handling and JSX runtime imports. After a recent update, it seems like the logic for detecting and removing pragma comments has been inverted, and there's also a problem with how import declarations are being replaced in the AST.

### Reproduction

When processing MDX files that contain JSX pragma comments, the comments are being incorrectly removed (or not removed when they should be). Additionally, the JSX runtime import replacement logic appears to be targeting the wrong index in the tree body, causing the wrong statement to be replaced.

This affects MDX files with structures like:
```mdx
/* @jsxRuntime classic */
import React from 'react'

export default function MyComponent() {
  return <div>Hello</div>
}
```

The pragma comment handling and import declaration replacement don't work as expected, leading to malformed output or runtime errors.

### Expected behavior

- Pragma comments should be correctly identified and removed when appropriate
- JSX runtime import declarations should be replaced at the correct position in the AST
- The transformed code should maintain proper structure and execute without errors

### Additional context

This seems to have started happening recently. The issue appears to be in the `recmaJsxBuild` function where it processes the tree comments and body declarations. The logic for checking pragma comments and the index used for replacing import declarations both seem off.

---
Repository: /testbed
