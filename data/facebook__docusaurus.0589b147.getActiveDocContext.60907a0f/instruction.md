# Bug Report

### Describe the bug

I'm experiencing an issue with the active doc detection in versioned docs. When navigating to a document page, the active version is being incorrectly included in the `alternateDocVersions` object, which should only contain versions *other than* the currently active one.

### Reproduction

```js
// Given a docs setup with multiple versions (e.g., 1.0.0, 2.0.0, 3.0.0)
// When viewing a document in version 2.0.0

const context = getActiveDocContext(data, pathname);

// The alternateDocVersions object incorrectly includes the current version
console.log(context.alternateDocVersions);
// Expected: { '1.0.0': {...}, '3.0.0': {...} }
// Actual: { '1.0.0': {...}, '2.0.0': {...}, '3.0.0': {...} }
```

### Expected behavior

The `alternateDocVersions` should only contain alternative versions of the current document, not the currently active version itself. This is causing issues with version switcher components that show the current version as an "alternate" option.

### Additional context

This seems to affect any multi-versioned documentation site. The current version should be excluded from the alternates list to avoid confusion in the UI.

---
Repository: /testbed
