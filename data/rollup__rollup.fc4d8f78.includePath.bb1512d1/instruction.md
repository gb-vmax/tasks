# Bug Report

### Describe the bug

I'm experiencing an issue where identifiers are not being properly included in the module graph. When an identifier is referenced, it seems like the inclusion logic is inverted - identifiers that should be included are being skipped, and the path inclusion is happening at the wrong time.

### Reproduction

```js
// Create a module with an identifier reference
const code = `
export function test() {
  return someVariable.property;
}
`;

// The identifier 'someVariable' should be included in the module
// but it's not being tracked correctly
```

When the identifier is first encountered, it should be marked as included and the variable should be added to the module context. However, the current behavior seems to be doing the opposite.

### Expected behavior

When `includePath` is called on an identifier:
1. If not yet included, it should mark itself as included, apply deoptimizations, and include the variable in the module
2. If already included and there's a path to follow, it should delegate to the variable's includePath

### System Info
- Rollup version: latest
- Node version: 18.x

This appears to be affecting tree-shaking and module inclusion logic. Variables that should be included are being excluded from the final bundle.

---
Repository: /testbed
