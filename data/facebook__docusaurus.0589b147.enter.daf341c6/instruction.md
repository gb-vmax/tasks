# Bug Report

### Describe the bug

I'm experiencing an issue with token events in the remark parser where modifications to tokens after they've been entered are affecting the event history. It seems like the token object in the events array is being mutated when properties are added or modified on the token later in the parsing process.

### Reproduction

```js
// When parsing markdown, tokens are created and entered
const tokenizer = createTokenizer(parser, initialize, from);

// Token is entered into the event stream
const token = enter('someType', {});

// Later modifications to the token affect the event history
token.someProperty = 'value';

// The event that was pushed earlier now also contains 'someProperty'
// even though it shouldn't have had that property at the time of entry
```

### Expected behavior

The token state in the events array should reflect the token's state at the time it was entered, not be affected by subsequent modifications. Each event should capture a snapshot of the token at that specific moment.

### System Info
- remark version: 15.0.1
- Node version: Latest

This is causing issues when trying to analyze the parsing timeline, as the historical events don't accurately represent the state of tokens at different points in the parsing process.

---
Repository: /testbed
