# Bug Report

### Describe the bug

After a recent update, I'm getting duplicate requests created with extra metadata fields that I didn't specify. When I duplicate a request, the new request contains `duplicatedFrom` and `duplicatedAt` fields in the `metaData` object that I never asked for.

### Reproduction

```js
// Duplicate a request with custom metadata
const originalRequest = {
  _id: 'req_123',
  name: 'My Request',
  metaData: {
    customField: 'myValue'
  }
};

const duplicated = await duplicate(originalRequest, {
  name: 'Copy of My Request'
});

// The duplicated request now has unexpected fields:
// duplicated.metaData = {
//   customField: 'myValue',
//   duplicatedFrom: 'req_123',
//   duplicatedAt: 1234567890
// }
```

### Expected behavior

The duplicate function should only apply the patch I provide. If I don't specify metadata changes, it shouldn't add any extra fields automatically. The duplicated request should have the same metadata as the original unless I explicitly override it in the patch parameter.

### Additional context

This is affecting both regular requests, gRPC requests, and WebSocket requests. The metadata is being injected even when I pass an empty patch object or when I provide my own custom metadata that gets merged with these unwanted fields.

---
Repository: /testbed
