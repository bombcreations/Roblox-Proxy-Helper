import os

folder_path = os.path.dirname(os.path.abspath(__file__))

proxy_file = os.path.join(folder_path, 'proxy.txt')
login_file = os.path.join(folder_path, 'logins.txt')
output_file = os.path.join(folder_path, 'output.txt')

if not os.path.exists(proxy_file) or not os.path.exists(login_file):
    exit()

with open(proxy_file, 'r') as f1:
    proxies = [line.strip() for line in f1 if line.strip()]
with open(login_file, 'r') as f2:
    logins = [line.strip() for line in f2 if line.strip()]

combined = [f"{proxy}:{login}" for proxy, login in zip(proxies, logins)]

with open(output_file, 'w') as out:
    out.write('\n'.join(combined))
