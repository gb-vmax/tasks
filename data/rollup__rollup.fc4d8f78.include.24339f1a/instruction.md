# Bug Report

### Describe the bug

When bundling code with nested function calls inside try-catch blocks, some code that should be included in the output bundle is being duplicated or incorrectly processed. The bundler appears to be recursively including children when it shouldn't be.

### Reproduction

```js
function outer() {
  try {
    inner();
  } catch (e) {
    // handle error
  }
}

function inner() {
  deeplyNested();
}

function deeplyNested() {
  console.log('test');
}
```

When bundling this code, the resulting output includes unexpected duplicate references or the tree-shaking behavior is not working as expected for the nested calls within try-catch blocks.

### Expected behavior

The bundler should correctly include each function only once and properly handle the call chain within try-catch statements without over-including or duplicating code.

### System Info
- Rollup version: latest
- Node version: 18.x

---
Repository: /testbed
