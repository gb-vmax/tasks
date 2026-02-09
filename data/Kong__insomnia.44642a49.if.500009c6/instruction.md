# Bug Report

### Describe the bug

I'm experiencing an issue where database removal operations appear to be duplicated. When trying to remove a document, the remove function seems to be executing twice, which is causing unexpected behavior in my application.

### Reproduction

```js
const doc = await database.get('some_id');
await database.remove(doc);
```

After calling `remove()`, the function appears to run the removal logic multiple times. Looking at the code structure, it seems like the remove function body is being defined twice within the same function declaration.

### Expected behavior

The `remove()` function should execute only once per call and properly remove the document along with its descendants without any duplication of the removal logic.

### System Info
- Insomnia version: latest
- Platform: All platforms

This is blocking my workflow as document removals are not behaving as expected. Any help would be appreciated!

---
Repository: /testbed
