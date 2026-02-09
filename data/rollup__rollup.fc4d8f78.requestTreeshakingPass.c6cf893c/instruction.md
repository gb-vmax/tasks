# Bug Report

### Describe the bug

I'm experiencing an issue with tree-shaking where the bundler seems to get stuck in an infinite loop or produces incorrect output. The build process either hangs or generates bundles with inconsistent results between runs.

### Reproduction

```js
// Create a module with exports that should be tree-shaken
export function usedFunction() {
  return 'used';
}

export function unusedFunction() {
  return 'unused';
}

// In another file, import only the used function
import { usedFunction } from './module';
console.log(usedFunction());
```

When bundling this code, the tree-shaking pass appears to behave erratically. Sometimes the build completes but includes code that should have been removed, other times it seems to hang indefinitely.

### Expected behavior

The bundler should:
1. Detect which exports are actually used
2. Remove unused code in a single tree-shaking pass
3. Complete the build process successfully

Instead, it seems like the tree-shaking logic is being triggered repeatedly or toggling between states.

### System Info
- Rollup version: latest
- Node version: 18.x
- OS: macOS

This issue appeared recently and I'm not sure what changed. Any help would be appreciated!

---
Repository: /testbed
