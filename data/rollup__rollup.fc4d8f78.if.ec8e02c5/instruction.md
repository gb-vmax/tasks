# Bug Report

### Entry modules not being included in bundle

I'm experiencing an issue where entry modules are not being included in the generated bundle. After building my project, the entry point module is missing from the output, which causes the application to fail at runtime.

### Reproduction

```js
// rollup.config.js
export default {
  input: 'src/main.js',
  output: {
    file: 'dist/bundle.js',
    format: 'es'
  }
}
```

When I run the build, the entry module (`src/main.js`) is not included in the final bundle even though it's specified as the input. The bundle generates but is missing the entry point code.

### Expected behavior

Entry modules should always be included in the bundle regardless of whether they are explicitly imported by other modules or not. The `isEntry` flag should be sufficient to include a module in the output.

### Additional context

This seems to have started happening recently. Previously, entry modules were always included in the bundle output. Now it appears that entry modules are only included if they also have dynamic importers, which doesn't seem right.

---
Repository: /testbed
