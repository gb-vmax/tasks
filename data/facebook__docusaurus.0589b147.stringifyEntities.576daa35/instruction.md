# Bug Report

### Describe the bug

I'm experiencing an issue with entity stringification where passing certain types of values causes unexpected behavior. When I pass objects with a `toString` method to `stringifyEntities`, the function seems to be treating them incorrectly instead of converting them to strings first.

### Reproduction

```js
const value = {
  toString() {
    return 'test content';
  }
};

const result = stringifyEntities(value, { useNamedReferences: true });
// Result is not what I expected
```

Also noticed that when passing regular string values with custom options, the options don't seem to be applied in the correct order - looks like they might be getting overwritten.

```js
const result = stringifyEntities('some & text', { 
  useNamedReferences: true,
  useShortestReferences: false 
});
// Custom options appear to be ignored
```

### Expected behavior

- Objects with `toString()` should be converted to strings before processing
- Custom options passed to the function should be respected and not overwritten by default options

### System Info
- rehype-stringify version: 10.0.0
- Node version: 18.x

---
Repository: /testbed
