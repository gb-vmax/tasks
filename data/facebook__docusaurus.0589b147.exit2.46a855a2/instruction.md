# Bug Report

### Describe the bug
When parsing markdown with the remark tokenizer, exit events are being pushed with the wrong event type. Instead of using the literal string `"exit"`, the tokenizer is now using the `type` parameter value, which causes event listeners and handlers expecting `"exit"` events to not trigger properly.

### Reproduction
```js
const parser = createTokenizer(/* ... */);

// Set up an event listener for exit events
parser.on('exit', (token) => {
  console.log('Token exited:', token);
});

// Parse some markdown
parser.parse('# Hello World');

// Expected: Event listener should be called with "exit" events
// Actual: Event listener is never called because events are pushed with token type instead of "exit"
```

### Expected behavior
The tokenizer should push events with the event type `"exit"` so that event handlers can properly listen for and respond to token exit events. The token's type information should be available through the token object itself, not as the event name.

### System Info
- remark version: 15.0.1
- Node version: Latest

This appears to be a regression - the exit events were working correctly before but now seem to be using the wrong value when pushing to the events array.

---
Repository: /testbed
