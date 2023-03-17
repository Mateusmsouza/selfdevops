import pulumi
import pulumi_gcp as gcp


class Instance:

    __urn = "gcpinstance"

    def __init__(self, count: int, name: str) -> None:
        self.__count = count
        self.__name = name

    def compose(self):
        return self

    def run(self):
        instance = gcp.compute.Instance(self.__urn,
        name=self.__name,
        machine_type='n1-standard-1',
        zone='us-central1-a',
        boot_disk=gcp.compute.InstanceBootDiskArgs(
            initialize_params=gcp.compute.InstanceBootDiskInitializeParamsArgs(
                image='debian-cloud/debian-9',
            ),
        ),
        network_interfaces=[gcp.compute.InstanceNetworkInterfaceArgs(
            network='default',
            access_configs=[gcp.compute.InstanceNetworkInterfaceAccessConfigArgs(
                nat_ip=gcp.compute.GlobalAddress('my-address').address,
            )],
        )],
        )

        pulumi.export('instance_selflink', instance.self_link)
        pulumi.export('instance_ip', instance.network_interfaces[0].access_configs[0].nat_ip)
        return self