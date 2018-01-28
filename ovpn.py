#!/usr/bin/env python3
import sys
import os.path
import subprocess
from jinja2 import Template

try:
    common_name = sys.argv[1]
except IndexError:
    sys.stderr.write('Client name?\n')
    sys.exit(1)

command_path = os.path.expanduser('~/easy-rsa/easyrsa.real')
template_path = os.path.expanduser('~/easy-rsa/template.ovpn.jinja')
priv_key_path = os.path.join(os.path.expanduser('~/easy-rsa/pki/private'), '{}.key'.format(common_name))
cert_path = os.path.join(os.path.expanduser('~/easy-rsa/pki/issued'), '{}.crt'.format(common_name))
output_path = os.path.join(os.path.expanduser('~/easy-rsa/'), '{}.ovpn'.format(common_name))

run = subprocess.run('{} build-client-full {} nopass'.format(command_path, common_name), shell=True)
try:
    run.check_returncode()
except subprocess.CalledProcessError:
    sys.exit(1)
else:
    with open(template_path) as tf:
        template_content = tf.read()
    template = Template(template_content)
    with open(priv_key_path) as priv_key_file:
        priv_key = priv_key_file.read().strip()
    with open(cert_path) as cert_file:
        cert = cert_file.read().strip()
    ovpn_content = template.render(private_key=priv_key, certificate=cert)

    with open(output_path, 'w') as ovpn_file:
        ovpn_file.write(ovpn_content)
