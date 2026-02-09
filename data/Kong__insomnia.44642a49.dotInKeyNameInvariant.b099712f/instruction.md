# Bug Report

### Describe the bug

I'm getting an error when trying to import data that should be valid. The importer is throwing an error about invalid keys containing dots (`.`), but the keys in my data don't actually have any dots in them.

### Reproduction

```js
const validData = {
  name: 'My Request',
  url: 'https://example.com',
  method: 'GET'
}

// This throws an error even though there are no dots in any keys
dotInKeyNameInvariant(validData)
```

The error message says: `Detected invalid key "name", which contains '.'. Please update it in the original tool and re-import it.`

But clearly "name" doesn't contain a dot character.

### Expected behavior

The function should only throw an error when keys actually contain dots. Valid keys without dots should pass through without errors.

### Additional context

This is blocking me from importing any data at all since every object has at least some basic keys like "name", "url", etc. The validation seems to be inverted - it's rejecting valid keys instead of invalid ones.

---
Repository: /testbed
