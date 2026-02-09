# Bug Report

### Describe the bug

When using output options like `intro` and `banner`, empty strings are being incorrectly modified with newline characters appended to them. This results in unexpected whitespace being added to the generated bundle even when these options are not provided or are empty.

### Reproduction

```js
const bundle = await rollup({
  input: 'main.js',
  // ...
});

await bundle.generate({
  format: 'es',
  intro: '', // or undefined
  banner: '' // or undefined
});
```

The generated output will contain extra newlines at the beginning even though `intro` and `banner` are empty strings.

### Expected behavior

When `intro` or `banner` are empty strings or undefined, no additional newlines should be added to the output. The bundle should only include newlines when these options actually contain content.

### System Info
- Rollup version: latest
- Node version: 18.x

---
Repository: /testbed
