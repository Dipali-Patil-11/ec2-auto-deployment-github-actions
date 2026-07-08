import os
import paramiko
import sys

print("===================================")
print(" EC2 Automatic Deployment Started ")
print("===================================")

# Read environment variables
HOST = os.environ.get("EC2_HOST")
USERNAME = os.environ.get("EC2_USERNAME")
KEY_FILE = "key.pem"

LOCAL_FILE = "templates/index.html"
REMOTE_TEMP = "/tmp/index.html"
REMOTE_FINAL = "/var/www/html/index.html"

# Check environment variables
if not HOST:
    print("ERROR: EC2_HOST environment variable not found.")
    sys.exit(1)

if not USERNAME:
    print("ERROR: EC2_USERNAME environment variable not found.")
    sys.exit(1)

# Check files
if not os.path.exists(KEY_FILE):
    print("ERROR: key.pem not found.")
    sys.exit(1)

if not os.path.exists(LOCAL_FILE):
    print("ERROR: templates/index.html not found.")
    sys.exit(1)

try:
    print(f"Connecting to {HOST}...")

    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    ssh.connect(
        hostname=HOST,
        username=USERNAME,
        key_filename=KEY_FILE
    )

    print("SSH Connection Successful")

    sftp = ssh.open_sftp()

    print("Uploading index.html...")
    sftp.put(LOCAL_FILE, REMOTE_TEMP)
    sftp.close()

    print("Upload Successful")

    print("Moving file to Apache directory...")

    stdin, stdout, stderr = ssh.exec_command(
        f"sudo mv {REMOTE_TEMP} {REMOTE_FINAL}"
    )

    exit_status = stdout.channel.recv_exit_status()

    if exit_status == 0:
        print("Website Updated Successfully!")
    else:
        print("Deployment Failed")
        print(stderr.read().decode())

    ssh.close()

except Exception as e:
    print("ERROR:")
    print(e)
    sys.exit(1)