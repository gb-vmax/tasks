# Bug Report

### Describe the bug

I'm experiencing an issue with logical expressions in bundled output where automatic semicolon insertion (ASI) is being handled incorrectly. When a logical expression gets tree-shaken and only one side remains, line breaks are being removed even when they should be preserved to prevent ASI issues.

### Reproduction

```js
// Input code with logical expression
const result = false || 
  someFunction()

// After bundling, the output incorrectly removes line breaks
// causing potential ASI problems
```

The issue occurs when:
1. A logical expression (using `||` or `&&`) has one branch that gets tree-shaken
2. The remaining expression is on a new line
3. Line breaks are being removed when `preventASI` is false, but should only be removed when `preventASI` is true

### Expected behavior

Line breaks should be preserved in the output to maintain proper ASI behavior. The bundler should only remove line breaks when explicitly told to prevent ASI (when `preventASI` is true), not the other way around.

### System Info

- Rollup version: latest
- Node version: 18.x

This seems to have started happening recently and is causing issues with code that relies on ASI. The logic appears to be inverted - line breaks are being removed in cases where they should be kept.

---
Repository: /testbed
