# Bug Report

### Describe the bug

I'm encountering an issue with the rehype-stringify vendor code where the handler lookup logic seems to be checking the wrong object. When processing nodes, the code is checking if `handlers` has the `key2` property instead of checking if the `value` object has it, which causes the handler selection to fail.

### Reproduction

```js
// When zwitch processes a node with a specific type
const processor = zwitch('type', {
  handlers: {
    element: handleElement,
    text: handleText
  }
});

// Processing a node fails because the condition checks handlers instead of value
const node = {
  type: 'element',
  tagName: 'div',
  children: []
};

processor(node); // Handler lookup doesn't work as expected
```

### Expected behavior

The handler should be selected based on whether the input `value` object has the `key2` property (e.g., 'type'), not whether the `handlers` object has it. The correct handler should be invoked based on the value's type property.

### System Info
- rehype-stringify version: 10.0.0
- Node version: Latest

This looks like it might have been introduced in a recent change to the zwitch implementation in the vendored code.

---
Repository: /testbed
