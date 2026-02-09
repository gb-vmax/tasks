# Bug Report

### Describe the bug

I'm having an issue with `Header.parse()` where it's not parsing header strings correctly. When I pass a multi-line header string, the method returns an empty array instead of the parsed headers.

### Reproduction

```js
const headerString = `Content-Type: application/json
Authorization: Bearer token123
X-Custom-Header: value`;

const parsed = Header.parse(headerString);
console.log(parsed);
// Expected: [{ key: 'Content-Type', value: 'application/json' }, ...]
// Actual: []
```

Even with a single header line, it returns an empty array:

```js
const singleHeader = 'Content-Type: application/json';
const result = Header.parse(singleHeader);
console.log(result); // []
```

### Expected behavior

The `Header.parse()` method should return an array of parsed header objects with `key` and `value` properties for each valid header line in the input string. Empty lines should be filtered out, but valid header lines should be parsed and included in the result.

### System Info
- insomnia-sdk version: latest
- Node version: 18.x

---
Repository: /testbed
