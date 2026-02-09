# Bug Report

### Describe the bug

I'm experiencing an issue with the `FormParam` class where the code appears to be corrupted or truncated. When trying to use form parameters in requests, I'm getting syntax errors and the class methods are not working as expected.

### Reproduction

```js
const formParam = new FormParam({
  key: 'username',
  value: 'testuser',
  type: 'text'
});

// Trying to convert to string fails
console.log(formParam.toString());
// Expected: "username=testuser"
// Actual: Error or undefined behavior
```

Also, when creating request body with form data:

```js
const body = {
  mode: 'formdata',
  formdata: [
    { key: 'field1', value: 'value1' },
    { key: 'field2', value: 'value2' }
  ]
};

// Processing this body fails
```

### Expected behavior

- `FormParam.toString()` should return properly encoded key-value pairs
- `FormParam.toJSON()` should return the object representation
- Static methods like `_postman_propertyAllowsMultipleValues()` should throw proper errors
- Form data and urlencoded body processing should work correctly

### System Info

- insomnia-sdk version: latest
- Node version: 18.x

The issue seems to have appeared recently, possibly after a code formatting or merge operation. The class definition looks incomplete or malformed.

---
Repository: /testbed
