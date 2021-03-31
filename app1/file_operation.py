import subprocess

def upload_data(file_location,host_ip,dest,ssh_password):
    cmd = f'sshpass -p {ssh_password} scp {file_location} {host_ip}:{dest}'
    output = subprocess.run(cmd, shell=True,capture_output=True,text=True)
    return output

def download_data(host_ip,file_path,dest,ssh_password):
    cmd = f'sshpass -p {ssh_password} scp {host_ip}:{file_path} {dest}'
    output = subprocess.run(cmd, shell=True,capture_output=True,text=True)
    return output





