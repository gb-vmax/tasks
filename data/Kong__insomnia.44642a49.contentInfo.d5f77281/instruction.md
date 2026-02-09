# Bug Report

### Describe the bug

I'm experiencing an issue with response content type parsing in the SDK. When working with responses that have `Content-Type` headers, the `contentInfo()` method appears to be broken or incomplete. The method seems to have been refactored but the implementation is cut off or missing critical parts.

### Reproduction

```js
const response = new Response({
  headers: [
    { key: 'Content-Type', value: 'application/json; charset=utf-8' }
  ],
  body: '{"test": "data"}'
});

// This fails or returns incomplete info
const info = response.contentInfo();
console.log(info);
```

### Expected behavior

The `contentInfo()` method should return a complete `ResponseContentInfo` object with:
- `mimeType` properly extracted from Content-Type header
- `mimeFormat` derived from the mime type
- `charset` extracted from Content-Type directives
- File information from Content-Disposition header if present

Instead, it seems like the method implementation is incomplete or the refactoring broke existing functionality.

### System Info
- Package: insomnia-sdk
- Affected file: `packages/insomnia-sdk/src/objects/response.ts`

This is blocking my ability to properly parse response metadata. Any help would be appreciated!

---
Repository: /testbed
