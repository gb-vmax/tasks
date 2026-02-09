# Bug Report

### Describe the bug

I'm encountering a build failure after updating to the latest version. The bundler crashes during the chunk generation phase and fails to complete the build process. This seems to be related to chunk constructor initialization.

### Reproduction

```js
// rollup.config.js
export default {
  input: 'src/index.js',
  output: {
    file: 'dist/bundle.js',
    format: 'esm'
  }
}
```

When running the build, it fails immediately during the chunking phase. The error occurs regardless of the project configuration or module structure.

### Expected behavior

The build should complete successfully and generate the output bundle as configured.

### System Info
- Rollup version: latest
- Node version: 18.x
- OS: macOS

This is blocking our production builds. Any help would be appreciated!

---
Repository: /testbed
