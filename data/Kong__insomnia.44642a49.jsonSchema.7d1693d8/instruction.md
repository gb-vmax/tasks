# Bug Report

### Describe the bug

I'm experiencing an issue with the `response.to.have.jsonSchema()` assertion method. When the response body doesn't match the expected JSON schema, the error message is not very helpful - it just says the schema doesn't match without providing details about what specifically failed validation.

### Reproduction

```js
const schema = {
  type: 'object',
  properties: {
    name: { type: 'string' },
    age: { type: 'number' }
  },
  required: ['name', 'age']
};

// Response body is missing required field
const response = {
  body: JSON.stringify({ name: 'John' })
};

// This fails but the error message doesn't tell me what's wrong
pm.expect(response).to.have.jsonSchema(schema);
```

### Expected behavior

The error message should include specific validation errors, like:
- Which paths in the JSON failed validation
- What was expected vs what was received
- Details about missing required properties, type mismatches, etc.

This would make debugging schema validation failures much easier instead of having to guess what went wrong.

### System Info
- insomnia-sdk version: latest
- Node version: 18.x

---
Repository: /testbed
