# Bug Report

### Describe the bug
When creating plugin data using the `create()` function, the `type` field is not being set correctly on the created document. This causes the plugin data to be created without the proper type identifier, which breaks plugin data storage and retrieval.

### Reproduction
```js
import * as models from './plugin-data';

// Create plugin data
const pluginData = await models.create({
  key: 'my-plugin',
  value: { some: 'data' }
});

// The type field is missing or incorrect
console.log(pluginData.type); // undefined or wrong value
```

### Expected behavior
The created plugin data document should have the correct `type` field set automatically, allowing it to be properly identified and queried in the database.

### Additional context
This appears to be affecting plugin functionality where plugin-specific data needs to be stored and retrieved. The type field is essential for database queries to filter and find the correct documents.

---
Repository: /testbed
