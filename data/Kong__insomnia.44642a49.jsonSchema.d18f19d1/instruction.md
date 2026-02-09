# Bug Report

### Describe the bug

The `jsonSchema` validation in the response object is not working correctly. When I try to validate a response against a JSON schema, the validation seems to be broken or not accepting the expected input format.

### Reproduction

```js
const response = // ... get response object

// This doesn't work as expected anymore
response.to.have.jsonSchema({
  type: 'object',
  properties: {
    name: { type: 'string' }
  }
});
```

I'm trying to validate my API response against a JSON schema but it's not behaving as it did before. The validation either fails incorrectly or doesn't provide proper error messages.

### Expected behavior

The `jsonSchema` assertion should accept a schema object and validate the response body against it. It should also provide clear error messages when validation fails so I can debug what's wrong with my response structure.

### Additional context

This appears to have started happening recently. I'm not sure if there was a change to how the schema validation is supposed to work, but my existing tests are now broken. Would appreciate any guidance on the correct way to use this feature.

---
Repository: /testbed
