# Bug Report

### Describe the bug

I'm experiencing an issue with `replaceSubstitutions` where variable substitution order appears to be reversed. Variables passed later in the arguments list are being overridden by earlier ones, which is the opposite of what I'd expect.

### Reproduction

```js
const template = "Hello {{name}}, you are {{age}} years old";

const result = Property.replaceSubstitutions(
  template,
  { name: "Alice", age: 25 },
  { name: "Bob", age: 30 }
);

// Expected: "Hello Bob, you are 30 years old"
// Actual: "Hello Alice, you are 25 years old"
```

### Expected behavior

When multiple variable objects are provided, later arguments should take precedence over earlier ones (like how `Object.assign` works). In the example above, the second object with `name: "Bob"` should override the first object's `name: "Alice"`.

### Additional context

This seems like it might be related to how the variables are being merged internally. The behavior is inconsistent with typical JavaScript patterns where rightmost values win in merge operations.

---
Repository: /testbed
