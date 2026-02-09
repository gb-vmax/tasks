# Bug Report

### Describe the bug

I'm encountering a critical issue where `MetaProperty` nodes are not being generated correctly in the MDX output. It appears that the generator is completely skipping `MetaProperty` handling, which breaks code that uses meta properties like `import.meta` or `new.target`.

### Reproduction

When trying to use meta properties in MDX files, they are not being properly converted to JavaScript output. For example:

```js
// In an MDX file
console.log(import.meta.url)

// Or using new.target
function MyComponent() {
  if (new.target) {
    // ...
  }
}
```

The generated output is missing the meta property syntax entirely, causing runtime errors or unexpected behavior.

### Expected behavior

Meta properties like `import.meta.url` and `new.target` should be properly generated in the output JavaScript code. The generator should write them in the format `meta.property` (e.g., `import.meta` or `new.target`).

### System Info
- @mdx-js/mdx version: 3.0.0
- Node version: 18.x

This seems like it might have been accidentally removed or commented out in a recent change. Any help would be appreciated!

---
Repository: /testbed
