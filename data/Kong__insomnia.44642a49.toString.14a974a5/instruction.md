# Bug Report

### Describe the bug

The `toString()` method on the `Url` class is broken after a recent update. When calling `toString()` on a URL object, it returns an incomplete URL string that's cut off partway through.

### Reproduction

```js
const url = new Url({
  protocol: 'https',
  host: 'api.example.com',
  port: '443',
  path: '/v1/users',
  query: [
    { key: 'name', value: 'john doe' },
    { key: 'age', value: '25' }
  ],
  hash: 'section1'
});

const urlString = url.toString();
console.log(urlString);
// Expected: "https://api.example.com:443/v1/users?name=john+doe&age=25#section1"
// Actual: Returns incomplete string or throws error
```

Also happens when using the `forceProtocol` parameter:

```js
const urlString = url.toString(true);
// Same issue - incomplete output
```

### Expected behavior

The `toString()` method should return a complete, properly formatted URL string with all components (protocol, host, port, path, query parameters, and hash) included.

### Additional context

This seems to have started happening in the latest version. The URL object itself appears to store all the data correctly, but `toString()` fails to generate the complete string representation.

---
Repository: /testbed
