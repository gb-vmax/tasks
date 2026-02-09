# Bug Report

### Describe the bug

I'm encountering an issue with `import.meta` properties where the wrong globals are being accessed depending on the format. It seems like file-related meta properties are not being handled correctly, causing incorrect behavior in the output.

### Reproduction

```js
// Using import.meta.ROLLUP_FILE_URL_referenceId in output
const fileUrl = import.meta.ROLLUP_FILE_URL_abc123;

// The generated code uses the wrong set of globals
// Expected: accessedFileUrlGlobals
// Actual: accessedMetaUrlGlobals
```

When checking the generated output, properties that should be using file URL globals are instead using meta URL globals, and vice versa.

### Expected behavior

When using `import.meta.ROLLUP_FILE_URL_*` or `import.meta.ROLLUP_FILE_OBJ_*` properties, the bundler should correctly identify these as file-related properties and use the appropriate `accessedFileUrlGlobals` for the output format. Other `import.meta` properties should use `accessedMetaUrlGlobals`.

### Additional context

This affects the generated code's runtime behavior as the wrong global variables are being referenced in the output bundle. The issue appears to be related to how the meta property prefix matching is being evaluated.

---
Repository: /testbed
