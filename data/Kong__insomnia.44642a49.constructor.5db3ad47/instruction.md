# Bug Report

### Describe the bug

I'm experiencing an issue with `QueryParam` construction where the key and value seem to be swapped when creating a QueryParam from a JSON string. When I pass a JSON string with `key` and `value` properties, the resulting QueryParam object has them reversed.

### Reproduction

```js
const jsonString = JSON.stringify({ key: 'myKey', value: 'myValue', type: 'text' });
const queryParam = new QueryParam(jsonString);

console.log(queryParam.key);   // Expected: 'myKey', Actual: 'myValue'
console.log(queryParam.value); // Expected: 'myValue', Actual: 'myKey'
```

The key and value are backwards - the key property contains the value and vice versa.

### Expected behavior

When creating a QueryParam from a JSON string, the `key` property should contain the key value and the `value` property should contain the value from the JSON. They shouldn't be swapped.

Also noticed that when passing an object directly (not a string), it seems to require a `type` property now even though it should be optional based on the type definition.

### System Info
- insomnia-sdk version: latest
- Node version: 18.x

---
Repository: /testbed
