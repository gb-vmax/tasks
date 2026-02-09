# Bug Report

### Describe the bug

I'm encountering an issue with `import.meta` file references where the file name resolution appears to be incorrect. When using `import.meta` with file-related properties, the referenced file names are not being resolved properly.

### Reproduction

```js
// In my bundler configuration
export default {
  plugins: [
    {
      resolveImportMeta(property, { chunkId, moduleId }) {
        if (property === 'ROLLUP_FILE_URL_referenceId') {
          return `'file-url'`;
        }
      }
    }
  ]
}

// In source code
const fileUrl = import.meta.ROLLUP_FILE_URL_someId;
```

The file name resolution seems to be behaving unexpectedly - it's either returning file names when it shouldn't, or the slicing of the property prefix is incorrect.

### Expected behavior

`import.meta` file references should only resolve file names for valid import meta properties, and the property prefix should be correctly stripped when getting the file name.

### System Info
- Rollup version: latest
- Node version: 18.x

---
Repository: /testbed
