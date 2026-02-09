# Bug Report

### Describe the bug

After a recent update, I'm encountering issues with directive parsing. The directives seem to be initialized with incorrect structure - specifically, the `children` property appears to be set to `null` instead of an empty array, which causes problems when trying to add child nodes.

### Reproduction

```js
const directive = {
  type: 'textDirective',
  name: 'myDirective',
  attributes: {},
  children: null  // This should be an array
}

// Attempting to add children fails
directive.children.push(childNode)  // TypeError: Cannot read property 'push' of null
```

### Expected behavior

Directives should be initialized with an empty `children` array (`[]`) so that child nodes can be added without errors. The structure should allow for standard array operations on the children property.

### System Info
- remark-directive version: 3.0.0
- Node version: Latest

---
Repository: /testbed
