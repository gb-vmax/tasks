# Bug Report

### Describe the bug

I'm encountering an issue with MDX JSX tag parsing where tag names appear to be getting duplicated or concatenated incorrectly. When parsing MDX content with JSX tags, the tag name seems to be accumulating values instead of being set properly.

### Reproduction

```js
// When parsing MDX content with JSX tags like:
<MyComponent />

// The tag name appears to be processed incorrectly, 
// potentially resulting in duplicated or concatenated names
// instead of just "MyComponent"
```

### Expected behavior

The parser should correctly extract and set the tag name to just the primary name (e.g., `MyComponent`) without any duplication or concatenation of previous values.

### Additional context

This seems to be related to how the `exitMdxJsxTagNamePrimary` function handles the tag name assignment. The tag name should be a simple string representing the component name, but it appears the current implementation may be preserving or concatenating previous state.

---
Repository: /testbed
