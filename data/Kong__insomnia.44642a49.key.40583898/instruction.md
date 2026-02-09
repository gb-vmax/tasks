# Bug Report

### Describe the bug

I'm encountering a syntax error when trying to use the request object in my pre-request scripts. The code seems to be corrupted or malformed, causing the entire SDK to fail.

### Reproduction

```js
const formParam = new FormParam({
  key: 'username',
  value: 'test_user',
  type: 'text'
});

// Trying to convert to JSON fails
console.log(formParam.toJSON());
```

When I try to run this, I get syntax errors and the request body handling doesn't work at all. It looks like there might be an issue with the FormParam class implementation.

### Expected behavior

The FormParam object should be created successfully and methods like `toJSON()` and `toString()` should work without syntax errors. The request body should be properly formatted when using form data or URL-encoded content.

### Additional context

This seems to have started happening recently. Previously, form parameters were working fine in my scripts. Now even basic operations with request bodies are failing.

---
Repository: /testbed
