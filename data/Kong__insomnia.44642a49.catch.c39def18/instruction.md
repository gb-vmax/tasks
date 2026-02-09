# Bug Report

### Describe the bug

After a recent update, I'm experiencing issues with gRPC error handling in the main process. When errors occur during gRPC calls, the renderer process doesn't receive the error event properly, causing the UI to hang indefinitely waiting for a response.

### Reproduction

```js
// In renderer process
ipcRenderer.send('grpc.sendMessage', requestId, messageData);

ipcRenderer.once('grpc.error', (event, id, error) => {
  console.log('Error received:', error);
  // This callback is never triggered
});
```

When a gRPC error occurs (like connection failures or invalid requests), the error handler doesn't seem to be sending the error back to the renderer process correctly. The application just hangs without any feedback.

### Expected behavior

When a gRPC operation fails, the renderer process should receive a `grpc.error` event with the error details so the UI can display appropriate error messages or retry logic.

### Additional context

This seems to have started happening after some recent changes to the IPC error handling. The issue is particularly noticeable when:
- Network connectivity is lost
- The gRPC server is unavailable
- Invalid message formats are sent

The UI just shows a loading state indefinitely instead of showing an error message.

---
Repository: /testbed
