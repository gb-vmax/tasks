# Bug Report

### Describe the bug

I'm experiencing an issue with authentication parameter extraction where the wrong values are being returned. It seems like the logic for finding authentication keys is not working correctly - it's returning values even when the key doesn't match.

### Reproduction

```js
const auth = {
  oauth2: [
    { key: 'accessToken', value: 'token123' },
    { key: 'clientId', value: 'client456' }
  ]
};

// When trying to get 'clientId', it returns the first value instead
// Expected: 'client456'
// Actual: 'token123' (wrong value!)
```

The function returns the first value it encounters regardless of whether the key actually matches what we're looking for.

### Expected behavior

The authentication helper should only return a value when the key exactly matches the target key. Right now it seems to be ignoring the key comparison and just returning any string value it finds.

### Additional context

This is causing authentication to fail because tokens and client IDs are getting mixed up. The function should check BOTH that the value is a string AND that the key matches before returning.

---
Repository: /testbed
