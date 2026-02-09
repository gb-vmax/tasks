# Bug Report

### Describe the bug

The Headers class appears to be broken after a recent update. When trying to use any header-related functionality, I'm getting errors about missing methods and properties. It seems like the entire class implementation got corrupted or accidentally replaced with incomplete code.

### Reproduction

```js
const header = new Header({ key: 'Content-Type', value: 'application/json' });
console.log(header.key); // Error: Header is not a constructor or methods are missing

// Also fails when trying to parse headers
const parsed = Header.parse('Content-Type: application/json\nUser-Agent: MyApp/1.0');
// Error: Header.parse is not a function
```

### Expected behavior

The Header class should work as before:
- Creating new Header instances should work
- Parsing header strings should return proper key-value pairs
- Unparsing headers back to strings should work
- All static methods like `parse()`, `parseSingle()`, `unparse()`, etc. should be available

### System Info

- insomnia-sdk version: latest
- The issue started appearing suddenly, possibly after a bad commit or incomplete file save

It looks like the class definition might have been accidentally truncated or overwritten. The file seems to cut off mid-implementation with an incomplete `normalizeHeaderKey` method that doesn't even have a closing brace.

---
Repository: /testbed
