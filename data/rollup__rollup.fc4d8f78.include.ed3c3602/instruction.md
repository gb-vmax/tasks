# Bug Report

### Describe the bug

I'm encountering an issue where `import.meta` properties are not being included in the bundle output. When using `import.meta.url` or other meta properties in my code, they're getting stripped out during the build process and don't appear in the final bundle.

### Reproduction

```js
// input.js
export function getModuleUrl() {
  return import.meta.url;
}

console.log('Module URL:', import.meta.url);
```

After bundling, the `import.meta.url` references are missing from the output, causing runtime errors when the code tries to access them.

### Expected behavior

The `import.meta` properties should be preserved in the bundle output. When I reference `import.meta.url` or other meta properties, they should appear in the generated code.

### System Info
- Rollup version: latest
- Node version: 18.x

---
Repository: /testbed
