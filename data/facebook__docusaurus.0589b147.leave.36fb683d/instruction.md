# Bug Report

### Describe the bug

I'm experiencing an issue where JSX transformation appears to be incomplete or truncated. When processing MDX files, the build process seems to cut off in the middle of handling JSX elements, specifically during the `leave` function that processes JSX nodes.

### Reproduction

This seems to happen when:
1. Processing MDX files with JSX elements
2. The transformation reaches the JSX element handling logic
3. The code appears to stop executing partway through the JSX text node processing

I noticed this after a recent update. The JSX import statements are being added correctly, but the actual JSX element transformation logic seems incomplete.

### Expected behavior

The JSX transformation should complete fully, processing all JSX elements, fragments, and text nodes properly. The `leave` function should handle all node types correctly and generate the appropriate runtime calls.

### System Info
- @mdx-js/mdx version: 3.0.0
- Node version: Latest

Has anyone else encountered this? It seems like the transformation logic got cut off somehow.

---
Repository: /testbed
