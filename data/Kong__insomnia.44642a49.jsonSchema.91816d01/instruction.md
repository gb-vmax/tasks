# Bug Report

### Describe the bug

I'm experiencing an issue with the `to.have.jsonSchema` assertion in the response object. When using this method to validate JSON responses against a schema, it's not working as expected. The assertion seems to be wrapping the schema in an unexpected way or changing its validation behavior.

### Reproduction

```js
const response = // ... some API response

// This doesn't validate correctly anymore
pm.expect(response).to.have.jsonSchema({
  type: 'object',
  properties: {
    id: { type: 'number' },
    name: { type: 'string' }
  }
})
```

The schema validation appears to fail or behave differently than it did before. I'm passing a standard JSON schema object but it's not being processed correctly.

### Expected behavior

The `to.have.jsonSchema` method should accept a JSON schema object directly and validate the response body against it, similar to how other assertion methods work (like `to.have.body` or `to.have.jsonBody`).

### System Info
- insomnia-sdk version: latest
- The issue appeared recently, possibly after an update

---
Repository: /testbed
