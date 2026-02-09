# Bug Report

### Describe the bug

The `json()` method on the Response object is not working correctly when trying to extract nested properties from the JSON response. When I pass a string path to access nested data, the method throws an error instead of returning the value.

### Reproduction

```js
const response = {
  body: JSON.stringify({
    user: {
      profile: {
        name: 'John Doe',
        email: 'john@example.com'
      }
    }
  }),
  headers: [
    { key: 'Content-Type', value: 'application/json' }
  ]
};

// This throws an error
const name = response.json('user.profile.name');
// Expected: 'John Doe'
```

Also having issues with array access:

```js
const response = {
  body: JSON.stringify({
    items: [
      { id: 1, name: 'Item 1' },
      { id: 2, name: 'Item 2' }
    ]
  })
};

// This also throws an error
const firstItem = response.json('items[0].name');
// Expected: 'Item 1'
```

### Expected behavior

The `json()` method should support path-based extraction when a string is passed as the first argument. It should be able to traverse nested objects and arrays using dot notation and bracket notation.

### Additional context

This seems related to how the reviver parameter is being handled. Previously, I could just call `json()` without arguments and it would parse the entire response, but now when trying to use path-based extraction the behavior is broken.

---
Repository: /testbed
