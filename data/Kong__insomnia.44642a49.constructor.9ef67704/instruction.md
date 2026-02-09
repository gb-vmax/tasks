# Bug Report

### Describe the bug

When creating a Certificate object without providing a name, the constructor throws an error instead of generating a default name. This makes it impossible to create certificates without explicitly specifying a name property.

### Reproduction

```js
const cert = new Certificate({
  matches: ['https://example.com'],
  key: { src: '/path/to/key.pem' },
  cert: { src: '/path/to/cert.pem' }
});
```

This throws an error because `name` is undefined, even though the certificate configuration is otherwise valid.

### Expected behavior

The Certificate constructor should automatically generate a default name when one is not provided, similar to how other SDK objects handle optional naming. For example, when matches are provided, it could use the first match pattern to generate a name like `cert_https___example_com`.

### Additional context

This seems to have broken after a recent update. Previously I could create certificates without specifying a name and it would work fine. Now I have to explicitly set a name for every certificate which is tedious when dealing with multiple certificates.

---
Repository: /testbed
