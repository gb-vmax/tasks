# Bug Report

### Describe the bug

I'm encountering an issue with `import.meta` file references not being resolved correctly. When using `import.meta.ROLLUP_FILE_URL_*` in my code, the referenced file names are not being extracted properly, causing the build to fail or produce incorrect output.

### Reproduction

```js
// In my source code
const assetUrl = import.meta.ROLLUP_FILE_URL_12345;
```

When bundling, the file reference isn't being resolved correctly. The generated output doesn't include the proper file reference, and I'm getting unexpected behavior with asset URLs.

### Expected behavior

The `import.meta.ROLLUP_FILE_URL_*` syntax should correctly resolve to the emitted file's URL. The file reference should be properly extracted and the corresponding file name should be retrieved from the output plugin driver.

### System Info
- Rollup version: latest
- Node version: 18.x

This seems to have started happening recently. Previously, these file references were working as expected.

---
Repository: /testbed
