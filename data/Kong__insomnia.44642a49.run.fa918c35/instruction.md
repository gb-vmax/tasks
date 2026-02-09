# Bug Report

### Describe the bug

The hash template tag is not working correctly after a recent update. When I try to use it for basic hashing operations, I'm getting syntax errors. It seems like the function structure was broken during some refactoring.

### Reproduction

```js
// Try to use the hash template tag
{% hash 'sha256', 'hex', 'test data' %}
```

This results in an error because the function definition appears to be malformed.

### Expected behavior

The hash template tag should work as before, allowing users to hash strings with different algorithms and encodings. The basic usage should be:
- Algorithm: sha256, md5, sha1, etc.
- Encoding: hex, latin1, base64
- Value: the string to hash

### Additional context

Looking at the code, it seems like there's a function definition (`parseInputEncoding`) that's placed outside of where it should be, and the indentation/structure of the `run` function looks incorrect. The `run` function should be properly nested within the template tag definition.

This is blocking our ability to use hash functionality in request templates.

---
Repository: /testbed
