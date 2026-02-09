# Bug Report

### Describe the bug

The `trackSegmentEvent` function in the test setup is modifying the properties object that gets passed to it. When I pass an object with string properties to track an event, the original object's string values are being mutated (trimmed and lowercased) instead of working with a copy.

### Reproduction

```js
const eventProperties = {
  userId: 'USER123',
  action: '  Click Button  '
};

await global.main.trackSegmentEvent('test_event', eventProperties);

// Original object is mutated!
console.log(eventProperties.userId); // Expected: 'USER123', Got: 'user123'
console.log(eventProperties.action); // Expected: '  Click Button  ', Got: 'click button'
```

### Expected behavior

The function should not modify the original properties object that's passed in. If normalization is needed, it should work on a copy of the object to avoid side effects.

### System Info
- Insomnia version: latest
- Node version: 18.x

---
Repository: /testbed
