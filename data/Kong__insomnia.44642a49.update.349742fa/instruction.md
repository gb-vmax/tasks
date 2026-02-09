# Bug Report

### Describe the bug
The `update()` function for API specs is not working correctly. When trying to update an API spec with new data, the changes aren't being applied properly. It seems like the parameters might be getting passed in the wrong order to the underlying database update function.

### Reproduction
```js
const apiSpec = {
  _id: 'spec_123',
  name: 'My API',
  contents: '...'
}

// Try to update the name
update(apiSpec, { name: 'Updated API' })

// The name doesn't actually get updated
```

### Expected behavior
The API spec should be updated with the new values from the patch object. The `name` field should change to 'Updated API' in the example above.

### Additional context
This affects any code that tries to update API spec properties. The update appears to silently fail or behave unexpectedly.

---
Repository: /testbed
