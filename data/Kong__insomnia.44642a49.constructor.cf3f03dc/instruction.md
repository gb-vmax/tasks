# Bug Report

### Describe the bug

I'm having trouble creating `QueryParam` objects when the `type` field is optional. When I try to instantiate a `QueryParam` with just `key` and `value` (without `type`), it throws an error saying "unknown options for new QueryParam", even though `type` is supposed to be optional according to the type definition.

### Reproduction

```js
// This should work since type is optional, but throws an error
const param = new QueryParam({
  key: 'search',
  value: 'test'
});
// Error: unknown options for new QueryParam

// This works fine
const paramWithType = new QueryParam({
  key: 'search',
  value: 'test',
  type: 'text'
});
```

### Expected behavior

The `QueryParam` constructor should accept objects with just `key` and `value` properties, since `type` is marked as optional in the type definition. It shouldn't require the `type` field to be present in the options object.

### Additional context

This is blocking me from creating query parameters dynamically where the type isn't always known or needed. The type signature says `type?: string` so it should be optional, but the constructor validation seems to require it.

---
Repository: /testbed
