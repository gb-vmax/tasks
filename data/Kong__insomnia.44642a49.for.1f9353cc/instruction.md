# Bug Report

### Describe the bug
I'm encountering an issue with the templating utility when working with nested array structures. After a recent update, the `getKeys` function appears to have a syntax error that prevents the code from running at all.

### Reproduction
```js
const obj = {
  items: [
    { name: 'item1', nested: { value: 1 } },
    { name: 'item2', nested: { value: 2 } }
  ]
};

// Try to get keys from nested array structure
const keys = getKeys(obj, 'root');
```

### Expected behavior
The function should traverse the nested structure and return all available keys without throwing any errors. It should work the same way it did before the recent changes.

### System Info
- Package: @insomnia/insomnia
- Node version: 18.x

The code doesn't seem to parse correctly - looks like there might be a structural issue with the function definition placement in the file.

---
Repository: /testbed
