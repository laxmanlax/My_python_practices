from multiprocessing import Pool 
import multiprocessing
from email.mime.text import MIMEText


def execute_on_rmote(host):
	cmd = ""
	ssh = Popen(["timeout", "3","ssh", "-o", "StrictHostKeyChecking=no", "-o", "ConnectTimeout=5","%s" %hostname, cmd], shell=False, stdout=PIPE, stderr=PIPE)
	result , error = p.communicate()
	if result:
		send_email(result)


def sendEmail(hosts, sub):
    """
    Send an email with host lists to the user when updating IDB status
    """
    email = "example@gmail.com"
    hostmsg = "Reuslts : {}".format(result)
    msg = MIMEText(hostmsg)
    msg["To"] = email
    msg["Subject"] = sub
    p = Popen(["/usr/sbin/sendmail", "-t", "-oi"], stdin=PIPE)
    p.communicate(msg.as_string())


def process_hosts():
	cpus = multiprocessing.cpu_count()
	pool = Pool(processes=cpus)
	pool.map(execute_on_rmote,host_lists)

