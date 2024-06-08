import socket
import re

def solve_math_problem(problem):
    # Use regular expressions to find numbers and the operator, including integer division //
    match = re.match(r"(\d+)\s*([+\-*/]|//)\s*(\d+)", problem)
    if not match:
        raise ValueError("Could not parse problem: " + problem)
    
    num1 = int(match.group(1))
    operator = match.group(2)
    num2 = int(match.group(3))
    
    if operator == '+':
        return num1 + num2
    elif operator == '-':
        return num1 - num2
    elif operator == '*':
        return num1 * num2
    elif operator == '/':
        return num1 / num2
    elif operator == '//':
        return num1 // num2
    else:
        raise ValueError("Unknown operator: " + operator)

def main():
    host = "0.cloud.chals.io"
    port = 15072

    # Create a socket and connect to the server
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((host, port))

    # Receive and solve math problems
    while True:
        # Receive data from the server
        data = s.recv(1024).decode('utf-8')
        if not data:
            break
        
        print("Received:", data)
        
        # Find the math problem in the received data
        problem = re.findall(r"\d+\s*(?:[+\-*/]|//)\s*\d+", data)
        if problem:
            answer = solve_math_problem(problem[0])
            print("Answer:", answer)
            
            # Send the answer back to the server
            s.sendall((str(answer) + "\n").encode('utf-8'))
    
    # Close the connection
    s.close()

if __name__ == "__main__":
    main()
