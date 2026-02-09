# Bug Report

### Describe the bug

I'm encountering an issue with sourcemap generation where placeholder replacement seems to be happening in the wrong order or not at all. The sourcemap file reference gets updated after being emitted, which causes the emitted sourcemap to have incorrect file references.

Additionally, for non-hashed chunks, the code placeholders are not being replaced when they should be. It looks like the condition for when to apply placeholder replacement is inverted - placeholders are only replaced when there are NO hashes available, but they should be replaced when hashes ARE available.

### Reproduction

```js
// Build configuration with hashed output and sourcemaps enabled
{
  output: {
    file: 'bundle-[hash].js',
    sourcemap: true
  }
}

// After building:
// 1. The generated sourcemap file contains placeholder values instead of actual hashes
// 2. Non-hashed chunks retain their placeholders in the code instead of having them replaced
```

### Expected behavior

- Sourcemap file references should be updated with hash placeholders BEFORE the sourcemap is emitted
- Code placeholders should be replaced when hashes are available (size > 0), not when they're unavailable (size === 0)
- The final output should contain properly resolved hash values in both the code and sourcemap references

### System Info
- Rollup version: latest
- Node version: 18.x

---
Repository: /testbed
