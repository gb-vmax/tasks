# Bug Report

### Describe the bug

I'm experiencing an issue where object expressions with side effects are not being properly detected during tree-shaking. The bundler seems to be calling `hasEffectsOnInteractionAtPath` multiple times unnecessarily, which is causing performance issues in my build.

### Reproduction

```js
// Input code
const obj = {
  get value() {
    console.log('side effect');
    return 42;
  }
};

// When accessing obj.value, the side effect check
// appears to be running twice
```

The build process is noticeably slower when dealing with large codebases that have many object expressions with getters or methods that have side effects.

### Expected behavior

The side effect analysis should only evaluate each path once per interaction. Currently it seems like the same check is being performed redundantly, leading to slower build times.

### System Info
- Rollup version: latest
- Node version: 18.x
- OS: macOS

---
Repository: /testbed
