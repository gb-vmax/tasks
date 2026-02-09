# Bug Report

### Describe the bug

When using `expect(response).to.have.jsonSchema()` in test assertions, the schema validation is not working as expected. It appears that the validation is always passing even when the response body doesn't match the provided JSON schema.

### Reproduction

```js
const response = {
  body: JSON.stringify({
    name: 'John',
    age: 'invalid' // should be a number
  })
}

const schema = {
  type: 'object',
  properties: {
    name: { type: 'string' },
    age: { type: 'number' }
  },
  required: ['name', 'age']
}

// This should fail but passes
expect(response).to.have.jsonSchema(schema)
```

### Expected behavior

The assertion should fail when the response body doesn't conform to the JSON schema. In the example above, the `age` property is a string but the schema expects a number, so the validation should fail.

### System Info
- insomnia-sdk version: latest
- The issue seems to affect the response object's `to.have.jsonSchema()` method

---
Repository: /testbed
