# Network-Port-Scanner
Python script that scans for open ports on a given IP address or hostname.

---

### **3. Simulate Open Ports for Testing (Optional)**
If you want to generate output with open ports:
1. **Run a Service Locally**:
   - Start a service like a web server to open specific ports:
     ```bash
     python3 -m http.server 8080
     ```
     This command starts a local web server on port `8080`.

2. **Re-run the Script**:
   - Scan for the range including `8080` (e.g., 8000-8100).
   - Example output:
     ```plaintext
     Scanning ports on 127.0.0.1 from 8000 to 8100...

     Open ports on 127.0.0.1:
     Port 8080 is open
     ```

3. **Save and Use This Output**:
   - Include this modified result as an example in your README.

---

### **4. Add Both Outputs to README**
If you want to demonstrate the script’s flexibility, show both:
1. **No Open Ports Found**:
   ```plaintext
   Scanning ports on 127.0.0.1 from 3 to 1022...

   No open ports found on 127.0.0.1 in the range 3-1022.
