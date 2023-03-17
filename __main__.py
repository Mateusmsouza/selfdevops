import pulumi_gcp as gcp

from gcp.compute.gcp_instance import Instance

Instance(count=1, name="myfirsstinstance").compose().run()