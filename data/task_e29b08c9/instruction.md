You are acting as a Kubernetes operator managing application manifests. In the directory <code>/home/user/k8s-manifests/</code>, there is a file named <code>deployments.csv</code>. Each line in <code>deployments.csv</code> describes a deployment in the following comma-separated format (with headers):

<pre>
name,namespace,image,replicas
frontend,default,nginx:1.20,3
backend,prod,backend-app:2.1,2
analytics,default,my-analytics:0.4,1
</pre>

Your task consists of the following steps:

1. Read <code>/home/user/k8s-manifests/deployments.csv</code> and convert its contents to a JSON array of objects with keys: <code>name</code>, <code>namespace</code>, <code>image</code>, and <code>replicas</code>. All values should be treated as strings (even numbers).
2. Save the resulting JSON array to <code>/home/user/k8s-manifests/deployments.json</code>. The format must be strict JSON without trailing commas or comments. All keys must be present for each object; preserve the header order: <code>name</code>, <code>namespace</code>, <code>image</code>, <code>replicas</code>.
3. Then, as a Kubernetes operator, you discover a change request: The <code>backend</code> deployment in the <code>prod</code> namespace should have its <code>replicas</code> set to <code>5</code>.
4. Modify <code>/home/user/k8s-manifests/deployments.json</code> accordingly, updating only the relevant deployment.
5. Output a log file at <code>/home/user/k8s-manifests/update.log</code>, with exactly one line, recording the operation in plain text:

<pre>
Updated backend in prod: replicas set to 5
</pre>

The automated test will verify:
<ul>
<li>The precise structure and contents of <code>/home/user/k8s-manifests/deployments.json</code>, including string types and order.</li>
<li>That only the <code>backend</code> deployment in <code>prod</code> has changed its <code>replicas</code> to <code>"5"</code>, nothing else changes.</li>
<li>The content and presence of <code>/home/user/k8s-manifests/update.log</code> as specified.</li>
</ul>
