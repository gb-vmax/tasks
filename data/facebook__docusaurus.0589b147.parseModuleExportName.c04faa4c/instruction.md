# Bug Report

### Describe the bug

I'm encountering a critical issue after a recent update where MDX parsing completely fails when trying to use module export names. The parser seems to be missing a required function and throws an error about `parseModuleExportName` not being defined.

### Reproduction

```js
// Any MDX file with named exports fails to parse
export { MyComponent as default } from './Component'

// Or using string literals as export names
export { "my-component" as MyComponent }
```

When trying to parse these MDX files, the parser crashes because it can't find the `parseModuleExportName` method.

### Expected behavior

MDX files with module exports (especially those using string literals as export names per ES2022 spec) should parse correctly without throwing errors. The parser should handle both identifier-based and string literal export names.

### System Info
- remark-mdx version: 3.0.0
- Node version: Latest LTS

This seems to have broken after the most recent changes. Any MDX content with exports is now completely unusable. Would appreciate a quick fix as this is blocking our entire documentation pipeline!

---
Repository: /testbed
