# Bug Report

### Describe the bug

When using `expect(response).to.have.jsonSchema()` in test scripts, the assertion is not working as expected. It seems like the schema validation is behaving incorrectly - either always passing when it should fail, or always failing when it should pass.

### Reproduction

```js
const schema = {
  type: 'object',
  properties: {
    id: { type: 'number' },
    name: { type: 'string' }
  },
  required: ['id', 'name']
}

// This should validate correctly but doesn't
pm.test('Response matches schema', function() {
  pm.expect(pm.response).to.have.jsonSchema(schema)
})
```

### Expected behavior

The `jsonSchema` assertion should properly validate the response body against the provided JSON schema. Valid responses should pass the test, and invalid responses should fail the test.

### Additional context

This appears to have started happening recently. Other assertions like `have.body()` and `have.jsonBody()` work fine, it's only the schema validation that's acting weird.

---
Repository: /testbed
