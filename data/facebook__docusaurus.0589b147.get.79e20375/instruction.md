# Bug Report

### Describe the bug

I'm encountering an issue with object property copying where nested property access returns `undefined` instead of the expected values. When copying properties from one object to another, the getter functions seem to be accessing the wrong property path.

### Reproduction

```js
const source = {
  name: 'test',
  value: 42,
  nested: { data: 'hello' }
}

const target = {}
// Copy properties using the utility function
copyProperties(target, source)

console.log(target.name) // Expected: 'test', Actual: undefined
console.log(target.value) // Expected: 42, Actual: undefined
```

### Expected behavior

When properties are copied from a source object to a target object, accessing properties on the target should return the same values as the source object. The getter should retrieve `source[key]` not `source[source[key]]`.

### System Info
- Node version: 18.x
- Affected module: remark-gfm vendor bundle

---
Repository: /testbed
