# Bug Report

### Describe the bug

I'm experiencing an issue with the request body handling in the SDK. When trying to work with form data or URL-encoded parameters, the code appears to be corrupted or improperly formatted. Methods and properties seem to be missing or have invalid syntax.

### Reproduction

```js
const formParam = new FormParam({
  key: 'username',
  value: 'testuser',
  type: 'text'
});

// Trying to use the FormParam methods
formParam.toString(); // Expected to work but fails
formParam.toJSON();   // Expected to work but fails
```

When attempting to create request bodies with form data:

```js
const requestBody = {
  mode: 'formdata',
  formdata: [
    { key: 'field1', value: 'value1' }
  ]
};

// Processing this throws errors about invalid syntax
```

### Expected behavior

- `FormParam` class methods like `toString()`, `toJSON()`, and `valueOf()` should work correctly
- Static methods should be properly defined
- Request body options with formdata and urlencoded should be processed without syntax errors

### System Info
- Package: insomnia-sdk
- Node version: 18.x

The code seems to have formatting issues that prevent normal operation. This is blocking my ability to work with form-based request bodies.

---
Repository: /testbed
