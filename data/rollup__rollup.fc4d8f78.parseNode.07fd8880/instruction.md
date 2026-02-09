# Bug Report

### Describe the bug

I'm encountering an issue with class declarations that have an `id` (name). When a class declaration includes a name, it seems to fail during parsing or rendering. The behavior is inverted from what it should be - classes without names work fine, but named classes cause problems.

### Reproduction

```js
// This causes issues
class MyClass {
  constructor() {
    this.value = 1;
  }
}

// Anonymous classes seem to work
export default class {
  constructor() {
    this.value = 1;
  }
}
```

### Expected behavior

Named class declarations should parse and process correctly. The class name should be properly handled and the declaration should work as expected in the bundled output.

### Additional context

This appears to be a regression as named classes were working correctly in previous versions. The issue specifically affects class declarations with an identifier, while anonymous class declarations continue to work without problems.

---
Repository: /testbed
