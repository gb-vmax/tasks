# Bug Report

### Describe the bug

I'm experiencing an issue with UMD bundle generation when using namespaced global variables. The generated code appears to be malformed and doesn't correctly check for the existence of nested properties in the global scope.

### Reproduction

When building a UMD bundle with a namespaced global variable like `My.Nested.Library`, the generated safe access pattern in the output is broken. The resulting code doesn't properly chain the existence checks.

Example configuration:
```js
{
  output: {
    format: 'umd',
    name: 'My.Nested.Library',
    file: 'dist/bundle.js'
  }
}
```

After building, the generated UMD wrapper code for checking global variable existence appears incorrect - the property names are missing from the chained checks.

### Expected behavior

The generated code should properly check each level of the namespace exists before attempting to access the next level, similar to:
```js
typeof My !== 'undefined' && My.Nested && My.Nested.Library
```

Instead, the current output seems to be missing the actual property references in the chain.

### System Info
- Rollup version: latest
- Node version: 18.x

---
Repository: /testbed
