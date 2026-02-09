# Bug Report

### Describe the bug

When I get a `MISSING_GLOBAL_NAME` warning from Rollup, the first warning in the batch is not being displayed in the console output. Only subsequent warnings after the first one are shown.

### Reproduction

Set up a build configuration that triggers multiple `MISSING_GLOBAL_NAME` warnings (e.g., multiple external dependencies without global names specified):

```js
// rollup.config.js
export default {
  input: 'src/index.js',
  external: ['react', 'lodash', 'moment'],
  output: {
    file: 'dist/bundle.js',
    format: 'iife'
    // intentionally not specifying output.globals
  }
}
```

When running the build, you'll notice that only 2 out of 3 missing global name warnings are displayed in the console. The first external module that should trigger a warning is missing from the output.

### Expected behavior

All missing global name warnings should be displayed in the console, including the first one. If there are 3 external modules without global names, all 3 should be shown with their guessed global variable names.

### System Info
- Rollup version: latest
- Node version: 18.x

---
Repository: /testbed
