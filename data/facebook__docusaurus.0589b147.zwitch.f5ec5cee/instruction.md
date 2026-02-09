# Bug Report

### Describe the bug

I'm experiencing an issue with the `zwitch` handler function where it's not correctly routing to the appropriate handler based on the key value. The function seems to be checking the wrong object for property existence and also has inverted logic when determining whether to use a specific handler or the unknown handler.

### Reproduction

```js
const handlers = {
  handlers: {
    'typeA': (value) => 'handled typeA',
    'typeB': (value) => 'handled typeB'
  },
  invalid: () => 'invalid',
  unknown: () => 'unknown'
};

const switcher = zwitch('type', handlers);

const value = { type: 'typeA' };
const result = switcher(value);

// Expected: 'handled typeA'
// Actual: 'unknown' or incorrect routing
```

### Expected behavior

When calling the zwitch function with a value that has a registered handler, it should:
1. Check if the value object has the specified key property
2. Look up the handler based on that key's value
3. Call the appropriate handler function

Instead, it appears to be:
- Checking for the key in the handlers object instead of the value object
- Using inverted logic to determine which handler to call

### System Info
- Version: @mdx-js/mdx@3.0.0
- Node: v18.x

---
Repository: /testbed
