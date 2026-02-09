# Bug Report

### Describe the bug

I'm encountering an issue with `throw` statements in my bundled output. After bundling, the code is generating invalid JavaScript where the space after `throw` is being inserted in the wrong position, causing syntax errors.

### Reproduction

```js
// Input code
function test() {
  throw new Error('test');
}

// After bundling, the output has malformed throw statements
// The space is inserted at the wrong position in the code
```

When I try to run the bundled code, I get syntax errors because the `throw` statement is not properly formatted. It seems like the whitespace handling for throw statements is broken.

### Expected behavior

The bundler should generate valid JavaScript with properly formatted `throw` statements. The space between `throw` and the argument should be correctly placed.

### System Info
- Rollup version: latest
- Node version: 18.x

This is blocking my production build. Any help would be appreciated!

---
Repository: /testbed
