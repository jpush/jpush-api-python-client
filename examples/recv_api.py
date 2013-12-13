from jpush import RecvClient


recv_client = RecvClient('appkey', 'master_secret')
recv_client.get_recv([0, 1, 2])
recv_client.get_recv('0,1,2')
