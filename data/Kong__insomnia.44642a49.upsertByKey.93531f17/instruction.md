# Bug Report

### Describe the bug

After a recent update, plugin data values are being stored in a different format than before. When I try to retrieve plugin data using `getByKey()`, I'm getting back a JSON string with a structured object containing `current` and `history` fields instead of the raw value I stored.

### Reproduction

```js
// Store a simple string value
await upsertByKey('my-plugin', 'api-key', 'secret123');

// Try to retrieve it
const doc = await getByKey('my-plugin', 'api-key');
console.log(doc.value);

// Expected: 'secret123'
// Actual: '{"current":"secret123","history":[]}'
```

This is breaking my plugin because I'm expecting the raw value, not a JSON-encoded object. I have to now parse the value every time I retrieve it, which wasn't necessary before.

### Expected behavior

The value should be stored and retrieved as-is, without any additional wrapping or structure. If I store `'secret123'`, I should get back `'secret123'`, not a JSON object.

### Additional context

This seems to have started happening recently. My plugin worked fine before and I didn't change any code on my end. Not sure if this is intentional or a regression, but it's definitely breaking backward compatibility with existing plugin data.

---
Repository: /testbed
