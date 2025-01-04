import socket

def scan_ports(target, start_port, end_port):
    print(f"Scanning ports on {target} from {start_port} to {end_port}...\n")
    open_ports = []

    for port in range(start_port, end_port + 1):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.settimeout(0.5)  # Timeout for each connection attempt
            result = s.connect_ex((target, port))  # Attempt to connect
            if result == 0:
                open_ports.append(port)

    return open_ports


if __name__ == "__main__":
    target = input("Enter the target IP address or hostname: ")
    start_port = int(input("Enter the start port (e.g., 1): "))
    end_port = int(input("Enter the end port (e.g., 1024): "))

    try:
        open_ports = scan_ports(target, start_port, end_port)
        if open_ports:
            print(f"\nOpen ports on {target}:")
            for port in open_ports:
                print(f"Port {port} is open")
        else:
            print(f"\nNo open ports found on {target} in the range {start_port}-{end_port}.")
    except socket.gaierror:
        print("Invalid hostname or IP address.")
    except ValueError:
        print("Invalid port range. Please enter valid numbers.")
