# Bug Report

### Describe the bug

Annotations are not being removed correctly from the generated code. After bundling, I'm seeing annotation comments still present in the output when they should have been stripped out.

### Reproduction

```js
// Input file with annotations
/**
 * @__PURE__
 */
function example() {
  return 42;
}

// After bundling, the annotation comment is still there
// Expected: annotation should be removed from output
```

When I inspect the bundled output, the `@__PURE__` and other annotation comments remain in the code instead of being stripped during the build process.

### Expected behavior

All annotation comments should be completely removed from the final bundle output. The generated code should not contain any of these special comment annotations.

### System Info
- Rollup version: latest
- Node version: 18.x

---
Repository: /testbed
