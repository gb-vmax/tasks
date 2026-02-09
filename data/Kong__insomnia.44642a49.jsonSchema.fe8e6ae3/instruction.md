# Bug Report

### Describe the bug

After a recent update, I'm experiencing an issue with JSON schema validation in the response assertions. The `to.have.jsonSchema()` method appears to be broken - the validation logic seems corrupted or incomplete.

### Reproduction

```js
const response = {
  body: JSON.stringify({ name: 'John', age: 30 })
};

const schema = {
  type: 'object',
  properties: {
    name: { type: 'string' },
    age: { type: 'number' }
  }
};

// This assertion fails or behaves unexpectedly
pm.expect(response).to.have.jsonSchema(schema);
```

### Expected behavior

The JSON schema validation should work correctly and validate the response body against the provided schema. Valid JSON should pass validation and invalid JSON should fail with proper error messages.

### Additional context

This seems to have started happening recently. The code structure looks malformed - there are some helper functions defined in the middle of the object definition which doesn't make sense. Not sure if this was a merge conflict or accidental edit, but the `jsonSchema` assertion is definitely not working as expected.

---
Repository: /testbed
