# Shell Injection Simulation

## Overview
This repository contains a simple Python script that demonstrates the concept of **Shell Injection**. It is designed for educational purposes only and aims to help users understand the potential risks associated with improper handling of user inputs in software applications.

Please note that this script should only be used in a safe, controlled environment. The code is intended to raise awareness about **security vulnerabilities** and how these issues can be mitigated. It is not meant to be used for malicious purposes.

## Purpose
Shell injection is a critical security vulnerability that occurs when an attacker is able to execute arbitrary shell commands on a server through an application that improperly handles user input. This simulation shows how a vulnerable function can be exploited and how proper sanitization can prevent such attacks.

### Key Features:
- **Vulnerable function**: Demonstrates how a simple function can be exploited using unsanitized user input.
- **Secure function**: Shows how input validation and sanitization can protect against such attacks using best practices.
- **Simulated attack**: Provides an example of a shell injection attempt and how it can be blocked.

## How to Use
1. Clone the repository to your local machine:
   ```
   git clone https://github.com/farrosfr/shell-injection-simulation.git
   ```

2. Navigate to the project directory:
   ```
   cd shell-injection-simulation
   ```

3. Run the script:
   ```
   python3 shell_injection_simulation.py
   ```

## Educational Purpose
This repository is a **humble contribution** to the cybersecurity community, intended to provide insights into one of the most common vulnerabilities in modern applications. We strongly encourage you to use this knowledge for good: to enhance the security of your own applications and to foster a safer online environment for everyone.

### A Word of Caution:
While this repository demonstrates a powerful concept, we kindly request that you **do not use this knowledge to engage in any unethical or illegal activities**. The code is provided with the sole purpose of education, and any use beyond that is at your own responsibility.

## Contributing
If you have suggestions for improving the code or wish to contribute, feel free to open an issue or submit a pull request. All contributions are appreciated.

## License
This project is licensed under the [MIT License](LICENSE).

## Disclaimer
The author is **not responsible** for any misuse of this code. This script is intended to demonstrate potential vulnerabilities, and it is the user's responsibility to ensure it is used ethically and legally.
