import os

private_path = '/ssl/zerotier/identity.secret'
node_address_file = '/ssl/zerotier/node_address.txt'

def get_node_address(private_file):
    with open(private_file, 'r') as file:
        node_address = file.readline().split(':')[0]
    return node_address

def write_node_address(node_address, output_file):
    with open(output_file, 'w') as file:
        file.write(node_address)

if __name__ == "__main__":
    if os.path.exists(private_path):
        node_address = get_node_address(private_path)
        write_node_address(node_address, node_address_file)
        print(f"Node address {node_address} written to {node_address_file}")
    else:
        print(f"Private file {private_path} does not exist")
