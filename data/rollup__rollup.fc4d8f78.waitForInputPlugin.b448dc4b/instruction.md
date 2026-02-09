# Bug Report

### Describe the bug

The `waitForInput` plugin is not properly waiting for the first input specifier. When multiple input specifiers are provided, the plugin skips checking the first one (index 0) and only waits for inputs starting from index 1.

### Reproduction

```js
// Configuration with multiple input specifiers
const config = {
  input: ['src/index.js', 'src/main.js', 'src/app.js'],
  plugins: [waitForInputPlugin()]
}

// If 'src/index.js' (the first input) doesn't exist yet,
// the plugin won't wait for it and will proceed immediately
// even though the file is missing
```

### Expected behavior

The plugin should wait for ALL input specifiers to be available before proceeding, including the first one in the array. Currently it only checks inputs starting from the second element.

### Additional context

This appears to affect scenarios where:
- Multiple entry points are specified
- The first entry point might not be available immediately
- You expect the build to wait for all inputs to be ready

The loop starts at index 1 instead of 0, which means the first input specifier is never checked.

---
Repository: /testbed
