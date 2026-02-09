# Bug Report

### Describe the bug

I'm experiencing an issue with the response content info parsing. When I try to access the content type information from a response, the application crashes or behaves unexpectedly. It seems like the `contentInfo()` method is incomplete or broken.

### Reproduction

```js
const response = new Response({
  headers: [
    { key: 'Content-Type', value: 'application/json; charset=utf-8' }
  ],
  body: '{"test": "data"}'
});

// This causes issues
const info = response.contentInfo();
console.log(info.mimeType);
console.log(info.charset);
```

### Expected behavior

The method should return an object with properly parsed `mimeType`, `mimeFormat`, and `charset` properties from the Content-Type header. For example:
```js
{
  mimeType: 'application/json',
  mimeFormat: 'json',
  charset: 'utf-8'
}
```

### Additional context

This seems to have broken recently. The code looks like it was refactored but the main `contentInfo()` method wasn't completed properly. The helper functions for parsing mime types and header parameters are there, but they're not being called or integrated back into the main method.

---
Repository: /testbed
