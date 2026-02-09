# Bug Report

### Describe the bug

I'm experiencing an issue where code removal during tree-shaking is leaving behind extra characters in the output. It appears that one character at the end of removed nodes is not being properly eliminated from the generated code.

### Reproduction

When tree-shaking removes unused code blocks, the last character of the removed section remains in the output. This causes syntax errors or unexpected characters in the final bundle.

For example, if a function or statement should be completely removed:
```js
function unusedFunction() {
  return 42;
}
```

After tree-shaking, instead of being completely removed, there's a trailing character left behind (like `}` or `;`), which breaks the generated code.

### Expected behavior

When a node is tree-shaken and removed from the code, it should be completely eliminated without leaving any trailing characters. The removal should be clean and not affect the syntax of the remaining code.

### Additional context

This seems to affect any code that gets removed during the tree-shaking process. The issue manifests as unexpected characters appearing in the bundled output where removed code used to be.

---
Repository: /testbed
