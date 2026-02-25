You are an edge computing engineer preparing for a secure deployment to a fleet of IoT devices. Your objective is to generate a new SSH keypair for device access, and set up a log to confirm the process for auditing.

Specifically, complete the following steps:

1. Generate a new SSH keypair using the ed25519 algorithm, with the comment "edge-iot-access" and no passphrase.
2. The private key file must be saved at <code>/home/user/.ssh/iot_edge_ssh</code>, and the public key must be saved at <code>/home/user/.ssh/iot_edge_ssh.pub</code>.
3. After successful key generation, create a log file named <code>/home/user/edge_ssh_keygen.log</code>. The log file must contain the following details, one per line, with each line prefixed as shown:
    <ul>
        <li><code>Key Type:</code> followed by the key type (should be "ed25519")</li>
        <li><code>Public Key Path:</code> followed by the absolute path of the public key file</li>
        <li><code>Private Key Path:</code> followed by the absolute path of the private key file</li>
        <li><code>Comment:</code> followed by the comment used during generation</li>
    </ul>
    Example log line: <code>Key Type: ed25519</code>
4. Ensure the private key file permissions are no more permissive than 600.
5. Ensure both key files and the log file are owned by <code>user</code> and located in their specified paths.

This log file will be used for automated verification of your setup, so ensure the format exactly matches the example for all entries.
