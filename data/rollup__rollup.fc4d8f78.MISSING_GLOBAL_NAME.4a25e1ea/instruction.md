# Bug Report

### Describe the bug

When Rollup detects missing global variable names for external modules, the warning message displays incorrect information. The pluralization logic seems off (checking `> 0` instead of `> 1`), and more importantly, the guessed global name being shown is wrong - it's trying to access the second element of the names array instead of the first one.

### Reproduction

```js
// Create a build configuration with an external module
// that doesn't have a global name specified

export default {
  input: 'src/main.js',
  external: ['lodash'],
  output: {
    format: 'iife',
    file: 'dist/bundle.js',
    // Missing globals configuration
  }
}
```

When building, the warning message will show:
- Incorrect singular/plural form (always shows "names" even for a single warning)
- Wrong guessed global name (shows undefined or the wrong array element)

### Expected behavior

The warning should:
1. Correctly pluralize based on the number of warnings (singular for 1, plural for 2+)
2. Display the first guessed global name from the names array, not the second one

### System Info
- Rollup version: latest
- Node version: 18.x

---
Repository: /testbed
