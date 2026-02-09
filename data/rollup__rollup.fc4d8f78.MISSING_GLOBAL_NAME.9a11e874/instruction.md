# Bug Report

### Describe the bug
When there's a single missing global variable name warning, the warning message displays incorrect grammar ("names" instead of "name"), and the actual warning details are not being shown in the output.

### Reproduction
```js
// rollup.config.js
export default {
  input: 'src/index.js',
  output: {
    format: 'iife',
    file: 'dist/bundle.js'
  },
  external: ['jquery']
  // Note: missing output.globals configuration
}
```

When building with this configuration where an external module lacks a global name mapping, the CLI output shows:
- Incorrect pluralization in the warning title
- No warning details are printed (the list of missing globals is empty)

### Expected behavior
The warning should:
1. Use correct singular/plural form ("name" for 1 warning, "names" for multiple)
2. Display the actual missing global variable information, including the module ID and guessed name

### System Info
- Rollup version: latest
- Node version: 18.x

---
Repository: /testbed
