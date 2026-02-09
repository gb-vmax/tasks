# Bug Report

### Describe the bug

I'm experiencing an issue where named exports are being registered twice in the module context. This causes duplicate export entries and leads to unexpected behavior when analyzing the module graph.

### Reproduction

```js
// example.js
export const foo = 'bar';
export function test() {
  return 42;
}
```

When this module is processed, the exports appear to be added to the context multiple times. This seems to happen during the initialization phase of export declarations.

### Expected behavior

Each named export should only be registered once in the module context, regardless of how the initialization process works internally.

### Additional context

This appears to be related to how export declarations are being initialized. The duplicate registration is causing issues with:
- Module dependency tracking
- Export name collision detection
- Tree-shaking analysis

The problem manifests when you have multiple named exports in a single file - they all get duplicated in the context.

---
Repository: /testbed
