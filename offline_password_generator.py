import argparse
import secrets
import math

def create_password(length):
    # Calculate nbytes for the desired length
    nbytes = math.ceil(length * 3 / 4)
    password = secrets.token_urlsafe(nbytes)
    return password[:length]

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Generate a random password.')
    parser.add_argument('length', type=int, help='The length of the password.')
    args = parser.parse_args()
    
    password = create_password(args.length)
    print(password)
