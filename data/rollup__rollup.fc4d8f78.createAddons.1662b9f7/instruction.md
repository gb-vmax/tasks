# Bug Report

### Describe the bug

I'm experiencing an issue with the generated bundle output where the `outro` section is not being included in the final output. When I define an outro in my rollup configuration, it simply doesn't appear in the bundled file, even though it should be appended at the end.

### Reproduction

```js
// rollup.config.js
export default {
  input: 'src/index.js',
  output: {
    file: 'dist/bundle.js',
    format: 'esm',
    outro: '// End of bundle'
  }
}
```

After building, the expected outro comment is missing from the output file. The banner, intro, and footer sections work fine, but outro is completely absent.

### Expected behavior

The outro text should be appended to the end of the generated bundle file, similar to how banner, intro, and footer are handled.

### System Info
- Rollup version: latest
- Node version: 18.x

---
Repository: /testbed
