# Bug Report

### Describe the bug

I'm experiencing an issue where modules that should not be included in the bundle are being added anyway. This is causing the bundle to contain unnecessary code and increase the overall bundle size.

### Reproduction

```js
// Create a module that is not included and not an entry point
// The module should not appear in the final bundle, but it does

// Example scenario:
// - Module A is the entry point
// - Module B is imported conditionally but tree-shaken out
// - Module B appears in the bundle even though it's not used
```

When building a project with tree-shaking enabled, modules that have been marked as not included (due to tree-shaking) are still appearing in the final bundle output. This seems to affect modules that:
- Are not entry points
- Have been tree-shaken (not included)
- Don't have dynamic importers

### Expected behavior

Only modules that are actually used should be included in the bundle. Modules that have been tree-shaken out should not appear in the final output.

### System Info
- Rollup version: latest
- Node version: 18.x

---
Repository: /testbed
