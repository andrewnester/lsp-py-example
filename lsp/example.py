import json
from connect import Connection

connection = Connection()

def lsp_request(msg):
    connection.send(msg)
    response = connection.receive()
    print(json.dumps(response, indent=4, sort_keys=True))

def main():
    connection.connect("127.0.0.1", 9090)
    
    # Initialize LSP server
    lsp_request({
        "method": "initialize",
        "params": {
            "rootUri": "file:///home/ec2-user/environment/example"
        },
        "jsonrpc": "2.0",
        "id": 0,
    })
    input("Press Enter to continue...")
    
    # Send request to find definition for class "Hello"
    lsp_request({
        "method": "textDocument/definition",
        "params": {
            "textDocument": {
                "uri": "file:///home/ec2-user/environment/example/main.py"
            },
            "position": {
                "line": 3,
                "character": 17
            }
        },
        "jsonrpc": "2.0",
        "id": 1,
    })
    input("Press Enter to continue...")
    
    # Send request to get references for class "World"
    lsp_request({
        "method": "textDocument/references",
        "params": {
            "textDocument": {
                "uri": "file:///home/ec2-user/environment/example/world.py"
            },
            "position": {
                "line": 0,
                "character": 8
            },
            "context": {
                "includeDeclaration": True
            }
        },
        "jsonrpc": "2.0",
        "id": 2,
    })
    input("Press Enter to continue...")
    
    # Send request to get signature for method "Hello.say_something"
    lsp_request({
        "method": "textDocument/signatureHelp",
        "params": {
            "textDocument": {
                "uri": "file:///home/ec2-user/environment/example/main.py"
            },
            "position": {
                "line": 4,
                "character": 26
            },
        },
        "jsonrpc": "2.0",
        "id": 3,
    })
    input("Press Enter to continue...")
    
    # Send request to get all document symbols from "main.py"
    lsp_request({
        "method": "textDocument/documentSymbol",
        "params": {
            "textDocument": {
                "uri": "file:///home/ec2-user/environment/example/main.py"
            },
        },
        "jsonrpc": "2.0",
        "id": 4,
    })
    input("Press Enter to continue...")
    
    connection.close()
    
    
    
    
if __name__ == "__main__":
    main()