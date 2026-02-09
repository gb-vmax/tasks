# Bug Report

### Describe the bug

When creating form data with duplicate keys or keys that have leading/trailing whitespace, the request body is not being processed correctly. The form parameters seem to be getting mangled or lost entirely.

### Reproduction

```js
const request = new Request({
  body: {
    mode: 'formdata',
    formdata: [
      { key: 'username', value: 'john' },
      { key: 'username', value: 'jane' },  // duplicate key
      { key: '  email  ', value: 'test@example.com' },  // whitespace in key
      { key: '', value: 'ignored' },  // empty key
    ]
  }
});

// The form data is not being handled as expected
console.log(request.body.formdata);
```

### Expected behavior

- Duplicate keys should be handled consistently (either kept or deduplicated in a predictable way)
- Keys with whitespace should be preserved or trimmed consistently
- Empty keys should be handled gracefully

Currently it seems like the form parameters are being processed in an unexpected way after a recent update. The behavior changed and now my scripts that were working before are breaking.

### System Info
- insomnia-sdk version: latest
- Node version: 18.x

---
Repository: /testbed
