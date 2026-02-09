# Bug Report

### Describe the bug

I'm experiencing an issue with tree-shaking where modules seem to be getting included multiple times during the tree-shaking passes, causing unexpected behavior in the final bundle.

### Reproduction

When building a project with multiple tree-shaking passes, modules that have already been processed appear to be re-included in subsequent passes. This leads to:

1. Variable initializers being included more than once
2. Potential side effects being executed multiple times
3. Larger than expected bundle sizes

The issue seems to occur when:
- A module is marked as executed
- Multiple tree-shaking passes are required
- The module has variable initializers that should only be included once

### Expected behavior

Each module should only be included once during the tree-shaking process, regardless of how many passes are performed. Variable initializers should be processed exactly one time per module.

### System Info

- Rollup version: latest
- Node version: 18.x

Has anyone else run into this? It seems like the tree-shaking logic might not be properly tracking which modules have already been processed.

---
Repository: /testbed
