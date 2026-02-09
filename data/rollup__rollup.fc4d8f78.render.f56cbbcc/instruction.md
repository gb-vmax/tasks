# Bug Report

### Describe the bug

When using `import.meta` properties in my code, they're not being transformed correctly during the build process. The `import.meta` references are appearing in the output bundle unchanged, which causes runtime errors in environments that don't support them natively.

### Reproduction

```js
// Input code
const url = import.meta.url;
const resolve = import.meta.resolve;

// After bundling, these are not being replaced/transformed
// Expected them to be converted to the appropriate format for the target output
```

### Expected behavior

`import.meta` properties should be properly transformed according to the output format. For example, `import.meta.url` should be replaced with the appropriate mechanism for the target environment (like `document.currentScript` for certain formats, or a relative URL mechanism).

### Additional context

This seems to have started happening recently. The build completes without errors, but the generated code contains raw `import.meta` references that fail at runtime in certain environments.

---
Repository: /testbed
