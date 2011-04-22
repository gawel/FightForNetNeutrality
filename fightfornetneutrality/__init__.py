# -*- coding: utf-8 -*-
from socket import inet_aton
from struct import unpack
import sys

if sys.version_info[:2] < (2, 6):
    bin = lambda x: "".join(map(lambda y:str((x>>y)&1), range(32-1, -1, -1)))

def ip_in_network(ip, net_addr, net_mask):
    """ Source : http://php.net/manual/fr/function.ip2long.php - jwadhams1 """
    if net_mask <= 0:
        return False
    ip_binary_string = bin(unpack('!I', inet_aton(ip))[0])
    net_binary_string = bin(unpack('!I', inet_aton(net_addr))[0])
    return ip_binary_string[:net_mask] == net_binary_string[:net_mask]

class NetNeutrality(object):

    def __init__(self, app, ips_banned=None):
        self.app = app
        self.ips_banned = ips_banned or {
            "62.160.71.0":24,
            "84.233.174.48":28,
            "80.118.39.160":27
          }
        html = ''.join(['<li>%s/%s</li>' % i for i in sorted(self.ips_banned.items())])
        self.html = HTML_PAGE % dict(html=html)


    def __call__(self, environ, start_response):
        if environ['REMOTE_ADDR'] == "127.0.0.1":
            client_ip = environ['HTTP_X_FORWARDED_FOR']
        else:
            client_ip = environ['REMOTE_ADDR']
        for ip, mask in self.ips_banned.items():
            if ip_in_network(client_ip, ip, mask):
                start_response('403 Forbidden', [('Content-Type', 'text/html; charset=utf-8')])
                return [self.html]
        return self.app(environ, start_response)

HTML_PAGE = """<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html>
<head>
	<meta http-equiv="Content-Type" content="text/html; charset=UTF-8" />
	<title>Ressource inaccessible</title>
	<style>
		h1{font-size:14px; padding-top:5px}
		h2{font-size:12px}
	</style>
</head>
<body>
	<div style="width:800px; margin:0 auto;">
		<img src="http://www.paulds.fr/p4ul/blocked/france.jpg" alt="liberté, égalité, fraternité ET Neutralité" style="float:left; margin-right:20px" />

		<h1>Le serveur (son propriétaire en fait) n'a pas envie de vous laisser accéder à cette ressource...</h1>
		<h2>Et en même temps, vous l'avez bien cherché...</h2>

        <p style="clear:both; text-align:justify; padding-top:50px">Ce nom de
        domaine, ainsi que beaucoup d'autres, ont été saisis par les
        internautes à la suite d'attaques répétées à l'encontre de la
        Neutralité du Net par les pouvoirs publics.</p>
        <p style="text-align:justify;">Conduire, financer, gêrer, superviser,
        diriger ou proposer une atteinte à la Neutralité du Net revient
        basiquement à s'attaquer à la liberté d'expression du peuple et devrait
        être considéré comme une atteinte manifeste aux droits de l'Homme.</p>
		<p style="text-align:justify;">Il n'y aura aucune suite à cette saisie citoyenne.</p>
		<p style="text-align:justify;">Les plages d'adresses IP filtrées sont les suivantes : </p>

		<ul>
        %(html)s
		</ul>
		<p>Plus d'informations ici : <a href="http://reflets.info/optimiser-son-internet-a-la-sauce-marland-militello/">Optimiser son Internet à la sauce Marland-Militello</a></p>

	</div>
</body>
</html>
"""

