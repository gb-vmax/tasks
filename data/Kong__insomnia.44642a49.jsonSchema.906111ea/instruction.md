# Bug Report

### Describe the bug

When using `pm.expect(response).to.not.have.jsonSchema()` in test scripts, the assertion behaves incorrectly. Instead of checking that the response does NOT match the schema, it appears to be checking that it DOES match the schema (inverted logic).

### Reproduction

```js
// Define a JSON schema
const schema = {
  type: 'object',
  properties: {
    name: { type: 'string' }
  }
};

// Response body that matches the schema
const response = {
  body: JSON.stringify({ name: 'John' })
};

// This should pass (response matches schema, so NOT matching should fail)
// But it fails when it shouldn't
pm.expect(response).to.not.have.jsonSchema(schema);
```

### Expected behavior

The `.not.have.jsonSchema()` assertion should verify that the response does NOT conform to the provided schema. If the response matches the schema, the assertion should fail. If the response doesn't match, it should pass.

Currently it seems like the logic is reversed - it's doing the opposite of what `.not` should do.

### System Info
- Insomnia SDK version: latest
- Using pre-request/test scripts

---
Repository: /testbed
