# Bug Report

### Describe the bug

I'm encountering an issue where empty imports are not being trimmed correctly from the dependency list. It appears that the last dependency with actual imports/reexports is being excluded from the output, and in some cases, dependencies that should be included are being skipped entirely.

### Reproduction

```js
// Given a list of dependencies where the last two are empty
const dependencies = [
  { imports: true, reexports: null },
  { imports: null, reexports: true },
  { imports: null, reexports: null },
  { imports: null, reexports: null }
]

// After trimming, expected to get the first 2 dependencies
// But actually getting only the first dependency
```

Also noticed that when all dependencies have imports/reexports except the very first one:

```js
const dependencies = [
  { imports: null, reexports: null },
  { imports: true, reexports: null },
  { imports: null, reexports: null }
]

// The function returns an incomplete result, missing valid dependencies
```

### Expected behavior

The function should return all dependencies up to and including the last one that has either imports or reexports, removing only the trailing empty ones.

### System Info
- Rollup version: latest
- Node version: 18.x

---
Repository: /testbed
