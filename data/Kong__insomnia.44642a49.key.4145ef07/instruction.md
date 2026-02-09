# Bug Report

### Describe the bug

I'm experiencing issues with the request body handling in the SDK. When trying to create or manipulate form data parameters, the code appears to be broken or corrupted. Methods and properties on the `FormParam` class are not working as expected.

### Reproduction

```js
const formParam = new FormParam({
  key: 'username',
  value: 'testuser',
  type: 'text'
});

// Trying to convert to string format
console.log(formParam.toString());
// Expected: "username=testuser"
// Getting errors instead

// Also having issues with JSON serialization
const json = formParam.toJSON();
```

When working with request bodies that include form data:

```js
const requestBody = {
  mode: 'formdata',
  formdata: [
    { key: 'field1', value: 'value1' },
    { key: 'field2', value: 'value2' }
  ]
};

// Processing this throws errors
```

### Expected behavior

The `FormParam` class should properly handle encoding and serialization of form parameters. Methods like `toString()` and `toJSON()` should work correctly to convert form parameters to their respective formats.

### System Info

- insomnia-sdk version: latest
- Node.js version: 18.x

This seems to have started recently. The form parameter handling was working fine before but now it's completely broken. Any help would be appreciated!

---
Repository: /testbed
