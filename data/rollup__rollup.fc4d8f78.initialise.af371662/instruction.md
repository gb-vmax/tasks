# Bug Report

### Describe the bug

I'm encountering an issue with tagged template expressions where the interaction tracking seems to be incorrect. When using tagged templates with member expressions, the context object isn't being properly tracked for side effects.

### Reproduction

```js
const obj = {
  method: function(strings, ...values) {
    // This should track obj as the receiver
    return strings[0];
  }
};

// Using tagged template with member expression
obj.method`template ${value}`;
```

The problem appears when the tag is a member expression - the interaction args don't seem to include the correct context, which affects side effect detection and tree-shaking behavior.

### Expected behavior

When a tagged template uses a member expression as the tag (like `obj.method`), the object (`obj`) should be properly tracked in the interaction arguments so that side effects are correctly detected. This is important for:
- Proper tree-shaking of unused code
- Correct side effect analysis
- Maintaining the right execution context

### Additional context

This seems to affect how the bundler determines whether certain code can be safely removed or reordered. In some cases, code that should be preserved is being eliminated, or vice versa.

---
Repository: /testbed
