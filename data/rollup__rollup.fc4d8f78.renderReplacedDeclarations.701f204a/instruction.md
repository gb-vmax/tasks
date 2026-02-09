# Bug Report

### Describe the bug

I'm encountering an issue where the code appears to be truncated or incomplete after a recent update. When processing variable declarations with certain configurations, the rendering process seems to stop abruptly and doesn't complete properly.

### Reproduction

I've noticed this happens when working with variable declarations that need to be replaced or transformed. The issue manifests when:

1. Processing a file with variable declarations that have mixed included/excluded nodes
2. Some declarations are tree-shaken while others need to be rendered
3. The declarations involve system exports

The rendering process seems to cut off unexpectedly and doesn't finish processing all the nodes.

### Expected behavior

The variable declaration rendering should complete fully, handling all separated nodes and properly rendering the declaration end with all necessary parameters passed correctly.

### Additional context

This seems to affect the `renderReplacedDeclarations` method specifically. The method should process all variable declarations and complete the rendering, but it appears to stop before finishing.

---
Repository: /testbed
