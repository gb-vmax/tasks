# Bug Report

### Describe the bug

I'm experiencing an issue with URL serialization when using the `toString()` method on `Url` objects. The generated URL string appears to be malformed in certain cases.

### Reproduction

```js
const url = new Url({
  protocol: 'https:',
  host: 'example.com',
  auth: {
    username: 'user',
    password: 'pass'
  }
});

console.log(url.toString());
// Expected: https://user:pass@example.com
// Actual: https://https://user:passexample.com
```

When converting a URL object to a string, the output seems incorrect. The protocol appears to be duplicated and the authentication separator (`@`) is missing, causing the username/password to concatenate directly with the host.

### Expected behavior

The `toString()` method should generate a properly formatted URL string with:
- Correct protocol formatting (no duplication)
- Proper auth string with `@` separator between credentials and host
- All URL components in the right order

### System Info
- Package: insomnia-sdk
- Version: latest

---
Repository: /testbed
