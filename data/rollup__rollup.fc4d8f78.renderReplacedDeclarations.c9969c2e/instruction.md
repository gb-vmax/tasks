# Bug Report

### Describe the bug

I'm encountering a build failure when bundling my project. The build process crashes with an error indicating that a variable is being referenced before it's defined. This appears to be happening during the code generation phase when processing variable declarations.

### Reproduction

```js
// Example code that triggers the issue
const { a, b } = someObject;
export { a };

// Or with destructuring in variable declarations
let x, y = getValue();
export { x, y };
```

When bundling code with variable declarations that involve exports, the build fails unexpectedly. The error seems to be related to how the bundler is handling the rendering of these declarations.

### Expected behavior

The code should bundle successfully without errors. Variable declarations with exports should be processed and rendered correctly in the output bundle.

### System Info
- Rollup version: latest
- Node version: 18.x
- OS: macOS

The build was working fine before, but now it consistently fails when processing files with certain variable declaration patterns. Any help would be appreciated!

---
Repository: /testbed
