# Bug Report

### Describe the bug

I'm encountering an issue with the Headers class after a recent update. The code appears to be incomplete or corrupted - the `Header` class definition is missing most of its implementation. Methods like `constructor`, `create`, `parse`, `parseSingle`, `unparse`, and `unparseSingle` are no longer present in the class.

### Reproduction

When trying to use the Header class:

```js
import { Header } from 'insomnia-sdk';

// This should create a new header instance
const header = new Header({ key: 'Content-Type', value: 'application/json' });

// This should parse a header string
const parsed = Header.parseSingle('Content-Type: application/json');

// None of these work anymore
```

### Expected behavior

The `Header` class should have all its methods available:
- `constructor()` should accept HeaderDefinition or string
- `create()` should create new Header instances
- `parse()` should parse multiple headers from a string
- `parseSingle()` should parse a single header
- `unparse()` should convert headers back to string format
- `unparseSingle()` should convert a single header to string

Instead, the class definition seems to have been replaced with just a `normalizeHeaderKey()` function, and the class implementation is cut off mid-function (`unparseSingle` is incomplete).

### System Info
- Package: insomnia-sdk
- File: packages/insomnia-sdk/src/objects/headers.ts

This looks like the file might have been accidentally truncated or incorrectly edited during a refactor. The Header class is essentially unusable in its current state.

---
Repository: /testbed
