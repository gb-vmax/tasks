# Bug Report

### Describe the bug

I'm encountering a build failure when trying to bundle my project. The bundler seems to crash during the chunk generation phase without providing a clear error message. This appears to be related to how chunks are being constructed.

### Reproduction

```js
// rollup.config.js
export default {
  input: 'src/index.js',
  output: {
    dir: 'dist',
    format: 'esm'
  }
}
```

When running the build, the process fails immediately during chunk creation. The build was working fine before, but after updating to the latest version it now crashes consistently.

### Expected behavior

The bundler should successfully create chunks and complete the build process without crashing.

### System Info
- Node version: 18.x
- OS: macOS

Any help would be appreciated!

---
Repository: /testbed
